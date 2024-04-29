"""
目标：自动化测试中操作项目数据库
案例：
    判断轻商城系统中id为10000的商品是否上架，
    1-上架，0-未上架
"""
# 导包pymysql
import pymysql

# 获取连接对象
conn = pymysql.connect(host="192.168.124.128", port=3306, database="litemall", user="root", password="123456",
                       charset="utf8")
# 获取游标对象
cursor = conn.cursor()
# 执行方法sql
sql = "select t.is_on_sale  from litemall_goods t WHERE t.id =10000 "
cursor.execute(sql)
# 获取执行结果并进行断言
s = cursor.fetchone()
print("执行结果为：", s)
#执行结果为一个元祖(1,)，通过下标获取元素
# assert 1 == s[0]
# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()
