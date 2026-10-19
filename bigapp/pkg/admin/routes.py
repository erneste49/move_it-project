from flask import Blueprint, render_template, request, redirect, url_for

admins = Blueprint('admin', __name__, template_folder='templates', static_folder='static', url_prefix='/admin')




@admins.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for('admin.home'))
    return render_template('admin/login.html')


@admins.route("/home")
def home():
    return render_template('admin/index.html')
