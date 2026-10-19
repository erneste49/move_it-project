from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired, Length, Email, EqualTo

class ContactForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired(message='Enter your fullname') ])
    email = EmailField('email', validators=[DataRequired(message='Please enter a vailid email')])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')