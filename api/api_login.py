"""
目标：实现登录接口对象封装
"""
#导包
import requests


#新建类：登录接口对象
class ApiLogin:

    # 新建方法：登录方法
    def api_post_login(self, url, mobile, code):
        """
        提示：url、mobile、code:最后都需要从data数据文件读取出来，做参数化使用，所以这里我们动态传参
        :param url:登录url
        :param mobile:电话号码
        :param code:短信验证码
        :return:登录请求的响应对象
        """
        #headers定义
        headers = {"Content-Type": "application/json"}
        # data定义
        data = {"mobile": mobile, "code": code}
        #调用登录post请求并返回响应对象
        return requests.post(url=url, headers=headers, json=data)
