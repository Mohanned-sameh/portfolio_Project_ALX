from flask import render_template, url_for, flash, redirect, request, abort
from socialmedia import app, db
from socialmedia.models import Post, Comment, likes
from flask_login import current_user, login_required
from socialmedia.forms import CommentForm, PostForm


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
    likes = len(post.likes)
    return render_template(
        "post.html",
        title="SocialMedia - Post",
        post=post,
        comments=comments,
        form=form,
        likes=likes,
    )


@app.route("/post/<int:post_id>/like", methods=["POST"])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    if likes.query.filter_by(user_id=current_user.id, post_id=post.id).first():
        flash("You already liked this post!", "info")
    else:
        like = likes(user_id=current_user.id, post_id=post.id)
        db.session.add(like)
        db.session.commit()
        flash("You liked this post!", "success")
    return redirect(url_for("get_post_by_id", post_id=post_id))


@app.route("/post/<int:post_id>/update", methods=["POST", "GET"])
@login_required
def update_post(post_id):
    form = PostForm()
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if request.method == "POST":
        post.content = form.content.data
        post.title = form.title.data
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("get_post_by_id", post_id=post_id))
    form.content.data = post.content
    form.title.data = post.title
    return render_template(
        "update_post.html", title="Update Post", form=form, post=post
    )


@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("home"))
