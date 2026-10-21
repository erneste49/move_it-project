import secrets
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation

from flask import Blueprint, current_app, flash, redirect, request, render_template, url_for, session
import requests

from pkg import db 
from pkg.models import User, Localgovernment, ProductCategory, State, Product, Relocation, RelocationPayment


user = Blueprint('user', __name__, template_folder='templates', static_folder='static', url_prefix="/user")

@user.route("/")
def home():
    if session.get('activeuser') == None:
        return redirect(url_for('home.login'))
    categories = ProductCategory.query.all()
    all_states = State.query.all()
    al_lga = Localgovernment.query.all()
    user_id = session.get('activeuser_id')
    user = User.query.get(user_id)
    if user is None:
        session.clear()
        return redirect(url_for('home.login'))
    all_products = Product.query.filter_by(seller_id=user_id).all()
    relocations = Relocation.query.filter_by(user_id=user_id).order_by(Relocation.created_at.desc()).all()
    
    sold_product = Product.query.filter_by(status="sold").all()
    total_amount_sold = sum([p.price for p in sold_product if p.seller_id == user_id])

    return render_template("/users/user_dashboard.html", categories=categories, states=all_states,  lgas=al_lga,  my_products=all_products, user=user,  relocations=relocations, total_sold=total_amount_sold, )


@user.post('/relocations/pay')
def pay_for_relocation():
    if session.get('activeuser') is None:
        return redirect(url_for('home.login'))

    user = User.query.get(session.get('activeuser_id'))
    if user is None:
        session.clear()
        return redirect(url_for('home.login'))

    relocation_id = request.form.get('relocation_id', type=int)
    if relocation_id is None:
        flash('The relocation request could not be found.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    relocation = Relocation.query.filter_by(id=relocation_id, user_id=user.id).first_or_404()
    if relocation.status != 'quoted' or relocation.driver_id is None:
        flash('Payment is available after a driver is assigned and your request is quoted.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    if any(payment.status == 'paid' for payment in relocation.payments):
        flash('This relocation has already been paid for.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    pending_payment = None
    for old_payment in relocation.payments:
        if old_payment.status == 'pending':
            pending_payment = old_payment
            break
    if pending_payment and pending_payment.checkout_url:
        return redirect(pending_payment.checkout_url)
    if pending_payment:
        pending_payment.status = 'failed'
        db.session.commit()

    secret_key = current_app.config.get('PAYSTACK_SECRET_KEY')
    if not secret_key:
        current_app.logger.error('PAYSTACK_SECRET_KEY is not configured.')
        flash('Online payment is temporarily unavailable. Please contact support.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    amount_kobo = int(Decimal(relocation.estimated_cost) * 100)
    if amount_kobo <= 0:
        flash('The relocation quote has an invalid amount. Please contact support.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    payment = RelocationPayment(
        relocation_id=relocation.id,
        reference=secrets.token_hex(16),
        amount_kobo=amount_kobo,
        status='pending',
    )
    db.session.add(payment)
    db.session.commit()

    callback_url = url_for('user.verify_relocation_payment', _external=True)
    try:
        response = requests.post(
            'https://api.paystack.co/transaction/initialize',
            headers={'Authorization': f'Bearer {secret_key}'},
            json={
                'email': user.email,
                'amount': amount_kobo,
                'currency': 'NGN',
                'reference': payment.reference,
                'callback_url': callback_url,
                'metadata': {
                    'relocation_id': relocation.id,
                    'user_id': user.id,
                },
            },
            timeout=30,
        )
        response.raise_for_status()
        result = response.json()
    except (requests.RequestException, ValueError):
        current_app.logger.exception('Paystack initialization failed for relocation %s.', relocation.id)
        payment.status = 'failed'
        db.session.commit()
        flash('Could not start your payment. Please try again.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    if not isinstance(result, dict) or result.get('status') is not True:
        current_app.logger.error('Paystack did not initialize payment for relocation %s.', relocation.id)
        payment.status = 'failed'
        db.session.commit()
        flash('Could not start your payment. Please try again.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    data = result.get('data')
    if not isinstance(data, dict):
        data = {}
    authorization_url = data.get('authorization_url', '')
    if (
        data.get('reference') != payment.reference
        or not authorization_url.startswith('https://checkout.paystack.com/')
    ):
        current_app.logger.error('Paystack returned an invalid checkout response for relocation %s.', relocation.id)
        payment.status = 'failed'
        db.session.commit()
        flash('Could not start your payment. Please try again.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    payment.checkout_url = authorization_url
    db.session.commit()
    return redirect(authorization_url)


@user.get('/relocations/payment/verify')
def verify_relocation_payment():
    if session.get('activeuser') is None:
        return redirect(url_for('home.login'))

    user = User.query.get(session.get('activeuser_id'))
    if user is None:
        session.clear()
        return redirect(url_for('home.login'))

    reference = request.args.get('reference', '')
    payment = RelocationPayment.query.filter_by(reference=reference).first()
    if payment is None or payment.relocation.user_id != user.id:
        flash('The payment reference could not be found.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))
    if payment.status == 'paid':
        flash('Payment confirmed. Your relocation is confirmed.', 'success')
        return redirect(url_for('user.home', _anchor='relocations'))

    relocation = payment.relocation
    if relocation.status != 'quoted' or relocation.driver_id is None:
        flash('This relocation is not ready for payment verification.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    secret_key = current_app.config.get('PAYSTACK_SECRET_KEY')
    if not secret_key:
        current_app.logger.error('PAYSTACK_SECRET_KEY is not configured.')
        flash('Payment verification is temporarily unavailable. Please contact support.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    try:
        response = requests.get(
            f'https://api.paystack.co/transaction/verify/{payment.reference}',
            headers={'Authorization': f'Bearer {secret_key}'},
            timeout=30,
        )
        response.raise_for_status()
        result = response.json()
    except (requests.RequestException, ValueError):
        current_app.logger.exception('Paystack verification failed for reference %s.', payment.reference)
        flash('We could not verify your payment yet. Please refresh your dashboard or contact support.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    if not isinstance(result, dict) or result.get('status') is not True:
        flash('Paystack could not verify your payment. Please try again or contact support.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    data = result.get('data')
    if not isinstance(data, dict):
        data = {}
    customer = data.get('customer')
    customer_email = customer.get('email') if isinstance(customer, dict) else None
    if (
        data.get('status') != 'success'
        or data.get('reference') != payment.reference
        or data.get('amount') != payment.amount_kobo
        or data.get('currency') != 'NGN'
        or not isinstance(customer_email, str)
        or customer_email.lower() != user.email.lower()
        or payment.amount_kobo != int(Decimal(relocation.estimated_cost) * 100)
    ):
        payment.status = 'failed'
        db.session.commit()
        flash('Payment was not successful or could not be matched to this relocation.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    payment.status = 'paid'
    payment.paid_at = datetime.now(timezone.utc).replace(tzinfo=None)
    relocation.status = 'confirmed'
    db.session.commit()
    flash('Payment confirmed. Your relocation is confirmed.', 'success')
    return redirect(url_for('user.home', _anchor='relocations'))


@user.post('/relocations/<int:relocation_id>/cancel')
def cancel_relocation(relocation_id):
    if session.get('activeuser') is None:
        return redirect(url_for('home.login'))

    user = User.query.get(session.get('activeuser_id'))
    if user is None:
        session.clear()
        return redirect(url_for('home.login'))

    relocation = Relocation.query.filter_by(
        id=relocation_id,
        user_id=user.id,
    ).first_or_404()
    has_pending_payment = any(payment.status == 'pending' for payment in relocation.payments)
    has_paid_payment = any(payment.status == 'paid' for payment in relocation.payments)
    if (
        relocation.status != 'quoted'
        or relocation.driver_id is None
        or has_pending_payment
        or has_paid_payment
    ):
        flash('This request cannot be cancelled while payment is in progress or after its status changes.', 'error')
        return redirect(url_for('user.home', _anchor='relocations'))

    relocation.status = 'cancelled'
    db.session.commit()
    flash('Your relocation request was cancelled.', 'success')
    return redirect(url_for('user.home', _anchor='relocations'))




@user.route("/post/item/", methods=["GET", "POST"])
def post_item():
    if session.get('activeuser') == None:
        return redirect(url_for('home.login'))
    user_id = session.get('activeuser_id')
    
    if request.method == "POST":
        item_name = request.form.get('p_name')
        description = request.form.get('p_description')
        price = request.form.get('p_price')
        image = request.files.get('p_image')
        category_id = request.form.get('p_category')
        state_id = request.form.get('p_state')
        lga_id = request.form.get('p_lga')
        condition = request.form.get('p_condition')
        

        if (item_name, description, price, image, category_id, state_id, lga_id, condition ) :
            filename = image.filename
            _, ext = filename.split('.')
            generated_name = secrets.token_hex(15)
            image_name = f"{generated_name}.{ext}"
            upload_path = f"pkg/users/static/posted_items/{image_name}"
            image.save(upload_path)
            
            new_item = Product(seller_id=user_id, name=item_name, description=description, price=price, image_name=image_name, category_id=category_id, state_id=state_id, lga_id=lga_id, status='available', condition=condition )
            
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('user.home'))
        return redirect(url_for('user.post_item'))
        
        
    return redirect(url_for("user.home"))


@user.post("/products/<int:item_id>/status")
def update_product_status(item_id):
    if session.get('activeuser') is None:
        return redirect(url_for('home.login'))

    product = Product.query.filter_by(
        id=item_id,
        seller_id=session.get('activeuser_id'),
    ).first_or_404()
    new_status = request.form.get('status')
    if new_status not in {'available', 'sold'}:
        return redirect(url_for('user.home'))

    product.status = new_status
    db.session.commit()
    return redirect(url_for('user.home'))


@user.route("/products/<int:item_id>/edit", methods=["GET", "POST"])
def edit_item(item_id):
    if session.get('activeuser') is None:
        return redirect(url_for('home.login'))

    product = Product.query.filter_by(
        id=item_id,
        seller_id=session.get('activeuser_id'),
    ).first_or_404()

    if request.method == "POST":
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        price_value = request.form.get('price', '').strip()
        category_value = request.form.get('category_id', '')
        state_value = request.form.get('state_id', '')
        lga_value = request.form.get('lga_id', '')
        condition = request.form.get('condition', '')

        if not all((name, description, price_value, category_value, state_value, lga_value, condition)):
            return redirect(url_for('user.edit_item', item_id=item_id))

        try:
            price = Decimal(price_value)
            category_id = int(category_value)
            state_id = int(state_value)
            lga_id = int(lga_value)
        except (InvalidOperation, ValueError):
            return redirect(url_for('user.edit_item', item_id=item_id))

        category = db.session.get(ProductCategory, category_id)
        selected_lga = Localgovernment.query.filter_by(
            lga_id=lga_id,
            state_id=state_id,
        ).first()
        allowed_conditions = {'like_new', 'fairly_used', 'good', 'scratched', 'broken'}
        if (
            not price.is_finite()
            or price < 0
            or category is None
            or selected_lga is None
            or condition not in allowed_conditions
        ):
            return redirect(url_for('user.edit_item', item_id=item_id))

        product.name = name
        product.description = description
        product.price = price
        product.category_id = category_id
        product.state_id = state_id
        product.lga_id = lga_id
        product.condition = condition
        db.session.commit()
        return redirect(url_for('user.home'))

    return render_template(
        "users/edit_product.html",
        product=product,
        categories=ProductCategory.query.order_by(ProductCategory.category).all(),
        states=State.query.order_by(State.state_name).all(),
    )


@user.post("/products/<int:item_id>/delete")
def delete_item(item_id):
    if session.get('activeuser') is None:
        return redirect(url_for('home.login'))

    item_to_delete = Product.query.filter_by(
        id=item_id,
        seller_id=session.get('activeuser_id'),
    ).first_or_404()
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('user.home'))



@user.post("/post/<int:product_id>") 
def view_single_product(product_id):
    if session.get('activeuser') is None:
        return redirect(url_for('home.login'))
    product = Product.query.get_or_404(product_id) 
    return render_template("users/view_product_details.html", product=product ) 