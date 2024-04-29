#导包
import json
import os
import sys

from config import base_path


#使用参数替换静态文件名
#新建读取json工具类
class ReadJson:
    #使用初始化方法获取要读取的文件名称
    def __init__(self, filename):
        #1、pathlib库：配置文件config.py中创建了基础路径，利用基础路径构建绝对路径
        # 使用 pathlib 库的 Path 类时，你可以使用正斜杠 / 作为路径分隔符，无论你的代码是在任意类型的操作系统。
        # pathlib 会自动处理路径分隔符的转换，以适应底层操作系统的要求。
        self.filepath = base_path/"data"/filename

        # # 2、os库，使用相对路径来构建绝对路径，避免由于工作目录的变化而导致的问题
        # # 获取当前测试文件所在的目录
        # test_dir = os.path.dirname(os.path.abspath(__file__))
        # print("当前测试文件所在的目录:", test_dir)
        # # 更改工作目录到测试脚本所在的目录
        # os.chdir(test_dir)
        # # 使用相对路径来组装绝对路径组装绝对路径
        # self.filepath = os.path.abspath("../data/" + filename)
        # print(self.filepath)

        # #3、相对路径：不建议使用，Python解释器的当前工作目录并不是这些文件所在的目录，会导致相对路径不生效
        # self.filepath = "../data/"+filename

        # #4、直接写死绝对路径，工作目录变化会导致路径失效。
        # # 使用原始字符串r直接使用windows风格的路径,就不用转义路径中的\为\\了
        # self.filepath = r"D:\PycharmProjects\pyP_hmTouTiao0417\data\{}".format(filename)

    #读取文件方法
    def read_json(self):
        #打开json文件获取文件流
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            data = json.load(f)
            return data


"""
问题：
    1、未经过封装无法在别的模块内使用。
    2、数据存储文件有好几个，如果写死，在读取别的文件时无法使用
解决：
    1、进行封装
    2、使用参数替换静态写死的文件名
"""

#打印读取的json数据
if __name__ == '__main__':
    print("读取的JSON数据：", ReadJson("login_more.json").read_json())
    datas = ReadJson("login_more.json").read_json()
    arrs = []
    #data.values()获取字典的所有值
    for i in datas.values():
        arrs.append((i.get("url"),
                     i.get("mobile"),
                     i.get("code"),
                     i.get("expect_result"),
                     i.get("status_code")))
    # 调试使用
    print("参数化的数据格式：", arrs)
