from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()  

# user = db.Table(
#     'users',
#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('name', db.String(200) ),
#     db.Column('email', db.String(100) ),
#     db.Column('message', db.String(255) )
#     #db.Column('Created_on', db.DateTime, default=datetime.now )
#)


## using ORM to create table for database (name: devdb)

class User(db.Model):
    __tablename__ = 'users' 
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False )
    email = db.Column(db.String(200), nullable=False, unique=True)
    message = db.Column(db.Text )
    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan' )
    profile = db.relationship('Profile', uselist=False, backref='user')     
    #posts = db.relationship("Post", back_populates='user')
    
    def __repr__(self):
        return f"{self.name} - {self.email}"


class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    title = db.Column(db.String(255), nullable=False )
    content = db.Column(db.Text )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id') ) 
    status = db.Column(db.Enum('unpublished', 'draft', 'published'), default='published')
    #user = db.relationship('User', back_populates='posts')
    

class Customer(db.Model):
    __tablename__ = "customers"
    
    cust_id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    cust_name = db.Column(db.String(100), nullable=False )
    cust_email = db.Column(db.String(200), nullable=False, unique=True )
    cust_phone = db.Column(db.String(20), nullable=False )
    cust_datereg = db.Column(db.DateTime, default=datetime.utcnow)
    


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False )
    pic = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True )


#below is how to do many to many relationship
student_course = db.Table (
    'student_course' ,
    db.Column('student_id', db.ForeignKey('student.id')),
    db.Column('course_id', db.ForeignKey('course.id'))
)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False )
    email = db.Column(db.String(100), nullable=False )
    courses= db.relationship("Course", secondary=student_course, back_populates='students')
    
    
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False )
    students= db.relationship('Student', secondary=student_course, back_populates='courses')


    