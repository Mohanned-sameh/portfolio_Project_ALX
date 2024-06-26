from datetime import datetime
from socialmedia import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


"""
User Model
This model represents the user table in the database.
"""


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)
    comments = db.relationship(
        "Comment", backref="author", lazy=True, cascade="all, delete-orphan"
    )
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    likes = db.relationship(
        "likes", backref="user", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"User('{self.id}','{self.username}', '{self.email}', '{self.image_file}')"
        )


"""
Post Model
This model represents the post table in the database.
"""


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    comments = db.relationship(
        "Comment", backref="post", lazy=True, cascade="all, delete-orphan"
    )
    likes = db.relationship(
        "likes", backref="post", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


"""
likes Model
This model represents the likes table in the database.
"""


class likes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)

    def __repr__(self):
        return f"Like('{self.user_id}', '{self.post_id}')"


"""
comment Model
This model represents the comment table in the database.
"""


class Comment(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content}', '{self.date_posted}')"
