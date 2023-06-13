#!/usr/bin/env python3

# Since we're using Flask-Migrate instead of pure Alembic, we define the application configuration variables in the application itself.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
# initialized our application for use within our database configuration

if __name__ == '__main__':
    app.run(port=5555, debug=True)