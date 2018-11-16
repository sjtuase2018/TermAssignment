# TermAssignment

1. 从Git上同步TermAssignment
2. 新建项目，将TermAssignment源码复制到项目文件夹
3. 建立虚拟环境
4. 安装必要包，包括flask, flask_sqlalchemy, flask_login, flask_wtf
5. 初始化数据库原型，在terminal中运行flask db.init; flask db.migrate -m "comment"; flask db.upgrade
6. 执行flask.run启动服务器
```
pip install virtualenv

cd ../backend

virtualenv -p python3 venv

venv\Scripts\activate

pip install -r requirements.txt

set FLASK_APP=run.py

set FLASK_ENV=development

set FLASK_ENV=production

flask run
```

### 退出
```
venv\Scripts\deactivate
```

## 深度学习所需必要环境
1. 语言切换至python3.6,第一次迭代的源码在3.6环境下经测试ok
2. 安装tensorflow（tensorflow.org）,有n卡的话请使用gpu版本
3. 安装keras
