#-*- coding= utf-8 -*-
from flask import Blueprint
api=Blueprint('api',__name__)
#导入apiMod模块,这个必须放在这里
from mod import apiMod