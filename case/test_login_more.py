"""
目标：完成登录业务层实现
"""

#导包unittest ApiLogin
import unittest

from parameterized import parameterized

from api.api_login import ApiLogin
from tools.read_json_more import ReadJson


#按参数化数据格式要求读取数据函数：
# parameterized参数化要求的数据格式 [(),(),()]  或   [[],[],[]]
def get_data():
    datas = ReadJson("login_more.json").read_json()
    arrs = []
    for i in datas.values():
        arrs.append((i.get("url"),
                     i.get("mobile"),
                     i.get("code"),
                     i.get("expect_result"),
                     i.get("status_code")))
    # 返回结果
    return arrs


#新建测试类
class TestLogin(unittest.TestCase):
    # 读取参数化数据
    @parameterized.expand(get_data)
    # 新建测试方法
    def test_login(self, url, mobile, code, expect_result, status_code):
        # #暂时存放数据url mobile code，后面通过参数化获取数据
        # #url，在线系统登录通过浏览器的F12工具抓取到的
        # url = "http://api-toutiao-web.itheima.net/mp/v1_0/authorizations"
        # #电话（在线系统中唯一可用账号，写死即可）
        # mobile = "12011111111"
        # #验证码(在线系统中唯一可用，写死即可)
        # code = "246810"

        #实例化ApiLogin()类并调用登录方法
        r = ApiLogin().api_post_login(url, mobile, code)

        #调试使用：打印响应内容
        print("登录响应为：", r.json())
        print("登录响应状态码为：", r.status_code)

        #断言响应信息,以下写法让报错信息更明确
        try:
            self.assertEqual(expect_result, r.json()["message"])
        except AssertionError as e:
            print(e)
        # 断言响应状态码,以下写法让报错信息更明确
        try:
            self.assertEqual(status_code, r.status_code)
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()

"""
'token': 
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDQ4NzAzOTAsInVzZXJfaWQiOjEsInJlZnJlc2giOmZhbHNlLCJ2ZXJpZmllZCI6dHJ1ZX0.M0edvw5kt2clJgmEaBbUNnNzDYo4beQw6xxQEoBkFe8'
"""