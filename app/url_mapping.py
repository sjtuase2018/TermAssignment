# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify
from db_io import ExitUser, VarifyUser, LogQuery, GetWeekDayLogNum, GetLogNumByRule, GetAreas, GetLogNumByArea, GethazardCategoryByArea,\
    AreaUpdate, NewArea, DeleteArea


api = Blueprint('api', __name__)


@api.route('/login/', methods=('POST',))
def login():
    username = request.json['username']
    password = request.json['password']
    if ExitUser(username):
        id = VarifyUser(username, password)
        if id is not None:
            return jsonify({'code': 200, 'username': username, 'userId': id})
    return jsonify({'code': 400})


@api.route('/getCamera/', methods=('GET',))
def getCamera():
    dict_areas = GetAreas()
    list_re = []
    for x in dict_areas.keys():
        dict_tmp = GethazardCategoryByArea(x)
        dict_toAppend = {}
        dict_toAppend['id'] = x
        dict_toAppend['area'] = dict_areas[x]
        dict_toAppend['hazardCategory'] = ''
        for y in dict_tmp.keys():
            dict_toAppend['hazardCategory'] += (dict_tmp[y] + ',')
        list_re.append(dict_toAppend)

    return jsonify(list_re)


@api.route('/getLogs/', methods=('GET','POST'))
def getLogs():
    data = request.get_json()
    # print data
    return jsonify(LogQuery(data['sortby'], data['pagesize'], data['startwith']))


@api.route('/getChart/', methods=('GET', 'POST'))
def getChart():
    data = request.get_json()
    # stdate = data['startTime']
    # enddate = data['endTime']
    stdate = '23233'
    enddate = '2323233'
    list_weekday_num = GetWeekDayLogNum(stdate, enddate)
    list_num_by_rule_1 = GetLogNumByRule(stdate, enddate, 1)
    list_num_by_rule_2 = GetLogNumByRule(stdate, enddate, 2)
    list_num_by_rule_3 = GetLogNumByRule(stdate, enddate, 3)

    dict_area = GetAreas()
    list_seriesData = []
    list_names = []

    for x in dict_area.keys():
        dict_tmp = {}
        dict_tmp['name'] = dict_area[x]
        dict_tmp['value'] = GetLogNumByArea(stdate, enddate, x)
        list_seriesData.append(dict_tmp)
        list_names.append(dict_area[x])

    dict_re = {}
    dict_re['dataWeek'] = list_weekday_num
    dict_re['dataM1'] = list_num_by_rule_1
    dict_re['dataM2'] = list_num_by_rule_2
    dict_re['dataM3'] = list_num_by_rule_3
    dict_re['seriesData'] = list_seriesData
    dict_re['name'] = list_names

    return jsonify(dict_re)


@api.route('/settingSave/', methods=('GET', 'POST'))
def settingSave():
    data = request.get_json()
    areaId = date['id']
    areaName = data['area']
    rules = data['rules'] # list
    if not areaId is None:
        AreaUpdate(areaId, name=areaName, rule_list=rules)
        return jsonify({'code': 200})
    else:
        return jsonify({'code': 400})


@api.route('/settingNew/', methods='POST')
def settingNew():
    data = request.get_json()
    areaName = data['area']
    appliedRules = data['rules'] # list
    if NewArea(areaName, appliedRules):
        return jsonify({'code': 200})
    else:
        return jsonify({'code', 400})

    
@api.route('/settingDelete/', methods=('POST',))
def settingDelete():
    data = request.get_json()
    areaId = data['id']
    if DeleteArea(areaId):
        return jsonify({'code': 200})
    else:
        return 400

