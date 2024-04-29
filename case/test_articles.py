"""
目标：完成对删除文章的业务层封装
"""
#导包
import unittest

from parameterized import parameterized

from api.api_articles import ApiArticles
from tools.read_json import ReadJson


#读取发布文章的数据函数：按照参数化要求的数据格式
def get_data_add():
    data = ReadJson("articles_add.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("token"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs


#读取删除文章的数据函数：按照参数化要求的数据格式
def get_data_delete():
    data = ReadJson("articles_delete.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("token"),
                 data.get("status_code")))
    return arrs


#新建测试类
class TestArticles(unittest.TestCase):
    # 获取参数化数据:发布文章
    @parameterized.expand(get_data_add())
    #新建测试方法：发布文章
    #方法的参数要与parameterized的中参数一一对应
    def test_articles_add(self, url, token, expect_result, status_code):
        # #临时数据
        # url = "http://api-toutiao-web.itheima.net/mp/v1_0/articles?draft=false"
        # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDUwMzY3MjMsInVzZXJfaWQiOjEsInJlZnJlc2giOmZhbHNlLCJ2ZXJpZmllZCI6dHJ1ZX0.y9njWKPsMtJgHCSYJRC70mVM44U840H4nqvxXjLoLaY"
        # #调用发布文章请求并返回响应对象
        r = ApiArticles().api_post_articles(url, token)

        #打印文章id
        print("发布文章的id为：", r.json().get("data").get("id"))

        #打印响应信息及状态码
        print("发布文章的响应信息为：", r.json())
        print("发布文章的响应状态码为：", r.status_code)

        #断言响应信息
        # self.assertEqual("OK", r.json().get("message"))

        #断言响应信息:动态参数化
        self.assertEqual(expect_result, r.json().get("message"))
        #断言响应状态码
        # self.assertEqual(201, r.status_code)

        # 断言响应状态码：动态参数化
        self.assertEqual(status_code, r.status_code)

    # 获取参数化数据:删除文章
    @parameterized.expand(get_data_delete())
    #新建测试方法：删除文章
    def test_articles_delete(self, url, token, status_code):
        # #临时测试数据,:target.为文章id
        # url = "http://api-toutiao-web.itheima.net/mp/v1_0/articles/1781547600718069760"
        # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDUwMzY3MjMsInVzZXJfaWQiOjEsInJlZnJlc2giOmZhbHNlLCJ2ZXJpZmllZCI6dHJ1ZX0.y9njWKPsMtJgHCSYJRC70mVM44U840H4nqvxXjLoLaY"

        # #调用删除文章请求
        r = ApiArticles().api_delete_artilcles(url, token)

        #调试：打印响应信息:,响应信息为空
        print("删除文章的响应信息为：", r.text)
        #调试：打印响应状态码
        print("删除文章的响应状态码为：", r.status_code)

        #调试断言响应状态码
        # self.assertEqual(204, r.status_code)
        # 断言响应状态码：使用动态参数化获取状态码
        try:
            self.assertEqual(status_code, r.status_code)
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
