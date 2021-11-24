"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/01
@File   :dog.py
"""
'''
创建一个狗类
'''
class Dog:
	
	# 初始化方法
	'''
	name :名字
	age：年龄
	'''
	def __init__(self,name,age):
		# 初始化属性
		self.name = name
		self.age = age
		
	# 自定义方法
	'''
	sit：小狗坐的方法
	'''
	def sit(self):
		print(f'{self.name.title()} is now sitting')
		
	'''
	roll_over:小狗打滚
	'''
	def roll_over(self):
		print(f'{self.name.title()} roll over')
	
	# def __repr__(self):
	# 	return f'{self.name} roll over'
	
# 实例化出一只具体的狗
habaDog = Dog('文旭',55)
print(f'这小狗的名字：{habaDog.name}，今年{habaDog.age}岁')
habaDog.sit()
habaDog.roll_over()
