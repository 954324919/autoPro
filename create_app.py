#-*- coding= utf-8 -*-
from flask import Flask,redirect,url_for
from mod import api
#from config import DevelopmentConfig

#app初始化工作 配置环境 实例化数据库模型  注册蓝图
#应用的工厂模式  表示通过某种函数或者对象来创建另一个对象.
def create_app(object_name):
    app=Flask(__name__)
    app.config.from_object(object_name) #这里将环境配置通过外部传入进行初始化工作
    app.config['ALLOWED_EXTENSIONS']=set(['txt','pdf','png','jpg','jpeg','gif','docx','xls','xlsx','sql'])
    #app.config['UPLOAD_FOLDER']='templates/upload/'
    #db.init_app(app)
    app.register_blueprint(api,url_prefix='/api')

    return app
