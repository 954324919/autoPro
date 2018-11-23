#-*- coding= utf-8 -*-
from . import api
from modules.utils import db_util
import json
@api.route('/')
def index():
    project=db_util.select_sql("select * from projects")
    version=db_util.select_sql("select * from versions")
    module=db_util.select_sql("select * from modules")
    dict_items={"data":{}}
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
    dict_items['data'] = mod
    #print dict_items
    return json.dumps(dict_items,encoding='utf-8')