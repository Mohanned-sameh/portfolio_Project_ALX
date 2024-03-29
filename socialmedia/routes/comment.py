from flask import url_for, flash, redirect, request, abort
from socialmedia import app, db
from socialmedia.models import Comment
from flask_login import current_user, login_required


@app.route("/post/<int:post_id>/comment", methods=["POST"])
@login_required
def new_comment(post_id):
    form = request.form["content"]
    comment = Comment(content=form, author=current_user, post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    flash("Your comment has been added!", "success")
    return redirect(url_for("get_post_by_id", post_id=post_id))


@app.route("/post/<int:post_id>/comment/<int:comment_id>/update", methods=["POST"])
@login_required
def update_comment(post_id, comment_id):
    # TODO: Create a form for the user to update their comment
    pass


@app.route("/post/<int:post_id>/comment/<int:comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(post_id, comment_id):
    # TODO: Implement feature to delete the user comment
    pass
