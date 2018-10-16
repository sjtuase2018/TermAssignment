# TermAssignment

1. 从Git上同步TermAssignment
2. 新建项目，将TermAssignment源码复制到项目文件夹
3. 建立虚拟环境 virtaulenv venv，效果是在项目文件夹下创建了一个venv的目录，激活虚拟环境venv\Scripts\activate(win)  source venv/bin/activate(mac)
4. 安装必要包，包括pip install flask, flask_sqlalchemy, flask_login, flask_wtf, flask_migrate
5. 初始化数据库原型，在terminal中运行flask db init; flask db migrate -m "comment"; flask db upgrade
6. 执行flask run启动服务器
