"""
    目标：
    1.搜索组装测试套件
    2,运行测试套件并生成测试报告
"""
import os
import time
#1、导包
import unittest

from config import base_path
from tools.HTMLTestRunner import HTMLTestRunner
import os
import sys
#实例化套件对象并加载测试用例
#1、pathlib库：配置文件config.py中创建了基础路径，利用基础路径构建绝对路径
#使用 pathlib 库的 Path 类时，你可以使用正斜杠 / 作为路径分隔符，无论你的代码是在任意类型的操作系统。
# pathlib 会自动处理路径分隔符的转换，以适应底层操作系统的要求。
path = base_path/"case"
suite = unittest.defaultTestLoader.discover(path, "test*.py")

# #2、os库，使用相对路径来构建绝对路径，避免由于工作目录的变化而导致的问题
# # 获取当前测试文件所在的目录
# test_dir = os.path.dirname(os.path.abspath(__file__))
# print("当前测试文件run_suite所在的目录:", test_dir)
# # 更改工作目录到测试脚本所在的目录
# os.chdir(test_dir)
#
# #使用相对路径来组装绝对路径
# path = os.path.abspath("./case")
# print("case的绝对路径", path)
#
# #使用绝对路径来找到测试用例
# suite = unittest.defaultTestLoader.discover(path, "test*.py")

# #3、相对路径：不建议使用，Python解释器的当前工作目录并不是这些文件所在的目录，会导致相对路径不生效
# suite = unittest.defaultTestLoader.discover("./case", "test*.py")

# # 4、直接写死绝对路径，工作目录变化会导致路径失效。
# # 使用原始字符串r直接使用windows风格的路径,就不用转义路径中的\为\\了
# suite = unittest.defaultTestLoader.discover(r"D:\PycharmProjects\pyP_hmTouTiao0417\case", "test*.py")


#实例化第三方运行对象并运行套件对象、生成测试报告

#1、pathlib库：配置文件config.py中创建了基础路径，利用基础路径构建绝对路径
#使用 pathlib 库的 Path 类时，你可以使用正斜杠 / 作为路径分隔符，无论你的代码是在任意类型的操作系统。
# pathlib 会自动处理路径分隔符的转换，以适应底层操作系统的要求。
filepath = base_path/"report"/"report_HmTouTiao{}.html".format(time.strftime("%Y-%m-%d"))

# #2、os库，使用相对路径来构建绝对路径，避免由于工作目录的变化而导致的问题
# # 获取当前测试文件所在的目录
# test_dir2 = os.path.dirname(os.path.abspath(__file__))
# print("当前测试文件run_suite所在的目录2:", test_dir2)
# # 更改工作目录到测试脚本所在的目录
# os.chdir(test_dir2)
#
# #测试报告文件存放路径
# filepath = "./report/report_HmTouTiao{}.html".format(time.strftime("%Y-%m-%d"))
#
# #使用相对路径来组装绝对路径
# filepath = os.path.abspath(filepath)
# print("测试报告的绝对路径:", filepath)

# #3、相对路径：不建议使用，Python解释器的当前工作目录并不是这些文件所在的目录，会导致相对路径不生效
# filepath = "./report/report_HmTouTiao{}.html".format(time.strftime("%Y-%m-%d"))


# #4、直接写死绝对路径，工作目录变化会导致路径失效。
# #使用原始字符串r直接使用windows风格的路径,就不用转义路径中的\为\\了
# filepath = r"D:\PycharmProjects\pyP_hmTouTiao0417\report\report_HmTouTiao{}.html".format(time.strftime("%Y-%m-%d"))
#

with open(filepath, "wb") as f:
    runner = HTMLTestRunner(f, 2, "黑马头条测试报告0420", "python3.11")
    #运行套件对象
    runner.run(suite)
