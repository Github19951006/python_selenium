"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/05
@File   :arrow_warror.py
"""
'''
士兵：弓箭兵
'''
# 导包
from player_game import warriors

class Arrow_warror(warriors):
	# 名称
	typeName= '弓箭兵'
	
	# 弓箭兵的雇佣价格
	price = 100
	
	# 最大生命值
	maxStrength = 100
	
	# 初始化方法
	def __init__(self,name,strength = maxStrength):
		# 优先调用父类的初始化化方法
		super(Arrow_warror, self).__init__(strength)
		
		# 子类的初始化方法
		self.name = name
		
		# 和妖怪战斗
	def kill_monster(self, monster):
		if monster == '鹰妖':
			self.strength -= 20
		elif monster == '狼妖':
			self.strength -= 80
		else:
			print('未知类型的妖怪！！！')