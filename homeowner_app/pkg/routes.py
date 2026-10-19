
from flask import render_template, request
from pkg import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact ():
    return render_template("contact.html")

@app.errorhandler(404)
def not_found(er):
    return render_template("404.html")