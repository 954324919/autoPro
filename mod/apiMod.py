#-*- coding= utf-8 -*-
from . import api
from modules.utils import db_util
from flask import request,jsonify
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
        #print inter_id
        #添加param
        result=db_util.exec_sql("insert into params(inter_id,header_param,param,param_body) values ('"+str(inter_id)+"','"+req_header+"','"+req_data+"','"+req_data+"')")
        #print result
        db_util.exec_sql("insert into inter_expect_res(inter_id,expect_res,res_assert_type) values ('"+str(inter_id)+"','"+res_expect+"','"+case_assert_type+"')")
    return data
#查询出全部接口列表
@api.route('/case_list',methods=['GET'])
def case_list():
    dict_items = {"datas": {}}
    all_list={"case_list":[]} #这种类型创建列表
    select="select * from inter_info order by id desc"


    result=db_util.select_sql(select)
    for i in result:
        get_pro_name="select project_name from projects where id='"+str(i[6])+"'" #i[6] 表示project_id
        get_ver_name="select version_name from versions where id='"+str(i[7])+"'" #i[7] 表示version_id
        get_mod_name = "select module_name from modules where id='" + str(i[8]) + "'"  # i[8] 表示module_id
        pro_name=db_util.one_sql(get_pro_name)[0]
        ver_name = db_util.one_sql(get_ver_name)[0]
        mod_name = db_util.one_sql(get_mod_name)[0]
        #print pro_name,ver_name,mod_name
        get_item={}
        get_item["pro_name"]=pro_name
        get_item["ver_name"]=ver_name
        get_item["mod_name"]=mod_name
        get_item['case_loc']=i[1] #接口url
        get_item['case_name']=i[3] #接口名字
        all_list['case_list'].append(get_item)

    dict_items['datas']=all_list
    #print dict_items
    return jsonify(dict_items)

#穿梭框中所有的接口
@api.route('/all_case',methods=['GET'])
def all_case():
    select="select * from inter_info order by id desc"
    all_cases=[]

    result=db_util.select_sql(select)
    for i in result:
        id=i[0]   #表示接口id
        sql="select url_name from inter_info where id='"+str(id)+"'"
        url_name=db_util.one_sql(sql)[0]

        get_item={}
        get_item["value"]=str(id)
        get_item["title"]=str(url_name)
        all_cases.append(get_item)
    s={"code":0}
    all_cases.append(s)
    # print all_cases
    return json.dumps(all_cases)
#所有接口
@api.route('/get_case',methods=['GET'])
def get_case():
    mydict={}
    mydict["code"]=0

    select="select * from inter_info order by id desc"
    all_cases=[]

    result=db_util.select_sql(select)
    for i in result:
        id=i[0]   #表示接口id
        sql="select url_name from inter_info where id='"+str(id)+"'"
        url_name=db_util.one_sql(sql)[0]

        get_item={}
        get_item["value"]=str(id)
        get_item["title"]=str(url_name)
        all_cases.append(get_item)
    mydict["data"]=all_cases

    # print all_cases
    return json.dumps(mydict)
#按照项目、版本、模块查询的接口列表
@api.route('/case_select_list',methods=['GET'])
def case_select_list():
    dict_items={"datas":()}
    all_list={"case_list":[]}
    pro_id=request.args.get("pro_id")
    ver_id=request.args.get("ver_id")
    mod_id=request.args.get("mod_id")
    sql="select * from inter_info where project_id='"+str(pro_id)+"' and version_id='"+str(ver_id)+"' and module_id='"+str(mod_id)+"'"
    result=db_util.select_sql(sql)
    for i in result:
        get_item={}
        inter_id=i[0] #接口id
        case_loc=i[1] #接口url
        case_name=i[3] #接口名字
        get_item["inter_id"]=inter_id
        get_item["case_loc"]=case_loc
        get_item["case_name"]=case_name
        all_list["case_list"].append(get_item)
    dict_items['datas']=all_list
    return jsonify(dict_items)

#添加场景
#json 格式：{"scene_name": "这是场景的名称","datas": [{"inter_id": "接口id","get_param_data": "中间变量","expect_res": "这是要校验的数据内容","res_assert_type": "响应数据校验方式","notes": "备注信息"}, {"inter_id": "接口id","get_param_data": "中间变量","expect_res": "这是要校验的数据内容","res_assert_type": "响应数据校验方式","notes": "备注信息"}]}
@api.route('/create_scene',methods=['POST'])
def create_scene():
    if request.method=='POST':
        data = request.get_data()  # 获取post数据
        data_result=json.loads(data.decode('utf-8'))
        scene_name=data_result['scene_name']
        scene_item=data_result['datas']
        db_util.exec_sql("insert into scene_info (scene_name) values ('"+scene_name+"')")
        scene_id=db_util.get_one()

        for i in range(0,len(scene_item)):
            inter_id=scene_item[i]['inter_id']
            scene_item_id=scene_item[i]["scene_item_id"]
            get_param_data=scene_item[i]["get_param_data"]
            expect_res=scene_item[i]['expect_res']
            res_assert_type=scene_item[i]['res_assert_type']
            notes=scene_item[i]['notes']
            db_util.exec_sql("insert into scene_info_item (inter_id,get_param_data,expect_res,res_assert_type,notes,scene_info_id,scene_item_id)"
                             " values ('"+str(inter_id)+"','"+get_param_data+"','"+expect_res+"','"+res_assert_type+"','"+notes+"','"+str(scene_id)+"','"+str(scene_item_id)+   "')")
        return "success"

#查询出全部场景
@api.route('/scene_list',methods=['GET'])
def scene_list():
    dict_items = {"datas": {}}
    all_list={"scene_list":[]} #这种类型创建列表
    select="select * from scene_info order by id desc"


    result=db_util.select_sql(select)
    for i in result:
        get_item={}
        get_item["id"]=i[0]
        get_item["scene_name"]=i[1]
        all_list['scene_list'].append(get_item)

    dict_items['datas']=all_list
    #print dict_items
    return jsonify(dict_items)

#查询出全部场景
@api.route('/get_scene',methods=['GET'])
def get_scene():
    mydict={}
    mydict['code']=0
    li=[]
    select="select * from scene_info order by id desc"


    result=db_util.select_sql(select)
    for i in result:
        get_item={}
        get_item["id"]=i[0]
        get_item["scene_name"]=i[1]
        li.append(get_item)

    mydict["data"]=li
    #print dict_items
    return jsonify(mydict)