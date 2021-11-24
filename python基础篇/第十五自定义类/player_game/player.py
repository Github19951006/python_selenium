"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/05
@File   :player.py
"""
'''
玩家
'''
class Player:
	
	# 初始化方法
	def __init__(self, stoneNum):
		# 灵石费
		self.stoneNum = stoneNum
		# 拥有的战士，包括弓箭兵和斧头兵的字典
		self.warriors = {}