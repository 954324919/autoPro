#-*- coding= utf-8 -*-
from modules.utils.db_util import exec_sql,select_sql
#mock时要进行规则匹配才会返回规则的响应
#规则匹配规则
#1.请求方式是否匹配
#2.请求url是否匹配
#3.请求参数是否匹配
def checkpath(path,varsvalue,method):
    #varsvalue 为列表类型，例如：[('hhh', u'123'), ('haotest', u'haighakhg')]
    method=method.lower()
    varsvalue.sort()
    if len(varsvalue)==0:
        pass
def checksize():
    pass