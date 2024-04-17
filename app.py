from socialmedia import app, db

"""
this is the main file that runs the application
"""
app.app_context().push()
db.create_all()
if __name__ == "__main__":
    app.run()
