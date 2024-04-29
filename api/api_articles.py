"""
目标：完成删除文章接口的封装
"""
import random

# 导包
import requests


# 新建类：删除文章对象
class ApiArticles:
    # 新建发布文章请求方法
    def api_post_articles(self, url, token):
        #headers定义
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + token}
        #data定义：文章名称用random.randint取不同名称
        data = {"title": "hantest"+str(random.randint(100, 999)), "content": "<p>1</p>", "imgType": "single", "channel_id": 7,
                "cover": {"type": 1, "images": ["http://toutiao-img.itheima.net/FlroLEiqEi1nKPzWennulkyx3-th"]}}

        #调用发布文章post请求并返回响应对象
        return requests.post(url, headers=headers, json=data)

    # 新建方法：删除文章请求方法
    def api_delete_artilcles(self, url, token):
        # headers定义
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + token}
        # 调用删除文章的delete请求并返回响应对象
        return requests.delete(url, headers=headers)
