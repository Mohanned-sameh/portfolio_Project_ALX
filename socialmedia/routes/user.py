
from flask import render_template, url_for, flash, redirect, request, abort
from socialmedia import app, db, bcrypt
from socialmedia.models import User, Post, PostComments
from flask_login import login_user, current_user, logout_user, login_required
from socialmedia.forms import (
    LoginForm,
    RegistrationForm,
    UpdateProfileForm,
    PostForm,
    CommentForm,
)



@app.route("/user/<int:user_id>", methods=["GET"])
def get_user_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    return render_template("user_posts.html", posts=posts)
