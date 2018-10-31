# -*- coding: UTF-8 -*-
import sys
sys.path.append('../')
from app import *
import random
#db = SQLAlchemy(app)
# me = Admin('')
#print db.metadata.tables
# admin = Admin('')
# me = Admin(user_name='drj',password='123')
# db.session.add(me)
# print Admin.query.all() #查询所有
# de = Admin.query.filter_by(id=3).first()#条件查询
# temp = db.session.query(Admin).fliter(id==1).first()
# db.session.delete(de)
# db.session.commit()
# A1 = Area.query.filter_by(id=1).first()
# A1.rules.append(R1)#向关系表中添加

# l1 = Vlog()

# v1 = Video('VideoFeeds',1)

# #rule
# R1 = Rule('无人区')
# R2 = Rule('安全帽')
# R3 = Rule('工作服')

# db.session.add(R1)
# db.session.add(R2)
# db.session.add(R3)

# #area
# A1 = Area('东1')
# A2 = Area('东2')
# A3 = Area('东3')
# A4 = Area('东4')
# A5 = Area('东5')

# db.session.add(A1)
# db.session.add(A2)
# db.session.add(A3)
# db.session.add(A4)
# db.session.add(A5)

# #area_rules
# R1 = Rule.query.filter_by(id=1).first()
# R2 = Rule.query.filter_by(id=2).first()
# R3 = Rule.query.filter_by(id=3).first()

# A1 = Area.query.filter_by(id=1).first()
# A2 = Area.query.filter_by(id=2).first()
# A3 = Area.query.filter_by(id=3).first()
# A4 = Area.query.filter_by(id=4).first()
# A5 = Area.query.filter_by(id=5).first()

# A1.rules.append(R1)
# A2.rules.append(R2)
# A3.rules.append(R3)
# A4.rules.append(R1)
# A4.rules.append(R2)
# A5.rules.append(R2)
# A5.rules.append(R3)

# db.session.add(A1)
# db.session.add(A2)
# db.session.add(A3)
# db.session.add(A4)
# db.session.add(A5)

# #video
# V1 = Video('VidoFeeds/video1', 1)
# V2 = Video('VidoFeeds/video2', 2)
# V3 = Video('VidoFeeds/video3', 3)
# V4 = Video('VidoFeeds/video4', 4)
# V5 = Video('VidoFeeds/video5', 5)

# db.session.add(V1)
# db.session.add(V2)
# db.session.add(V3)
# db.session.add(V4)
# db.session.add(V5)

# # vlog
# # 删除并把id起始为1
# # DELETE FROM vlog;
# # ALTER TABLE vlog AUTO_INCREMENT = 1;

# a, b, c = 1, 1, 1
# while (a <= 300) :
#     if b > 5 :
#         b, c = 1, 1
#     db.session.add(Vlog("Pic/pic" + str(a), b, c))
#     a += 1
#     b += 1
#     c += 1

# #rule_vlogs
# R1 = Rule.query.filter_by(id=1).first()
# R2 = Rule.query.filter_by(id=2).first()
# R3 = Rule.query.filter_by(id=3).first()

# a = 1
# while (a <= 300):
#     V1 = Vlog.query.filter_by(id=a).first()
#     r = random.randint(1, 3)
#     if r == 1:
#         V1.rules.append(R1)
#     elif r == 2:
#         V1.rules.append(R2)
#     else:
#         V1.rules.append(R3)
#     a += 1

# db.session.commit()


