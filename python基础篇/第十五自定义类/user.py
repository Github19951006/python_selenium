"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/01
@File   :user.py
"""
'''
练习 9-3
'''
class User:
	
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		
	def describe_user(self):
		# print(self.first_name)
		return f'{self.first_name}'
	
	def greet_user(self):
		print('你好！！python自动化测试')

# 实例化对象
name1 = User('小妞','韩愈')
name2 = User('老边','哲瀚')
name3 = User('水鱼','杨洋')
name = name1.describe_user()
print(name)
name_greet = name2.greet_user()
print(name_greet)