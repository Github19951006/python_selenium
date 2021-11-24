"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/01
@File   :car.py
"""
'''
Car 车的父类
'''
class Car:
	
	# 初始化方法
	def __init__(self,make,model,year):
		'''
		:param make: 手动还是自动波
		:param model: 模型
		:param year: 年限
		'''
		# 初始化属性  汽车的属性
		self.make = make
		self.model = model
		self.year = year
		# 给属性指定默认值
		self.odometer_reading = 0
	
	'''
	自定义方法
	返回的是字符串
	'''
	def get_descriptive_name(self):
		long_name = f'{self.year} , {self.make} , {self.model}'
		return long_name
	
	def read_odometer(self):
		'''打印一条汽车的公里数的消息'''
		return f'this is car  {self.odometer_reading} miles on it'
	
	
	def update_odometer(self,mileage):
		self.mileage = mileage
		'''
		将里程表读数设置为指定的值
		禁止将里程表读数往回调
		'''
		# 判断新的里程大于老的就把新的里程赋值给old里程
		if mileage > self.odometer_reading:
			self.odometer_reading = mileage
			return '调回去'
		else:
			return 'you can not roll back an odometer'
		 
	'''
	通过方法对属性的值进行递增
	'''
	# 增加里程数量
	def increment_odometer(self,miles):
		self.odometer_reading += miles
	
# 实例化对象
my_new_car = Car('audi','a6',2021)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())

# 修改属性值，通过实例对象.属性 =  赋值
my_new_car.odometer_reading  = 33
print(my_new_car.read_odometer())

print(my_new_car.update_odometer(140))
print(my_new_car.read_odometer())

my_new_car.increment_odometer(101)
print(my_new_car.read_odometer())

