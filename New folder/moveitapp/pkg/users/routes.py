from flask import Blueprint, redirect, request, render_template, url_for


user = Blueprint('user', __name__, template_folder='templates', static_folder='static', url_prefix="/user")

@user.route("/")
def login():
    
    return render_template('/users/login.html')


@user.route("/register/")
def register_user():
    return render_template("users/register.html")


@user.route("/dashboard/")
def user_dashboard():
    return render_template("/users/dashboard.html")
