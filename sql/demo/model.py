from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/course?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)


area_rules = db.Table('area_rules',
    db.Column('area_id', db.Integer, db.ForeignKey('area.id')),
    db.Column('rule_id', db.Integer, db.ForeignKey('rule.id'))
)

rule_vlogs = db.Table('rule_vlogs',
    db.Column('rule_id', db.Integer, db.ForeignKey('rule.id')),
    db.Column('vlog_id', db.Integer, db.ForeignKey('vlog.id'))
)


class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    videoes = db.relationship('Video', backref='area', lazy='dynamic')
    vlogs = db.relationship('Vlog', backref='area', lazy='dynamic')
    area_rules = db.relationship('Area_rule', secondary=area_rules,
        backref=db.backref('area', lazy='dynamic'))


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    save_path = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    vlogs = db.relationship('Vlog', backref='video', lazy='dynamic')


class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    area_rules = db.relationship('Rule_vlog', secondary=rule_vlogs,
        backref=db.backref('rule', lazy='dynamic'))


class Vlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    pic_path = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    password = db.Column(db.String(20))
    logintime = db.Column(db.DateTime)
    loginip = db.Column(db.Integer)


db.create_all()


