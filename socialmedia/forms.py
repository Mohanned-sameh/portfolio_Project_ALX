"""
TODO: 
1. Create a form for the user to create a new post
2. Create a form for the user to create a new comment
3. Create a form for the user to register
4. Create a form for the user to login
5. Create a form for the user to update their account
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    content = TextAreaField(
        "Content", validators=[DataRequired(), Length(min=1, max=140)]
    )
    submit = SubmitField("Post")


class CommentForm(FlaskForm):
    content = TextAreaField(
        "Content", validators=[DataRequired(), Length(min=1, max=140)]
    )
    submit = SubmitField("Comment")


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    confirm_password = StringField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Update")
