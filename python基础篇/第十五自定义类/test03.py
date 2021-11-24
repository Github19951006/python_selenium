"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/28
@File   :test03.py
"""
class Car:
    brand = '奔驰'
    name = 'Car'

    def __init__(self):
        # 可以通过实例访问到类属性
        print(self.brand)

        # 定义实例属性和类属性重名
        self.name = 'benz car'

c1 = Car()
# print(c1)

print(f'通过实例名访问name：{c1.name}')
print(f'通过类名  访问name：{Car.name}')