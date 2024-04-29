"""
目标：实现内容列表接口对象封装
"""

#导包
import requests


#新建类
class ApiChannels:
    #新建请求方法
    def api_get_channels(self, url):
        #headrs定义
        headers = {"Content-Type": "application/json"}
        #调用内容列表接口的get请求
        return requests.get(url, headers=headers)
