from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/course'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)
print('+1s')

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


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    save_path = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    vlogs = db.relationship('Vlog', backref='video', lazy='dynamic')


class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))


class Vlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    pic_path = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    rules = db.relationship('Rule', secondary=vlog_rules)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    logintime = db.Column(db.DateTime)
    loginip = db.Column(db.Integer)

print('+1s')
db.create_all()



