from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
# from flask_login import UserMixin
# from app import login


ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password_hash, role):
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username


area_rules = db.Table('area_rules',
    db.Column('area_id', db.Integer, db.ForeignKey('area.id')),
    db.Column('rule_id', db.Integer, db.ForeignKey('rule.id'))
)

vlog_rules = db.Table('rule_vlogs',
    db.Column('vlog_id', db.Integer, db.ForeignKey('vlog.id')),
    db.Column('rule_id', db.Integer, db.ForeignKey('rule.id'))
)


class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    videoes = db.relationship('Video', backref='area', lazy='dynamic')
    vlogs = db.relationship('Vlog', backref='area', lazy='dynamic')
    rules = db.relationship('Rule', secondary=area_rules)

    def __init__(self, description):
        self.description = description


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    save_path = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    vlogs = db.relationship('Vlog', backref='video', lazy='dynamic')

    def __init__(self, save_path, area_id):
        self.save_path = save_path
        self.area_id = area_id

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, description):
        self.description = description


class Vlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now)
    pic_path = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    rules = db.relationship('Rule', secondary=vlog_rules)

    def __init__(self, pic_path, area_id, video_id, date = datetime.now):
        self.pic_path = pic_path
        self.area_id = area_id
        self.video_id = video_id  
        self.date = date


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    logintime = db.Column(db.DateTime)
    loginip = db.Column(db.Integer)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, user_name, password=None, logintime=None, loginip=None):
        self.user_name = user_name 
        self.password = password
        self.logintime = logintime
        self.loginip = loginip   
# do not modify
# @login.user_loader
# def load_user(uid):
#     return User.query.get(int(uid))