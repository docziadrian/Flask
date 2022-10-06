from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Felhasználónév foglalt, kérlek válassz másikat!')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Cím foglalt, kérlek válassz másikat!')

    username = StringField(label='Felhasználónév:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Cím:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Jelszó:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Jelszó ismét:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Fiók létrehozása')


class LoginForm(FlaskForm):
    username = StringField(label='Felhasználó:', validators=[DataRequired()])
    password = PasswordField(label='Jelszó:', validators=[DataRequired()])
    submit = SubmitField(label='Bejelentkezés')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Megvásárolom!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Eladom!')