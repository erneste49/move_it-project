
from datetime import datetime
from pkg import db


class State(db.Model):
    __tablename__ = 'state'
    state_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(255), nullable=False )

    # relationships
    lgas = db.relationship('Localgovernment', backref='state')
    users= db.relationship('User', backref='state' )
    drivers = db.relationship('Driver', backref='state' )
    products = db.relationship('Product', backref='state' )



class Localgovernment(db.Model):
    __tablename__ = 'lga'
    lga_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_id = db.Column(db.Integer, db.ForeignKey(State.state_id, ondelete='CASCADE'),  nullable=False)
    lga_name = db.Column(db.String(255), nullable=False)

    # relationships
    users = db.relationship('User', backref='lga')
    drivers = db.relationship('Driver', backref='lga')
    products = db.relationship('Product', backref='lga')




class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(150), nullable=False )
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(100), nullable=False, unique=True)
    state_id = db.Column(db.Integer, db.ForeignKey(State.state_id), nullable=False)
    lga_id = db.Column(db.Integer, db.ForeignKey(Localgovernment.lga_id), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum('active', 'inactive', 'blocked'), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.Enum('admin', 'user'), default='user', nullable=False)

    #relationship
    products = db.relationship('Product', backref='user' )



class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(150), nullable=False )
    d_state_id = db.Column(db.Integer, db.ForeignKey(State.state_id), nullable=False)
    d_lga_id = db.Column(db.Integer, db.ForeignKey(Localgovernment.lga_id), nullable=False )
    address = db.Column(db.String(255), nullable=False )
    phone = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    status = db.Column(db.Enum('active', 'inactive', 'deactivated'), default='active', nullable=False)
    licence_number = db.Column(db.String(100), nullable=False, unique=True )
    vehicle = db.Column(db.Enum('pickup', 'mini truck', 'box van', 'large truck'), nullable=False )
    plate_number = db.Column(db.String(150), nullable=False, unique=True )






class Relocation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False )
    current_state_id = db.Column(db.Integer, db.ForeignKey(State.state_id), nullable=False)
    current_lga_id = db.Column(db.Integer, db.ForeignKey(Localgovernment.lga_id), nullable=False )
    new_state_id = db.Column(db.Integer, db.ForeignKey(State.state_id), nullable=False)
    new_lga_id = db.Column(db.Integer, db.ForeignKey(Localgovernment.lga_id), nullable=False)
    status = db.Column(db.Enum('pending', 'quoted', 'confirmed', 'in_transit', 'completed', 'cancelled'), default='pending', nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)
    current_address = db.Column(db.String(255), nullable=True)
    new_address = db.Column(db.String(255), nullable=True)
    driver_id = db.Column(db.Integer, db.ForeignKey(Driver.id), nullable=True)
    estimated_cost = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    final_cost = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    items_and_properties = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #relationships
    current_state = db.relationship('State', backref='relocations_from',
    foreign_keys = [current_state_id] )
    new_state = db.relationship('State', backref='relocations_to', foreign_keys = [new_state_id] )

    current_lga = db.relationship('Localgovernment', backref='relocations_from', foreign_keys=[current_lga_id] )
    new_lga = db.relationship('Localgovernment', backref='relocations_to', foreign_keys=[new_lga_id] )

    user = db.relationship('User', foreign_keys=[user_id])
    driver = db.relationship('Driver', foreign_keys=[driver_id])
    payments = db.relationship('RelocationPayment', backref='relocation')


class RelocationPayment(db.Model):
    __tablename__ = 'relocation_payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    relocation_id = db.Column(
        db.Integer,
        db.ForeignKey(Relocation.id, ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    reference = db.Column(db.String(100), nullable=False, unique=True)
    amount_kobo = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum('pending', 'paid', 'failed'), default='pending', nullable=False)
    checkout_url = db.Column(db.String(512), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    paid_at = db.Column(db.DateTime, nullable=True)





class ProductCategory(db.Model):
    __tablename__ = 'productcategory'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(150), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship
    product_cat = db.relationship('Product', backref='productcategory' )



class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False )
    name = db.Column(db.String(200), nullable=False )
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    image_name = db.Column(db.String(255), nullable=False )
    category_id =  db.Column(db.Integer, db.ForeignKey(ProductCategory.id), nullable=False )
    state_id =  db.Column(db.Integer, db.ForeignKey(State.state_id), nullable=False )
    lga_id =  db.Column(db.Integer, db.ForeignKey(Localgovernment.lga_id), nullable=False )
    status = db.Column(db.Enum('available', 'reserved', 'sold'), default='available', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    condition = db.Column(db.Enum('like_new', 'fairly_used', 'good', 'scratched', 'broken'), nullable=False)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False )
    last_name = db.Column(db.String(100), nullable=False )
    email = db.Column(db.String(255), nullable=False )
    phone = db.Column(db.String(100), nullable=False )
    password = db.Column(db.String(255), nullable=False )


