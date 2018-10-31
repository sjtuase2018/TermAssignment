# -*- coding: UTF-8 -*-
from app import db
# from flask_login import login_required, current_user, login_user, logout_user
from flask import render_template, redirect, url_for, flash, request, Blueprint, jsonify
# from flask_wtf import FlaskForm
# from wtforms import SubmitField, StringField, PasswordField, BooleanField, TextAreaField
# from wtforms.validators import DataRequired, ValidationError, EqualTo
# from werkzeug.urls import url_parse
# from app.entity_mapping import User
# from models import db, User
from entity_mapping import *
import json

api = Blueprint('api', __name__)

@api.route('/login/', methods=('POST',))
def login():
    # print(request)
    # # print(data['username']) wrong
    # print(data)
    # username = request.get_json('username')
    # password = request.json.get('password')
    # if username and password:
    #     print('ok')
    a = request.json['username']
    b = request.json['password']
    if Admin.query.filter_by(user_name = a).first() == None:
        u = Admin(user_name=a, password=b)
        db.session.add(u)
        db.session.commit()
    return jsonify({'code': 200, 'hello': '11'})

@api.route('/getCamera/', methods=('GET',))
def getCamera():
    res = Area.query.all()
    cam = Video.query.filter_by(id=1).first()
    # temp = []
    # for x in res:
    #     temp.append(x.to_json())
    # return jsonify(objects = temp)
    return jsonify({
            'id': '01',
            'area': '101',
            'hazardCategory': 'A'
        },
        {
            'id': '02',
            'area': '102',
            'hazardCategory': 'B',
        })

@api.route('/getLogs/', methods=('GET','POST'))
def getLogs():
    data = request.get_json()
    print(data)
    return jsonify({
            'time': '2018.10.21/19:11:14',
            'area': 101,
            'hazardCategory': 'A'
          },
          {
            'time': '2018.10.21/19:11:14',
            'area': 101,
            'hazardCategory': 'A'
          },
        )

@api.route('/getChart/', methods=('GET',))
def getChart():
    
    return jsonify(
        {
            'dataWeek': [820, 932, 901, 934, 1290, 1330, 1320],
            'dataM1': [6, 9, 10, 15, 25, 76, 135, 162, 32, 20, 6, 3],
            'dataM2': [2, 5, 9, 26, 28, 70, 175, 182, 48, 18, 6, 2],
            'dataM3': [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 4, 2],
            'name': ['地区1', '地区2', '地区3'],
            'value': [10, 10, 10]
        }
        )

@api.route('/settingEdit/', methods=('POST',))
def settingEdit():
    data = request.get_json()
    print(data)
    return jsonify({'code': 200, 'hello': '11'})

    
@api.route('/settingDelete/', methods=('DELETE',))
def settingDelete():
    data = request.get_json()
    print(data)
    return jsonify({'code': 200, 'hello': '11'})