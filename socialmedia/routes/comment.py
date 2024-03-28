
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




@app.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def new_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = PostComments(
            content=form.content.data, author=current_user, post_id=post_id
        )
        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been created!", "success")
        return redirect(url_for("get_post_by_id", post_id=post_id))
    pass


@app.route(
    "/post/<int:post_id>/comment/<int:comment_id>/update", methods=["POST"]
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

