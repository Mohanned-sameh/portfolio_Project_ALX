#!/usr/bin/python3
from socialmedia import db, app

app.app_context().push()
db.create_all()
