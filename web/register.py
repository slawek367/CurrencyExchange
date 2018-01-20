from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask import request

class Register(Form):

    name = StringField('Name', [validators.Length(min=2, max=50)])
    surrname = StringField('Surrname', [validators.Length(min=2, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Name', [validators.Length(min=6, max=50)])

    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confrim', message='Passwords do not match')
    ])

    confrim = PasswordField('Confrim Password')

        