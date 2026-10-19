from flask import Blueprint, render_template , request, redirect, url_for , session, jsonify
from werkzeug.utils import secure_filename 
from pkg.models import db, Post, Item, Payment, User
import secrets, os
from dotenv import load_dotenv
import requests 


load_dotenv()


posts = Blueprint('posts', __name__, template_folder='templates' )

@posts.route("/")
def home():
    if session.get('useronline') != None:
        posts = Post.query.order_by(Post.id.desc()).all()
        return render_template("posts/home.html", posts=posts)
    
    return redirect(url_for('users.login'))

@posts.route("/create/", methods=["GET", "POST"])
def create():
    if session.get('useronline') != None:
        if request.method == "POST":
            title = request.form.get ("title")
            content = request.form.get ("content")
            image = request.files.get ("image")
            if title != "" and content != "":
                if image:
                    filename = image.filename
                    #filename = secure_filename(filename)   using jinja secure filename replace lines #1 #2 #3
                    _, ext = filename.split('.')        #1
                    generated = secrets.token_hex(24)   #2
                    new_filename= f"{generated}.{ext}"      #3
                    upload_path = f"pkg/static/uploads/{new_filename}"
                    image.save(upload_path)
                    post = Post(title = title, content=content, image=new_filename)
                    db.session.add(post)
                    db.session.commit()
                    return redirect(url_for('posts.home'))
                else:
                    post = Post(title = title, content=content, image=new_filename)
                    db.session.add(post)
                    db.session.commit()
                    return redirect(url_for('posts.home'))
            else:
                return redirect(url_for('posts.create'))
        return render_template('posts/create.html')
    
    return redirect(url_for('users.login'))
        

@posts.route('/item/create/')
def item_create():
    item1 = Item(name='LG-SmartTv', description='This is a smart Tv produced by LG', price=2500)
    item2 = Item(name='HP Elite Laptop', description='This is a laptop produced by HP', price=1500)
    item3 = Item(name='Hisense Ac', description='This is an air conditioner produced by Hisense', price=500)
    
    db.session.add_all([item1, item2, item3])
    db.session.commit()

    return redirect(url_for('posts.home'))

@posts.route("/items/")
def all_items():
    if session.get('useronline') != None:
        items = Item.query.all()
        return render_template('posts/items.html', items=items)
    return redirect(url_for('users.login'))


@posts.route("/pay/initialize/<int:item_id>/", methods=["POST"])
def pay_initialize(item_id):
    if session.get('useronline') != None:
        user_id = session.get('useronline')
        user = User.query.get(int(user_id))
        item = Item.query.filter_by(id=item_id).first()
        amount = int(item.price) * 100
        reference = f'ITEM-{secrets.token_hex(10)}'
        
        session['reference'] = reference
        
        payment = Payment(amount=amount, reference=reference, item_id=item.id, user_id=user.id, status='pending' )
        db.session.add(payment)
        db.session.commit()
        
        url = 'https://api.paystack.co/transaction/initialize'
        headers = {
            'Content-Type':'appication/json',
            'Authorization': f'Bearer {os.getenv("PAYSTACK_API_SECRET_KEY")}'  
        }
        
        payload = {
            'email': user.email,
            'amount': amount,
            'reference': reference,
            'callback_url' : 'http://127.0.0.1:5000/pay/confirm/'
        }
        
        resp = requests.post(url, json=payload, headers=headers )
        result = resp.json()
        
        if result['status']:
            auth_url = result['data']['authorization_url']
            return redirect(auth_url)
        return redirect(url_for('posts.all_items'))
        
    return redirect(url_for('users.login'))

@posts.route("/pay/confirm/")
def pay_confirm():
    if session.get('useronline') != None:
        ref = request.args.get('trxref')
        reference = session.get('reference')
        if ref == reference:
            url = 'https://api.paystack.co/transaction/verify/' + ref
            headers = {
                'Content-Type':'appication/json',
                'Authorization': f'Bearer {os.getenv("PAYSTACK_API_SECRET_KEY")}'  
            }
            resp = requests.get(url, headers=headers)
            result = resp.json()
            
            payment = Payment.query.filter_by(reference=ref).first()
            
            if result['status']:
                payment.status = 'success'
                db.session.commit()
                return redirect(url_for('posts.all_items'))
            
            payment.status = 'failed'
            db.session.commit()
            return redirect(url_for('posts.all_items'))
        
        return redirect(url_for('posts.all_items'))
        
    return redirect(url_for('users.login')) 