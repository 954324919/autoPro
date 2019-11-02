#-*- coding= utf-8 -*-
import os,json
from itsdangerous import Signer,TimestampSigner
from flask import Flask,redirect,url_for,request,render_template,current_app,make_response,session
from flask_script import Manager,Server
from create_app import create_app
from config import DevelopmentConfig
from werkzeug import secure_filename
from flask_bootstrap import Bootstrap
#from flask_sqlalchemy import SQLAlchemy

import datetime,pymysql
app=create_app(DevelopmentConfig)
manager=Manager(app)
Bootstrap(app)
#db=SQLAlchemy(app)
manager.add_command("runserver",Server(port=8000))

##实现路由功能，可以将所有请求进行筛选
#思路来源：https://testerhome.com/topics/10238
#github：https://github.com/r455678/simple_mock
'''
@app.route('/<path:path>/<path:path1>', methods=['GET','POST'])
def get_all_task(path,path1):
    npath='/'+path+'/'+path1
    if request.method=='GET':
        varsvalue=request.args.items() #请求的列表

        print varsvalue
    elif request.method=='POST':
        varsvalue=request.form.items()


    return str(path+path1)
@app.route('/<path:path>', methods=['GET','POST'])
def get_all_task1(path):
    return str(path)
'''

@app.route('/',methods=['GET','POST'])
def root():
    return render_template('index1.html')
    #return render_template('index.html')

@app.route('/add_inter')
def add_inter():
    return render_template('autotest/add_case.html')

@app.route('/inter_list')
def inter_list():
    return render_template('autotest/api_zhdq.html')
@app.route('/add_scene')
def add_scene():
    return render_template('autotest/add_scene1.html')
@app.route('/scene_list')
def scene_list():
    return render_template('autotest/api_scene.html')
@app.route('/scene_info',methods=['GET','POST'])
def scene_info():
    scene_id=request.args.get("scene_id")
    return render_template('autotest/scene_info.html',scene_id=scene_id)
@app.route('/task')
def task():
    return render_template('autotest/create_task.html')

@app.route('/task_list')
def task_list():
    return "task_list"

@app.route('/test1')
def test1():
    res=make_response(render_template('autotest/getingdata.html'))
    res.set_cookie('username','root',max_age=100)
    res.set_cookie('password','root')
    session["user"]="hao"
    return res


@app.route('/hehe/<test>')
def hh(test):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chendaqian', db='test1')
    # 创建游标
    cursor = conn.cursor()

    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute("select * from user")
    final=""
    all = cursor.fetchall()
    for results in all:
        if test==results[1]:
            final=results[2]
        else:
            final="2"
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return str(final)

@manager.command  #装饰器
def dev():
    from livereload import  Server
    live_server=Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)
@manager.shell
def make_shell():
    return dict(app=app)

if __name__ == "__main__":
    manager.run()
    #{"touser":"chendaqian | lvguangyi", "toparty":"", "msgtype":"text", "agentid":1000025,"text":{"content": "测试一下，请忽略"}, "safe":"0"}