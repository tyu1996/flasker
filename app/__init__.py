"""
Flask app initialiser
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Set a project base directory variable
baseDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Fl4sk3R'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(baseDir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# This is needed for Flask to navigate webpages
from app import routes  # noqa
