"""
目标：完成账户信息接口封装
"""

#导包
import requests


#新建类：账户信息接口对象
class ApiProfile:
    # 新建方法：登录接口方法
    def api_get_profile(self, url, token):
        #headers定义，token需要登录获取，2小时有效
        headers = {"Content-Type": "application/json",
                    "Authorization": "Bearer "+token}
        #调用账户信息get请求并返回响应对象
        return requests.get(url, headers=headers)
