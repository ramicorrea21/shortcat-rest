from flask import Flask
import os
from dotenv import load_dotenv
from models import db
from flask_migrate import Migrate
from flask_cors import CORS


load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
CORS(app)

db.init_app(app)
migrate = Migrate(app, db)

from routes import *


if __name__ == "__main__":
    app.run(debug=True)