#-*- coding= utf-8 -*-
#在初始化时进行 创建蓝图
from flask import Blueprint

mock_api=Blueprint('mock_api',__name__) #template_folder='templates/api/',static_folder='static/api/'

