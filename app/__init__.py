from flask import Flask

app = Flask(__name__)
app.debug = True  # Enable debug mode to show detailed errors

from app import routes  # Import routes after the app is created
