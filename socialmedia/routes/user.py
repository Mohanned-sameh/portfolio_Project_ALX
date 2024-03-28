from flask import render_template
from socialmedia import app
from socialmedia.models import Post


@app.route("/user/<int:user_id>", methods=["GET"])
def get_user_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    return render_template("user_posts.html", posts=posts)
