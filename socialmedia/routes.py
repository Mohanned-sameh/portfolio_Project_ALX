import os
import secrets
from PIL import Image
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


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts, title="SocialMedia - Home")


@app.route("/landing-page")
def landing_page():
    # return render_template("landing-page.html", title="SocialMedia - Landing Page")
    pass


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Your profile has been created! You are now able to log in", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="SocialMedia - Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="SocialMedia - Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your profile has been updated!", "success")
        return redirect(url_for("profile"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template(
        "profile.html", title="SocialMedia - profile", image_file=image_file, form=form
    )


@app.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    # TODO: Create a form for the user to create a new post
    pass


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    pass


@app.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    # TODO: Create a form for the user to update their post
    pass


@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    # TODO: Implement feature for the user to delete their post
    pass


@app.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def new_comment(post_id):
    # TODO: Create a form for the user to create a new comment
    pass


@app.route(
    "/post/<int:post_id>/comment/<int:comment_id>/update", methods=["GET", "POST"]
)
@login_required
def update_comment(post_id, comment_id):
    # TODO: Create a form for the user to update their comment
    pass


@app.route("/post/<int:post_id>/comment/<int:comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(post_id, comment_id):
    # TODO: Implement feature to delete the user comment
    pass


@app.route("/user/<string:username>")
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).all()
    return render_template("user_posts.html", posts=posts, user=user)
    pass
