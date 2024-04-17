from flask import render_template
from socialmedia import app
from socialmedia.models import Post, User

"""
User Posts
This page allows the user to view all the posts created by a specific user.
"""


@app.route("/user/<int:user_id>", methods=["GET"])
def get_user_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    user = User.query.get(user_id)
    title = "SocialHub - " + user.username
    return render_template("user_posts.html", posts=posts, user=user, title=title)
