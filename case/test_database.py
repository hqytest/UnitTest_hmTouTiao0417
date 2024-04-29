"""
目标：在unittest框架中使用数据库工具类
"""
# 导包
import unittest

from tools.read_database import ReadDB


# 新建测试类：操作数据库
class TestDB(unittest.TestCase):
    # 新建测试方法：操作数据库获取一条执行结果
    def test_get_sql_one(self):
        # 定义sql语句
        sql = "select t.is_on_sale  from litemall_goods t WHERE t.id =10000 "
        # 调用get_sql_one方法
        data = ReadDB().get_sql_one(sql)
        # 调试：打印sql执行结果
        print("get_sql_one执行结果：", data)
        # 断言执行结果
        self.assertEqual(1, data[0])

    # 新建测试方法：操作数据库获取所有执行结果
    def test_get_sql_all(self):
        # 定义sql语句
        sql = "select t.is_on_sale  from litemall_goods t  "
        # 调用get_sql_all方法
        data = ReadDB().get_sql_all(sql)
        # 调试：打印sql执行结果
        print("get_sql_all执行结果：", data)
        # 断言执行结果:有很多执行结果，通过下标索引任意选择一条数据断言
        self.assertEqual(1, data[0][0])

    # 新建测试方法：操作数据库新增数据
    def test_insert_sql(self):
        # 定义sql语句
        #插入数据的sql
        sql_insert = "INSERT INTO litemall_goods(id, goods_sn, name, category_id, brand_id, gallery, keywords, brief, "\
                     "is_on_sale, sort_order, pic_url, share_url, is_new, is_hot, unit, counter_price, retail_price, " \
                     "detail, add_time, update_time, deleted) VALUES (20000, '10000', '母亲节礼物-舒适安睡组合han0406_10000'," \
                     " 1008008, 1001020, '[\"http://yanxuan.nosdn.127.net/355efbcc32981aa3b7869ca07ee47dac.jpg\", " \
                     "\"http://yanxuan.nosdn.127.net/43e283df216881037b70d8b34f8846d3.jpg\"," \
                     " \"http://yanxuan.nosdn.127.net/12e41d7e5dabaf9150a8bb45c41cf422.jpg\"," \
                     " \"http://yanxuan.nosdn.127.net/5c1d28e86ccb89980e6054a49571cdec.jpg\"]', '', '安心舒适是最好的礼物'," \
                     " 1, 1, 'http://yanxuan.nosdn.127.net/1f67b1970ee20fd572b7202da0ff705d.png', '', 1, 0, '件', " \
                     "2618.00, 2598.00, '', '2018-02-01 00:00:00', '2018-02-01 00:00:00', 0)"

        # 调用update_sql方法,此方法没有返回数据
        ReadDB().update_sql(sql_insert)

        # 查询插入数据的id值
        sql_serach = "select t.id  from litemall_goods t WHERE t.id =20000 "
        # 调用get_sql_one查询方法
        data = ReadDB().get_sql_one(sql_serach)
        # 调试：打印sql执行结果
        print("insert_sql执行结果：", data)
        # 断言执行结果:
        self.assertEqual(20000, data[0])

    # 新建测试方法：操作数据库修改数据
    def test_update_sql(self):
        # 定义sql语句
        # 修改数据的sql
        sql_update = '''update litemall_goods set name="母亲节礼物test" WHERE id =20000'''
        # # 删除数据的sql
        # sql_delete = ""
        # 调用update_sql方法,此方法没有返回数据
        ReadDB().update_sql(sql_update)
        # 查询插入数据的id值
        sql_serach = "select t.name  from litemall_goods t WHERE t.id =20000 "
        # 调用get_sql_one查询方法
        data = ReadDB().get_sql_one(sql_serach)
        # 调试：打印sql执行结果
        print("update_sql执行结果：", data)
        # 断言执行结果:
        self.assertEqual("母亲节礼物test", data[0])

    # 新建测试方法：操作数据库删除数据
    def test_delete_sql(self):
        # 定义sql语句
        # # 删除数据的sql
        sql_delete = "delete  from litemall_goods WHERE id =20000"
        # 调用update_sql方法,此方法没有返回数据
        ReadDB().update_sql(sql_delete)
        # 查询插入数据的id值
        sql_serach = "select t.*  from litemall_goods t WHERE t.id =20000 "
        # 调用get_sql_one查询方法
        data = ReadDB().get_sql_one(sql_serach)
        # 调试：打印sql执行结果
        print("delete_sql执行结果：", data)
        # 断言执行结果:
        self.assertEqual(None, data)


if __name__ == '__main__':
    unittest.main()
