
from flask import render_template, request
from pkg import app


@app.route("/")
def index():
    return "<h1> Welcome to my Homepage </h1>"



