"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/29
@File   :test04_父类.py
"""
class BYDCar:
	# 类的基本属性
	name = '比亚迪'
	country = '中国'
	
	@staticmethod
	def ling():
		return '开灯'
	'''
	# 使用方法: 类名(参数)
	'''
	# 初始化方法
	def __init__(self,color,engineSN):
		self.color = color
		self.engineSN = engineSN
	
	'''
	使用方法：实例化名称.方法名(参数)
	'''
	# 自定义方法
	def changeColo(self,newColor):
		 self.color = newColor
		 
# 定义子类
class BYD001(BYDCar):
	price = 220000
	model = 'BYD001'
	
class BYD002(BYDCar):
	price = 320000
	model = 'BYD002'

# 实例化一个实例对象出来
byd001 = BYD001('黑色','byd0018384hfni')
byd002 = BYD002('绿色','byd0038384hfdsfd')

# print(byd001.ling())
# print(byd001.name)
# print(byd002.color)
# byd002.changeColo('白色')
# print(byd002.color)
