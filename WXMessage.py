# !/usr/bin/env python
#-*- coding= utf-8 -*-
import requests
import json
'''
发送消息到企业微信
'''
class WXMessage(object):
  def get_token(self):
      #使用corpid   corpsecret获取AccessToken
      corpid="ww356b41417245d850"  #企业ID

      corpsecret="VNpfT368QGpXGdq0JlMwfQ-JRm7EEjCsCZMOrAiRi08"
      company={"corpid":corpid,"corpsecret":corpsecret}
      #{"corpid": "ww356b41417245d850", "corpsecret": "VNpfT368QGpXGdq0JlMwfQ-JRm7EEjCsCZMOrAiRi08"}
      #获取access_token的接口地址(GET)  限200 次/天
      access_token_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
      #获取jsapi_ticket的接口地址(GET)  限200 次/天
      jsapi_ticket_url="https://qyapi.weixin.qq.com/cgi-bin/get_jsapi_ticket?access_token=ACCESSTOKEN"

      res=requests.post(access_token_url,params=company)
      data=json.loads(res.text)
      #print data["access_token"]
      return data["access_token"]
  def send_msg(self):
      agentid = "1000025"  # 企业应用ID
      send_url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+self.get_token()
      values="""
      {"touser" : "chendaqian|lvguangyi",
      "toparty":"",
    "msgtype":"text",
    "agentid":1000025,
    "text":{
      "content": "%s"
    },
    "safe":"0"
    }
      """ % (str("测试一下"))
      req=requests.post(send_url,values)
      print req.content
  def 
if __name__ == "__main__":
    WXMessage().send_msg()

#{"touser":"chendaqian","toparty":"","msgtype":"text","agentid":1000025,"text":{"content": "${message}"},"safe":"0"}
# #固定参数
# def test1(a,b):
#     print a+b  #打印
# test1(4,5)  #调用
#
# #命名参数
# def test2(a,b):
#     print a+b
# test2(b=5,a=4)
#
# #默认参数
# def test3(a,b=5):
#     print a+b
# test3(4)
#
# #不定长参数
# def test4(*args):
#     print args
# test4(4,5,6,7,8,9)