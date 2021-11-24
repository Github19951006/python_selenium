"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/29
@File   :python05_子类.py
"""
from test04_父类 import BYDCar
class Byd(BYDCar):
	price = 9908
	
	def __init__(self, color, engineSN, aabb):
		# 要特别注意的是，子类的初始化方法里面，需要调用父类的初始化方法_init_
		BYDCar.__init__(self, color, engineSN)
		self.abb = aabb # 车的重量
		self.oilweight = 0  # 油的重量
	
	# 自定义类
	def filloil(self,oilAdded):
		self.oilweight += oilAdded
		self.abb += oilAdded

# 实例化对象

car1 = Byd('黑色','090987uhuh',10)
print(car1) # 返回的是对象的地址：<__main__.Byd object at 0x0000022D3ED531F0>
print(car1.name)
print(car1.abb)
car1.filloil(50)
print(car1.oilweight)
print(car1.abb)

			