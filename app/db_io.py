# from entity_mapping import *


def ExitUser(username):
    return True


def VarifyUser(username, password):
    return 2


def LogQuery(sortby, size, startwith):
    print sortby, size, startwith
    return {}


def GetWeekDayLogNum(startdate, enddate):
    return [20, 30, 40, 50, 60, 70, 10]


def GetLogNumByRule(startdate, enddate, id):
    return [12,12,12,12,12,12,12,12,12,12,12,12]

def GetAreas():
    # return area name 'id':'name'
    return {'1': 'name1', '2': 'name2', '3': 'name3'}


def GetLogNumByArea(startdate, enddate, id):
    return 100


def GethazardCategoryByArea(areaid):
    return {'1': 'name1', '2': 'name2'}


def AreaUpdate(areaid, **kw):
    # return update state
    return true


def NewArea(name, rules):
    # return io state
    return true

def DeleteArea(id):

    return true
