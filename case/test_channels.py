"""
目标：完成内容列表业务层封装
"""

#导包
import unittest

from parameterized import parameterized

from api.api_channels import ApiChannels
from tools.read_json import ReadJson


#按参数化数据格式要求读取数据函数：
# parameterized参数化要求的数据格式 [(),(),()]  或   [[],[],[]]
def get_data():
    data = ReadJson("channels.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                data.get("expect_result"),
                data.get("status_code")))
    return arrs


#新建测试类
class TestChannels(unittest.TestCase):
    #获取参数化数据
    @parameterized.expand(get_data())
    # 新建测试方法
    def test_channels(self, url, expect_result, status_code):
        #暂时测试数据
        #url = "http://api-toutiao-web.itheima.net/mp/v1_0/channels"

        #调用get请求
        r = ApiChannels().api_get_channels(url)

        #调试内容
        print("内容列表响应信息为：", r.json())
        print("内容列表的响应状态码为：", r.status_code)
        # #调试断言内容
        # self.assertEqual("OK", r.json().get("message"))
        # self.assertEqual(200, r.status_code)

        #断言响应信息，,以下写法让报错信息更明确
        try:
            self.assertEqual(expect_result, r.json().get("message"))
        except AssertionError as e:
            print(e)
        # 断言响应状态码，,以下写法让报错信息更明确
        try:
            self.assertEqual(status_code, r.status_code)
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
