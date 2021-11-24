"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/05
@File   :axe_warror.py
"""
'''
士兵：斧头兵
'''
from player_game import warriors


class Axe_warror(warriors):
	# 名称
	typeName = '斧头兵'
	
	# 弓箭兵的雇佣价格
	price = 120
	
	# 最大生命值
	maxStrength = 120
	
	# 初始化方法
	def __init__(self, name, strength=maxStrength):
		# 优先调用父类的初始化化方法
		super(Axe_warror, self).__init__(strength)
		
		# 子类的初始化方法
		self.name = name
	
	# 和妖怪战斗
	def kill_monster(self, monster):
		if monster == '鹰妖':
			self.strength -= 80
		elif monster == '狼妖':
			self.strength -= 20
		else:
			print('未知类型的妖怪！！！')