from flask import render_template, redirect, url_for, request
from pkg import app 
from pkg.models import db, User , Post


@app.route("/create/")
def create():
    user = User(name="Smith", email="smith@example.com", message="i am smith, Good to be here")
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for("read"))


@app.route("/read/")
def read():
    users = db.session.query(User).all()
    posts = Post.query.all()
    #print(users)
    return render_template("read.html", users=users, posts=posts)


@app.route("/update/")
def update():
    user = User.query.get_or_404 (3)
    user.email = "mark@gmail.com"
    user.message = "I love database"
    db.session.commit()
    
    return redirect(url_for("read"))


@app.route("/delete/")
def delete():
    user = db.session.query(User).get_or_404(2)
    db.session.delete(user)
    db.session.commit()
    
    return redirect(url_for("read"))


@app.route("/post_create/")
def post_create():
    post = Post(title="Food is Important", content="I love food it is good for the body", user_id=1)
    #post2 = Post(title="practice always", content="I love to practice always so i can be good", user_id=3)
    
    #db.session.add_all([post1, post2])
    db.session.add(post)
    db.session.commit()
    return redirect(url_for("read"))




