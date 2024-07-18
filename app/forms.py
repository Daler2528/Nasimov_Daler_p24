from flask_wtf import FlaskForm
from sqlalchemy.testing.pickleable import User
from wtforms import SelectField , EmailField , PasswordField , SearchField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, EqualTo, Email ,ValidationError

class RegisterForm(FlaskForm):
    full_name = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])

    def validate_full_name(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already taken. Please choose a different one.')

    def validate_username(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already taken. Please choose a different one.')
