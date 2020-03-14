from app.models import User
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    SelectField,
)
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo


class SignInForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(message="Required field")]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(message="Required field")]
    )
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign in")


class SignUpForm(FlaskForm):
    username = StringField("User", validators=[DataRequired(message="Required field")])
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Required field"),
            Email(message="Insert a valid email"),
        ],
    )
    password = PasswordField(
        "Password", validators=[DataRequired(message="Required field")]
    )
    password_confirmation = PasswordField(
        "Password confirmation",
        validators=[
            DataRequired(message="Required field"),
            EqualTo("password", message="Password must be equal"),
        ],
    )
    user_role = SelectField(
        "Role", choices=[(0, "Admin"), (1, "User")], coerce=int, validators=[]
    )
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already exists")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email")
