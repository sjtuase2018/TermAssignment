# -*- coding: UTF-8 -*-
from app.entity_mapping import *
from sqlalchemy import and_,or_,not_

def Register(username, password):
    user = Admin(username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user.id

def ExitUser(username):
    user = Admin.query.filter_by(user_name=username).first()
    if user != None:
        return True
    return False

def VarifyUser(username, password):
    user = Admin.query.filter_by(user_name=username).first()
    if user.check_password(password):
        print (user.id)
        return user.id
    return None

def LogQuery(sortby, size, startwith, search=None):
    print (sortby, size, startwith, search)
    logs_list = []  
    if search == None:
        logs = Vlog.query.order_by(sortby).offset(startwith).limit(size)
        total = Vlog.query.count()
    else:
        search = '%' + str(search) + '%'
        logs = Vlog.query.\
            filter(Vlog.rule_name.like(search) | Vlog.area_name.like(search) | Vlog.date.ilike(search)).\
            distinct().order_by(sortby).offset(startwith).limit(size)
        total = Vlog.query.\
            filter(Vlog.rule_name.like(search) | Vlog.area_name.like(search) | Vlog.date.ilike(search)).\
            distinct().order_by(sortby).count()
    for log in logs:
        dict_tmp = {}
        dict_tmp['date'] = log.date
        dict_tmp['area'] = log.area_name
        dict_tmp['rule'] = log.rule_name
        dict_tmp['pic_path'] = log.pic_path
        # for rule in log.rules:
        #     dict_tmp['rule'] += (rule.description + ' ')
        logs_list.append(dict_tmp)
    res = {}
    res['logs'] = logs_list
    res['length'] = total
    return res


def GetWeekDayLogNum(startdate, enddate):
    # @pram startdate: '2017-10-1'
    # @pram enddate: '2018-10-1'
    # return: num
    res= [0, 0, 0, 0, 0, 0, 0]
    logs = Vlog.query.filter(Vlog.date.between(startdate, enddate))
    for log in logs:
        w = log.date.weekday()
        res[w] += 1
    return res


def GetLogNumByRule(startdate, enddate, id):
    # @pram startdate: '2017-10-1'
    # @pram enddate: '2018-10-1'
    # @pram id: rule_id
    # return: num
    res= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ruleName = Rule.query.filter_by(id = id).first().description
    logs = Vlog.query.filter(Vlog.date.between(startdate, enddate)).filter_by(rule_name = ruleName).all()
    for log in logs:
        w = log.date.month
        res[w-1] += 1
    return res

def GetAreas():
    # return area name 'id':'name'
    areas = Area.query.all()
    res = {}
    for area in areas:
        res[area.id] = area.description
    return res



def GetLogNumByArea(startdate, enddate, areaid):
    # @pram startdate: '2017-10-1'
    # @pram enddate: '2018-10-1'
    # @pram id: area_id
    # return: num
    areaname = Area.query.filter_by(id=areaid).first().description
    res = Vlog.query.filter(Vlog.date.between(startdate, enddate)).filter_by(area_name=areaname).count()
    return res


def GetRuleByArea(areaid):
    area = Area.query.filter_by(id=areaid).first()
    res = {}
    for rule in area.rules:
        res[rule.id] = rule.description
    return res


def AreaUpdate(areaid, **kw):
    # return update state
    area = Area.query.filter_by(id=areaid).first()
    if area is None:
        print ('area is none')
        return False
    area.description = kw['name']
    rules = db.session.query(Rule).all()
    area.rules = []
    # print 1, area.rules
    # for rule in area.rules:
    #     area.rules.remove(rule)
    # print 2, area.rules
    # rules = kw['rule_list'].split(',')
    rules = kw['rule_list']
    for rule in rules:
        r = db.session.query(Rule).filter(Rule.description == rule).first()
        if r:
            area.rules.append(r)
        else:
            print ('can not find ', r)
    db.session.add(area)
    db.session.commit()
    return True


def NewArea(name, rules):
    # return io state
    newArea = Area(name)
    db.session.add(newArea)
    db.session.commit()
    newArea = Area.query.filter_by(description = name).first()
    rules_list = rules
    # rules_list = rules.split(',')
    for rule in rules_list:
        r = Rule.query.filter_by(description = rule).first()
        if r:
            newArea.rules.append(r)
        else:
            print ('can not find ', r)
    db.session.add(newArea)
    db.session.commit()
    return True


def DeleteArea(id):
    de = Area.query.filter_by(id=id).first()
    db.session.delete(de)
    db.session.commit()
    return True


# 日志生成
def addLog(pic_path, area_id, rule_name, date=None):
    area = Area.query.filter_by(id=area_id).first()
    area_name = area.description
    if date is not None:
        newLog = Vlog(pic_path, area_name, rule_name, date)
    else:
        newlog = Vlog(pic_path, area_name, rule_name)
    db.session.add(newlog)
    db.session.commit()
    return True