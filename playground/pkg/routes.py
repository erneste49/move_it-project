
from flask import render_template, request, redirect, flash 
from pkg import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact", methods=("GET", "POST"))
def contact():
    if request .method == "POST":
        flash("Form submission successful. Expect a message from us in your email", "success")
        return redirect("/contact")
    return render_template("contact.html")

@app.route("/projects")
def project():
    return render_template("projects.html")

@app.route("/about-us")
def about_us():
    return redirect("/about")   #syntax to use redirect


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")



