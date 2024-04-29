"""
    目标：完成数据库相关工具类封装
    分析：
        1,主要方法
            def get_sql_one(sql)：查询一条结果
            def get_sql_all(sql)：查询所有结果集
            def update_sql(sql):新增、修改、删除操作
        2,辅助方法
            1.获取连接对象
            2.获取游标对象
            3.关闭游标对象方法
            4.关闭连接对象方法
"""

#导包pymysql
import pymysql


#新建工具类：数据库
class ReadDB:
    conn = None

    #获取连接对象方法封装
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect(host="192.168.124.128", user="root", password="123456", database="litemall",
                                        port=3306, charset="utf8")
        #返回连接对象
        return self.conn

    #获取游标对象方法封装
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭游标对象方法封装
    def close_cursor(self, cursor):
        #如果游标对象cursor不为空才进行关闭
        if cursor:
            cursor.close()

    #关闭连接对象封装
    def close_conn(self):
        #如果连接对象不为空才进行关闭
        if self.conn:
            self.conn.close()
            #注意：连接对象关闭后，对象还存在内存中，需要手工设置为None
            self.conn = None

    #主要执行方法 -> 在外界调用此方法就可以完成数据相应的操作
    #1、获取sql的一条执行结果
    def get_sql_one(self, sql):
        #定义游标对象及数据变量
        cursor = None
        data = None
        # 捕获异常:sql执行报错的捕获
        try:
            #获取游标对象:在获取游标对象方法中已经调用获取连接对象方法
            cursor = self.get_cursor()
            #调用执行方法
            cursor.execute(sql)
            #获取执行结果
            data = cursor.fetchone()
        except Exception as e:
            print("get_sql_one error:", e)
        finally:
            #关闭游标对象
            self.close_cursor(cursor)
            #关闭连接对象
            self.close_conn()
            #返回执行结果
            return data

    #2、获取sql的所有执行结果
    def get_sql_all(self, sql):
        #定义游标对象及数据变量:变量初始化
        cursor = None
        data = None
        # 捕获异常:sql执行报错的捕获
        try:
            #获取游标对象:在获取游标对象方法中已经调用获取连接对象方法
            cursor = self.get_cursor()
            #调用执行方法
            cursor.execute(sql)
            #获取执行结果:fetchall获取所有结果
            data = cursor.fetchall()
        except Exception as e:
            print("get_sql_all error:", e)
        finally:
            #关闭游标对象
            self.close_cursor(cursor)
            #关闭连接对象
            self.close_conn()
            #返回执行结果
            return data

    #3、新增、修改、删除sql的数据库操作
    def update_sql(self, sql):
        #定义游标对象及数据变量
        cursor = None
        # 捕获异常:sql执行报错的捕获
        try:
            #获取游标对象:在获取游标对象方法中已经调用获取连接对象方法
            cursor = self.get_cursor()
            #调用执行方法
            cursor.execute(sql)
            #提交事务
            self.conn.commit()
        except Exception as e:
            #事务回滚:sql执行异常则需要回滚sql的操作
            self.conn.rollback()
            print("update_sql error:", e)
        finally:
            #关闭游标对象
            self.close_cursor(cursor)
            #关闭连接对象
            self.close_conn()
