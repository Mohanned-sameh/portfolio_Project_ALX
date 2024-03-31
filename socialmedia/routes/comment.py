from flask import url_for, flash, redirect, request, abort, render_template
from socialmedia import app, db
from socialmedia.models import Comment, Post
from flask_login import current_user, login_required
from socialmedia.forms import CommentForm


@app.route("/post/<int:post_id>/comment", methods=["POST"])
@login_required
def new_comment(post_id):
    form = request.form["content"]
    comment = Comment(content=form, author=current_user, post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    flash("Your comment has been added!", "success")
    return redirect(url_for("get_post_by_id", post_id=post_id))


@app.route("/comment/<int:comment_id>/update", methods=["GET", "POST"])
@login_required
def update_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user:
        abort(403)
    form = CommentForm()
    if request.method == "POST":
        comment.content = form.content.data
        db.session.commit()
        flash("Your comment has been updated!", "success")
        return redirect(url_for("get_post_by_id", post_id=comment.post_id))
    elif request.method == "GET":
        form.content.data = comment.content
    return render_template(
        "update_comment.html", title="Update Comment", form=form, comment=comment
    )


@app.route("/post/<int:post_id>/comment/<int:comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(post_id, comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash("Your comment has been deleted!", "success")
    return redirect(url_for("get_post_by_id", post_id=post_id))
