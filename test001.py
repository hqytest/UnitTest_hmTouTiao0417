import random

import requests

# #登录接口
# url = "http://api-toutiao-web.itheima.net/mp/v1_0/authorizations"
# mobile = "12011111111"
# # 短信验证码获取
# code = "246810"
# #headers定义
# headers = {"Content-Type": "application/json"}
# # data定义
# data = {"mobile": "12011111112", "code": "246810"}
# r = requests.get(url, headers=headers)
# print(r.text)
# print(r.status_code)

#内容列表接口
# 暂时测试数据,:target.为文章id
url = "http://api-toutiao-web.itheima.net/mp/v1_0/articles/1781545741844480000"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDUwMzY3MjMsInVzZXJfaWQiOjEsInJlZnJlc2giOmZhbHNlLCJ2ZXJpZmllZCI6dHJ1ZX0.y9njWKPsMtJgHCSYJRC70mVM44U840H4nqvxXjLoLaY"

#headers定义
headers = {"Content-Type": "application/json",
            "Authorization": "Bearer "+token}

# headers = {"Content-Type": "application/json"}

r = requests.delete(url, headers=headers)
print(r.text)
print(r.status_code)
print("hantest"+str(random.randint(100, 999)))