# -*- coding:UTF-8 -*-
# 基本类定义


class Man:                                     # 定义类名
    def __init__(self, name, age, gender):     # 定义构造方法  (self) 必须有, self 可替换其他
        self.name = name                       # 构造普通字段名
        self.age = age
        self.gender = gender

    def getinfo(self):                         # 定义构造普通方法  (self) 必须有
        print "your info:\n%s\n%d\n%s" % (self.name, self.age, self.gender)
m = Man(raw_input("name: "), input("age: "), raw_input("male/female: "))  # 封装类
m.getinfo()                  # 引用类方法
