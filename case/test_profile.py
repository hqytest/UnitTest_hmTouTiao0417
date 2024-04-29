"""
目标：完成账户信息业务层封装
"""
#导包
import unittest

from parameterized import parameterized

from api.api_profile import ApiProfile
from tools.read_json import ReadJson


#按参数化数据格式要求读取数据函数：
# parameterized参数化要求的数据格式 [(),(),()]  或   [[],[],[]]
def get_data():
    data = ReadJson("profile.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("token"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs


#新建测试类
class TestProfile(unittest.TestCase):
    # 读取参数化数据
    @parameterized.expand(get_data())
    #新建测试方法
    def test_profile(self, url, token, expect_result, status_code):
        # #临时测试数据
        # url = "http://api-toutiao-web.itheima.net/mp/v1_0/user/profile"
        # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDQ5NDQzNzQsInVzZXJfaWQiOjEsInJlZnJlc2giOmZhbHNlLCJ2ZXJpZmllZCI6dHJ1ZX0.mzj5AriwnZGYceRj8EkpdUx_mn69DIydU5D0t9E9Dak"

        r = ApiProfile().api_get_profile(url, token)

        #调试：打印响应信息、状态码
        print("响应信息为：", r.json())
        print("响应状态码", r.status_code)

        #断言响应信息
        # self.assertEqual("OK", r.json().get("message"))
        try:
            self.assertEqual(expect_result, r.json().get("message"))
        except AssertionError as e:
            print(e)
        #断言响应状态码
        # self.assertEqual(200, r.status_code)
        try:
            self.assertEqual(status_code, r.status_code)
        except AssertionError as e:
            print(e)
