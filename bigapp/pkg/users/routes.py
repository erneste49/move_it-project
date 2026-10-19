from flask import Blueprint, render_template, request, redirect, url_for, session
from pkg.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint('users', __name__, template_folder='templates', static_folder='static', url_prefix='/users')

@users.route("/", methods=["GET", "POST"])
def users_homepage():
    if request.method=="POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_pwd = request.form.get('confirm_password')
        if username != None and email != None and password != None and confirm_pwd != None:
            uname = User.query.filter_by(username=username).first()
            email_addr = User.query.filter_by(email=email).first()
            if uname or email_addr:
                return redirect(url_for('users.users_homepage'))
            else:
                if password == confirm_pwd:
                    password_hash = generate_password_hash(password)
                    user = User(username=username, email=email, password_hash=password_hash)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('users.login'))
                    
        else:
            return redirect(url_for('users.users_homepage'))
                    
    
    return render_template("users/home.html")

@users.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email != None and password != None: 
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password_hash,password):
                session['useronline'] = user.id #user is now logged in
                return redirect(url_for('posts.home'))
            else:
                return redirect(url_for('users.login'))
        else:
            return redirect(url_for('users.login'))
    return render_template("users/login.html")

@users.post("/logout/")
def logout():
    if session.get('useronline') != None:
        session.pop('useronline', None)
        session.clear() 
    return redirect(url_for('users.login'))
