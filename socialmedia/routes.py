import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from socialmedia import app, db, bcrypt
from socialmedia.models import User, Post, PostComments
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts)


@app.route("/landing-page")
def landing_page():
    return render_template("landing-page.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # TODO: Create a form for the user to register
    pass


@app.route("/login", methods=["GET", "POST"])
def login():
    # TODO: Create a form for the user to login
    pass


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    # TODO: Create a form for the user to update their account
    pass


@app.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    # TODO: Create a form for the user to create a new post
    pass


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = PostComments.query.filter_by(post_id=post.id).all()
    return render_template("post.html", post=post, comments=comments)


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
