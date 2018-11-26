#-*- coding= utf-8 -*-
from . import api
from modules.utils import db_util
from flask import request
import json,requests
#获取项目信息
@api.route('/')
def index():
    project=db_util.select_sql("select * from projects")
    version=db_util.select_sql("select * from versions")
    module=db_util.select_sql("select * from modules")
    dict_items={"datas":{}}
    pro = {"pro_info": []}
    ver={"ver_info":[]}
    mod={"mod_info":[]}

    for item in project:

        #dict_items['project_id']=item[0]
        #dict_items['project_name']=item[2]
        get_item={}
        get_item['pro_name']=item[2]
        get_item['pro_id']=item[0]

        pro['pro_info'].append(get_item)

    for item in version:
        get_item={}
        get_item['ver_name']=item[2]
        get_item['ver_id']=item[0]
        get_item['project_id']=item[3]
        ver["ver_info"].append(get_item)
    for item in module:
        get_item={}
        get_item['mod_name']=item[2]
        get_item['mod_id']=item[0]
        get_item['project_id']=item[3]
        get_item['version_id']=item[4]
        mod['mod_info'].append(get_item)
    pro.update(ver)
    mod.update(pro)
    dict_items['datas'] = mod
    #print dict_items
    return json.dumps(dict_items,encoding='utf-8')
@api.route('/post_inter',methods=['GET','POST'])  #提交添加接口
def post_inter():
    if request.method=='POST':
        #{"pro_name":项目名字,"ver_name":版本,"mod_name":模块,"case_name":用例名字
        #,"case_loc":接口地址,"case_method":请求方式,"req_data":请求数据
        #,"req_header":请求header,"case_assert_type":响应校验方式,"res_expect":预期响应结果}
        data=request.get_data()#获取post数据
        data_result=json.loads(data.decode('utf-8'))['datas']
        pro_name=data_result['pro_name']
        ver_name=data_result['ver_name']
        mod_name=data_result['mod_name']
        case_name=data_result['case_name']
        case_loc=data_result['case_loc']
        case_method=data_result['case_method']
        req_data=data_result['req_data']
        req_header=data_result['req_header']
        case_assert_type=data_result['case_assert_type']
        res_expect=data_result['res_expect']

        # print pro_name
        # print type(pro_name)
        pro_id=db_util.one_sql("select id from projects where project_name='"+pro_name+"'")
        ver_id=db_util.one_sql("select id from versions where version_name='"+ver_name+"'")
        mod_id=db_util.one_sql("select id from modules where module_name='"+mod_name+"'")
        # db_util.exec_sql("insert into inter_info (url,req_method,url_name"
        #                  "project_id,module_id,version_id) VALUES "
        #                  +case_loc+case_method+case_name,)
        #print "insert into inter_info (req_method,url,url_name,project_id,version_id,module_id) values ('" + case_method + "','" + case_name + "','" + str(pro_id[0]) + "','" + str(ver_id[0]) + "','"+ str(mod_id[0]) + "')"
        #添加inter
        result=db_util.one_sql("insert into inter_info (req_method,url,url_name,project_id,version_id,module_id) "
                         +"values ('"+case_method+"','"+case_loc+"','"+case_name+"','"+str(pro_id[0])+"','"+str(ver_id[0])+"','"+str(mod_id[0])+"')")
        #获取到插入成功的值
        inter_id=db_util.get_one()
        print inter_id
        #添加param
        result=db_util.exec_sql("insert into params(inter_id,header_param,param,param_body) values ('"+str(inter_id)+"','"+req_header+"','"+req_data+"','"+res_expect+"')")
        print result
    return data