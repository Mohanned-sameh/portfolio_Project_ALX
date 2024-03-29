from flask import render_template, url_for, flash, redirect, request
from socialmedia import app, db
from socialmedia.models import Post, Comment
from flask_login import current_user, login_required
from socialmedia.forms import CommentForm


@app.route("/post/new", methods=["POST"])
@login_required
def add_new_post():
    form = request.form["content"]
    title = request.form["title"]
    post = Post(content=form, author=current_user, title=title)
    db.session.add(post)
    db.session.commit()
    flash("Your post has been created!", "success")
    return redirect(url_for("home"))


@app.route("/post/<int:post_id>", methods=["GET"])
def get_post_by_id(post_id):
    form = CommentForm()
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template(
        "post.html", title="SocialMedia - Post", post=post, comments=comments, form=form
    )


@app.route("/post/<int:post_id>/like", methods=["POST", "GET"])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    db.session.commit()
    return redirect(url_for("get_post_by_id", post_id=post_id))


@app.route("/post/<int:post_id>/update", methods=["POST"])
@login_required
def update_post(post_id):
    form = request.form["content"]
    post = Post.query.get_or_404(post_id)
    post.content = form
    db.session.commit()
    flash("Your post has been updated!", "success")
    return redirect(url_for("home"))


@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("home"))
