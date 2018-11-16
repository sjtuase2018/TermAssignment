# -*- coding: UTF-8 -*-
from entity_mapping import *
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
        print user.id
        return user.id
    return None

def LogQuery(sortby, size, startwith):
    print sortby, size, startwith
    res = []
    logs = Vlog.query.order_by(sortby).offset(startwith).limit(size)
    for log in logs:
        dict_tmp = {}
        dict_tmp['date'] = log.date
        dict_tmp['area'] = log.area_id
        dict_tmp['rule'] = ''
        dict_tmp['pic_path'] = log.pic_path
        for rule in log.rules:
            dict_tmp['rule'] += (rule.description + ' ')
        res.append(dict_tmp)
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
    logs = Vlog.query.filter(Vlog.date.between(startdate, enddate))
    for log in logs:
        w = log.date.month
        res[w] += 1
    return res

def GetAreas():
    # return area name 'id':'name'
    areas = Area.query.all()
    res = {}
    for area in areas:
        res[area.id] = area.description
    return res



def GetLogNumByArea(startdate, enddate, id):
    # @pram startdate: '2017-10-1'
    # @pram enddate: '2018-10-1'
    # @pram id: area_id
    # return: num
    res = Vlog.query.filter(Vlog.date.between(startdate, enddate)).filter_by(area_id =id).count()
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
        print 'area is none'
        return False
    area.description = kw['name']
    rules = db.session.query(Rule).all()
    area.rules = []
    # print 1, area.rules
    # for rule in area.rules:
    #     area.rules.remove(rule)
    # print 2, area.rules
    rules = kw['rule_list'].split(',')
    for rule in rules:
        r = db.session.query(Rule).filter(Rule.description == rule).first()
        if r:
            area.rules.append(r)
        else:
            print 'can not find ', r
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
            print 'can not find ', r
    db.session.add(newArea)
    db.session.commit()
    return True


def DeleteArea(id):
    de = Area.query.filter_by(id=id).first()
    db.session.delete(de)
    db.session.commit()
    return True
