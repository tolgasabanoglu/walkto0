from flask import Flask

app = Flask(__name__)

# Import routes so they get registered with the app
from app import routes
