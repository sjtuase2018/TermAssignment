import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
# app.config.from_object('config')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/course'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    #
    return render_template("index.html")


db = SQLAlchemy(app)
migrate = Migrate(app, db)


# login = LoginManager(app)
# login.login_view = 'login'


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/applog.log', maxBytes=10240,backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('server startup')

# from app import url_mapping, entity_mapping
# from app import video_stream
# from app.url_mapping import api
from app.entity_mapping import *
from app.url_mapping import *
from app.video_stream import *
app.register_blueprint(api, url_prefix="/api")
