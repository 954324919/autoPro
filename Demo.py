# !/usr/bin/env python
#-*- coding= utf-8 -*-
import requests
import json
import  unittest

'''
发送消息到企业微信
'''
class WXMessage(object):
  def get_token(self,str1):
    str2=""
    for i in str1:
        i.strip()
        i.replace("\n","")
        str2=str2+i
    print str2
  def token_give(self):
      data={'activity_id':6773,'name':"测试1号",'phone':13051711789}
      #参加课程
      cook=dict(mvp_token='123')
      requests.get("http://api-liuhaibo.office-public.tengyue360.com/yzs/api/promo/common/participate",params=data,)




if __name__ == "__main__":
    WXMessage().token_give()
