"""
重写父类中的方法，覆盖
"""


#定义一个狗类
class Dog:
    def bark(self):
        print("汪汪叫")


#定义一个哮天犬类 ，继承狗类
class XiaoTian(Dog):
    #重写bark方法，改为 嗷嗷嗷叫
    def bark(self):
        print("嗷嗷嗷叫")
    def fly(self):
        print("我会飞")


xt=XiaoTian()
xt.bark()  # 调用父类的父类Animal的方法
