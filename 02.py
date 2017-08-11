# -*- coding:UTF-8 -*-
# 继承的演示


class Penguin:                                             # 定义企鹅类
    def __init__(self, name, ID):                          # 定义构造方法，属性(初始化)
        self.name = name                                   # 引用属性名
        self.ID = ID

    def eat(self):                                         # 定义eat方法
        print self.name, "is eating"

    def info(self):                                         # 定义info方法
        print "I'm", self.name, "my id is", self.ID
a = Penguin("jerry", 432)                                   # 调用构造方法
a.eat()                                                     # 调用eat方法
a.info()                                                    # 调用info方法
# ----------------------------------------------------------


class Mouse:                                                 # 同理，如上
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def eat(self):
        print self.name, "is eating"

    def info(self):
        print "I'm", self.name, "my id is", self.ID
a = Mouse("cherry", 492)
a.eat()
a.info()
# ----------------------------------------------------------
# ----------------------------------------------------------   # 优雅的分割线,下面为 继承


class Animal:                                         # 定义父类：动物类
    def __init__(self, name, ID):                     # 定义父类构造方法，属性(初始化)
        self.name = name
        self.ID = ID

    def eat(self):                                     # 定义父类（公共）eat方法
        print self.name, "is eating"

    def info(self):                                    # 定义父类（公共）info方法
        print "I'm", self.name, "my id is", self.ID


class Penguin(Animal):                                 # 定义子类Penguin继承父类Animal
    def __init__(self):                                # 定义子类构造方法，属性(初始化)
        Animal.__init__(self, name="jerry", ID=432)    # 子类属性继承父类属性,属性赋值


class Mouse(Animal):
    def __init__(self):
        Animal.__init__(self, name="cherry", ID=492)
x = Penguin()                                           # 以下为调用
y = Mouse()
x.eat()
y.eat()
x.info()
y.info()
