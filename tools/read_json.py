#导包
import json
import os

from config import base_path


# #方式1、打开json文件并获取文件流
# with open("../data/login.json", "r", encoding="utf-8") as f:
#     # 调用load方法加载文件流
#     data = json.load(f)
#     print(data)


# #方式2、使用函数进行封装，问题文件名是写死的
# def read_json():
#     with open("../data/login.json", "r", encoding="utf-8") as f:
#         # 调用load方法加载文件流
#         data = json.load(f)
#         print(data)
#         return data


#方式3、使用参数替换静态文件名
#新建读取json工具类
class ReadJson:
    #使用初始化方法获取要读取的文件名称
    def __init__(self, filename):
        #1、pathlib库：配置文件config.py中创建了基础路径，利用基础路径构建绝对路径
        # 使用 pathlib 库的 Path 类时，你可以使用正斜杠 / 作为路径分隔符，无论你的代码是在任意类型的操作系统。
        # pathlib 会自动处理路径分隔符的转换，以适应底层操作系统的要求。
        self.filepath = base_path/"data"/filename

        # # 2、OS库、使用相对路径来构建绝对路径，避免由于工作目录的变化而导致的问题
        # # 获取当前测试文件所在的目录
        # test_dir = os.path.dirname(os.path.abspath(__file__))
        # print("当前测试文件所在的目录:", test_dir)
        # # 更改工作目录到测试脚本所在的目录
        # os.chdir(test_dir)
        # #使用相对路径来组装绝对路径
        # self.filepath = os.path.abspath(r"../data/"+filename)
        # print("测试数据json文件的绝对路径：", self.filepath)

        #3、相对路径：不建议使用，Python解释器的当前工作目录并不是这些文件所在的目录，会导致相对路径不生效
        # self.filepath = "../data/"+filename

        # #4、直接写死绝对路径，工作目录变化会导致路径失效。
        # # 使用原始字符串r直接使用windows风格的路径,就不用转义路径中的\为\\了
        # self.filepath = r"D:\PycharmProjects\pyP_hmTouTiao0417\data\{}".format(filename)

    #读取文件方法
    def read_json(self):
        #打开json文件获取文件流
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            # data = json.load(f)
            return json.load(f)


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
    # #1、登录数据调试
    # print("读取的JSON数据：", ReadJson("login.json").read_json())
    # data = ReadJson("login.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("mobile"),
    #              data.get("code"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # # 调试使用
    # print("参数化的数据格式：", arrs)

    # #2、内容列表数据调试
    # print("读取的JSON数据：", ReadJson("channels.json").read_json())
    # data = ReadJson("channels.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("token"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # # 调试使用
    # print("参数化的数据格式：", arrs)

    # #3、内容列表数据调试
    # print("读取的JSON数据：", ReadJson("profile.json").read_json())
    # data = ReadJson("profile.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # # 调试使用
    # print("参数化的数据格式：", arrs)
    #
    # #3、发布文章数据调试
    # print("读取的JSON数据：", ReadJson("articles_add.json").read_json())
    # data = ReadJson("articles_add.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("token"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)
    # # 调试使用
    # print("参数化的数据格式：", arrs)
    #3、删除文章数据调试
    print("读取的JSON数据：", ReadJson("articles_delete.json").read_json())
    data = ReadJson("articles_delete.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("token"),
                 data.get("status_code")))
    # 调试使用
    print("参数化的数据格式：", arrs)
