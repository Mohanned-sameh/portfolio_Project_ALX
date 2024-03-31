from socialmedia import app, db

app.app_context().push()
if __name__ == "__main__":
    db.create_all()
    app.run()
