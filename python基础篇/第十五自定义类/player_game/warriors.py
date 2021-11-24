"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/05
@File   :warriors.py
"""
'''
兵的父类
'''
class Warriors:
	
	# 初始化生命值
	def __init__(self,strength):
		self.strength = strength
		
	# 用灵石疗伤
	def healing(self, stoneCount):
		# 如果已经到达最大生命值，灵石不起作用，浪费了
		if self.strength == self.maxStrength:
			return
		self.strength += stoneCount
		
		# 不能超过最大生命值
		if self.strength > self.maxStrength:
			self.strength = self.maxStrength