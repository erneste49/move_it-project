from flask import Blueprint, render_template, request, redirect, url_for 
#from pkg.models import db, Post
import secrets


home = Blueprint('home', __name__, template_folder='templates')

@home.route("/")
def home_page():
    return render_template("home/index.html")

@home.route("/relocate/")
def relocate():
    return render_template("home/relocate.html")