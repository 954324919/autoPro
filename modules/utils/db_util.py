#-*- coding= utf-8 -*-
from __future__ import division
import os,datetime
import hashlib
from sqlalchemy import Column,create_engine,Integer,String
from sqlalchemy.types import CHAR,VARCHAR,DATETIME,Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
'''
#创建对象基类
Base=declarative_base()

class PasteFile(Base):
    #表名字
    __tablename__= 'PasteFile'

    #表结构
    id=Column(Integer,autoincrement=True,primary_key=True,nullable=False)
    filename=Column(VARCHAR(5000),nullable=False)
    filehash=Column(VARCHAR(128),nullable=True,unique=True)
    filemd5=Column(VARCHAR(128),nullable=False)
    uploadtime=Column(DATETIME,nullable=False)
    mimetype=Column(VARCHAR(256),nullable=False)
    size=Column(Float(unsigned=True),nullable=False)
    fileurl=Column(String(128))
    def __init__(self,filename=None,filehash=None,filemd5=None,uploadtime=None,mimetype=None,size=None,fileurl=None):
        self.filename=filename
        self.filehash=filehash
        self.filemd5=filemd5
        self.uploadtime=uploadtime
        self.mimetype=mimetype
        self.size=size
        self.fileurl=fileurl
    def __repr__(self):
        return '%s (%r,%r,%r,%r,%r,%r,%r)' % (self.__class__.__name__,self.filename,self.filehash,self.filemd5,self.uploadtime,self.mimetype,self.size,self.fileurl)
#初始化数据库连接.
engine=create_engine('mysql://root:root@localhost:3306/test1')
#创建DBSession类型
DBSession=sessionmaker(bind=engine)
#创建session对象
session=DBSession()
#创建新的PasteFile对象
new_file=PasteFile(id=1,filename='unit.sql',filemd5='hgejglaj089jkgkajngkfdj',uploadtime='2016-10-08 10:18:30',mimetype='sql',size='50.2'
                   )
#添加到session
session.add(new_file)
#提交即保存到数据库
session.commit()
#关闭session连接
session.close()

#从数据库查询数据
session=DBSession()
#创建Query查询,filter是where条件 最后调用one()返回唯一行,如果调用all() 则返回所有行
#myfile=session.query(PasteFile).filter(PasteFile.size>60).one()
#myfiles=session.query(PasteFile).filter().all()
#print type(myfiles)
#for myfile in myfiles:
#    print myfile.uploadtime
#打印类型和对象的创建时间属性
#print 'type:',type(myfile)
#print 'uploadtime:', myfile.uploadtime
#关闭session连接
#session.close()
'''
# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='chendaqian', db='ty_test')
# 创建游标
cursor = conn.cursor()
'''
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from user")
print effect_row
# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

# row=cursor.fetchall()  查询出所有受影响的行
# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
'''
def exec_sql(sql):
    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    return effect_row
def select_sql(sql):
    cursor.execute(sql)
    result=cursor.fetchall()
    return result
h=select_sql("select * from user where id=2")
print h