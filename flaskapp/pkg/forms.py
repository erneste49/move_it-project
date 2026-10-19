from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='cannot be empty'), Length(min=3) ])
    firstname = StringField('Firstname', validators=[DataRequired(message='cannot be empty')])
    lastname = StringField('Lastname', validators=[DataRequired(message='cannot be empty')] )
    email = EmailField('Email', validators=[DataRequired(message='cannot be empty'), Email(message="email does not exist or is incorrect") ])
    password = PasswordField('Password', validators=[DataRequired(message='cannot be empty')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message='cannot be empty'),EqualTo('password', message='passwords do not match, password must be the same')])
    submit = SubmitField('Register Now')
    
    


