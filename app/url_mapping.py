# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify
from app.db_io import Register, ExitUser, VarifyUser, LogQuery, GetWeekDayLogNum, GetLogNumByRule, GetAreas, GetLogNumByArea, GetRuleByArea,\
    AreaUpdate, NewArea, DeleteArea, GetRule
# from app import _pool

api = Blueprint('api', __name__)


cameraOn = [False for i in range(len(GetAreas()))]


# realTime
@api.route('/active/', methods=('POST','GET'))
def active():
    print('active')
    cameraId = request.json['cameraId']
    from app import figure_scanner, helmet_scanner, cams
    from camera.camera_sim import Camera
    # rules = GetRule()
    # for rule in rules:
    #     if '无人区' in rule:
    #         figure_scanner.switch_signal(cams[cameraId])
    #         figure_scanner.active()
    #     else if '安全帽' in rule:
    #         helmet_scanner
    rules = GetRule(cameraId)
    print(rules)
    if '无人区' in rules:
        print('+无人区')
        figure_scanner.switch_signal(Camera(int(cameraId)))
        figure_scanner.active()
    elif '安全帽' in rules:
        print('+安全帽')
        helmet_scanner.switch_signal(Camera(int(cameraId)))
        helmet_scanner.active()
    return jsonify({'code': 200})



@api.route('/deactive/', methods=('POST','GET'))
def deactive():
    print('deactive')
    cameraId = request.json['cameraId']
    global cameraOn
    if (cameraId == 0):
        return jsonify({'code': 200, 'cameraOn': cameraOn})
    index = request.json['index']
    from app import figure_scanner, helmet_scanner
    figure_scanner.deactive()
    helmet_scanner.deactive()
    # from app import cameraOn
    cameraOn = [False for i in range(len(GetAreas()))]
    cameraOn[index] = True
    return jsonify({'code': 200, 'cameraOn': cameraOn})


# register
@api.route('/register/', methods=('POST',))
def register():
    username = request.json['username']
    password = request.json['password']
    if ExitUser(username):
        return jsonify( {'error': 'already exit username'}), 400
    id = Register(username, password)
    return jsonify({'code': 200, 'username': username, 'userId': id})


# login
@api.route('/login/', methods=('POST',))
def login():
    username = request.json['username']
    password = request.json['password']
    if ExitUser(username):
        id = VarifyUser(username, password)
        if id is not None:
            return jsonify({'code': 200, 'username': username, 'userId': id})
    return jsonify({'code': 400})


# charts
@api.route('/getChart/', methods=('GET', 'POST'))
def getChart():
    data = request.get_json()
    stdate = data['startTime']
    enddate = data['endTime']
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


# logs
@api.route('/getLogs/', methods=('GET','POST'))
def getLogs():
    data = request.get_json()
    print (data)
    if 'search' in data:
        return jsonify(LogQuery(data['sortby'], data['pagesize'], data['startwith'], data['search']))
    return jsonify(LogQuery(data['sortby'], data['pagesize'], data['startwith']))


# settings
@api.route('/getCamera/', methods=('GET',))
def getCamera():
    dict_areas = GetAreas()
    list_re = []
    for x in dict_areas.keys():
        dict_tmp = GetRuleByArea(x)
        dict_toAppend = {}
        dict_toAppend['id'] = x
        dict_toAppend['area'] = dict_areas[x]
        dict_toAppend['rules'] = []
        for y in dict_tmp.keys():
            dict_toAppend['rules'].append(dict_tmp[y])
        list_re.append(dict_toAppend)

    return jsonify(list_re)


@api.route('/settingSave/', methods=('GET', 'POST'))
def settingSave():
    data = request.get_json()
    areaId = data['id']
    areaName = data['area']
    rules = data['rules'] # string
    if not areaId is None:
        AreaUpdate(areaId, name=areaName, rule_list=rules)
        return jsonify({'code': 200})
    else:
        return jsonify({'code': 400})


@api.route('/settingNew/', methods=('POST',))
def settingNew():
    data = request.get_json()
    areaName = data['area']
    appliedRules = data['rules'] # string 无人区,安全帽,
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

