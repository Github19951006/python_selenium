"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/01
@File   :restaurant.py
"""
'''
9-1 餐馆类
'''
class Restaurant:
	
	# 初始化方法
	'''
	restaurant_name: 餐厅的名字
	cuisine_type：菜类型
	'''
	def __init__(self,restaurant_name,cuisine_type):
		# 初始化属性
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		# 就餐人数的属性
		self.number_served = 0
		
	'''
	自定义两个方法：
	description_restaurant() : 餐馆的描述
	open_restaurant():餐馆是否有营业
	'''
	def description_restaurant(self):
		return f'{self.restaurant_name} ,特殊{self.cuisine_type}'
		
	def open_restaurant(self):
		print('餐馆正在营业！')
	
	# 修改就餐人数的方法
	def set_number_served(self,numberage):
		if numberage > self.number_served:
			self.number_served = numberage
		else:
			print('不能负人数就餐')
	 
	 # 对属性值进行递归增加就餐人数
	def increment_number_served(self,number):
		self.number_served += number
	
# 实例化
restaurant = Restaurant('新北京餐馆','粤菜')
# 调用方法
print(restaurant.description_restaurant())
restaurant.open_restaurant()
print(f'就餐人数：{restaurant.number_served}')
# 修改就餐人数
restaurant.set_number_served(200)
print(f'就餐人数：{restaurant.number_served}')

# 递归计算就餐人数
restaurant.increment_number_served(30)
print(f'递归增加就餐人数：{restaurant.number_served}')



















print('==============================================================================')

'''
练习题 9-2
创建三个实例，并调用description_restaurant方法
'''
# 创建3个餐馆的实例对象，存储到列表中
list_restaurant = [ Restaurant(f'新北京餐馆{i}','粤菜') for i in range(3)]
for i in list_restaurant:
	print(i.description_restaurant())



