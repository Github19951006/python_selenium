"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/28
@File   :test02.py
"""
class Dog(object):
    food='牛肉'
    name='大黄狗'
    def __init__(self, name):
        self.name = name
    @staticmethod
    def eat(self):
        print('%s eat %s' %(self.name,Dog.food))
d = Dog("拉布拉多")
d.eat()
Dog.eat()
