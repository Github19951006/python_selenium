"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/19
@File   :yuerwen_game.py
"""
# 鹰妖
# 属性：类型名 typename
class Eagle:
	typeName = '鹰妖'

# 狼妖
# 属性：类型名 typename
class Wolf:
	typeName = '狼妖'

# 兵的父类
class Warrior:
	
	def __init__(self,name):
		'''
		实例的初始函数
		:param name:实例的兵的名字
		'''
		# 实例属性  生命值
		self.strength = self.maxStrength
		self.name = name
			
	def fight_With_Monster(self,monster):
		'''
		士兵和妖怪战斗的方法
		:param monster:  妖怪的对象
		:return:
		'''
		if monster.typeName in self.fightRule:
			self.strength -= self.fightRule[monster.typeName]
		else:
			print('妖怪类型不支持')
			
	def hael(self,stoneCount):
		'''
		给士兵疗养的方法
		:param stoneCount: 疗养数量
		:return:
		'''
		self.strength += stoneCount
		if self.strength > self.maxStrength:
			self.strength = self.maxStrength
			
# 弓箭兵
# 属性：类型名 typename
# 	雇佣价： 100 灵石
#   最大生命值： 10
#   名字  name
# 行为：和妖怪战斗 fight_With_Monster
class Archer(Warrior):
	# 类属性
	typeName = '弓箭兵'
	price = 100
	maxStrength = 100
	fightRule = {
		'鹰妖':20,
		'狼妖':80
	}
	
# 斧头兵
# 属性：类型名 typename
# 	雇佣价： 120 灵石
#     最大生命值： 120
# 方法：和妖怪战斗 fight_With_Monster
class Axeman(Warrior):
	# 类属性
	typeName = '斧头兵'
	price = 120
	maxStrength = 120
	fightRule = {
		'鹰妖': 20,
		'狼妖': 80
	}

# 玩家
# 属性：灵石数量
class Player:
	def __init__(self,stoneNumber):
		'''
		玩家的实例方法
		:param stoneNumber: 玩家的灵石
		'''
		self.stoneNumber = stoneNumber
		self.warriors = {}
	
	# 雇佣战士
	def hireWarrior(self):
		menu = '''
		请选择雇佣操作
		1 - 雇佣弓箭兵
		2 - 雇佣斧头兵
		3 - 退出
		：'''
		
		while True:
			choice = input(menu)
			if choice not in ['1','2','3']:
				print('输入错误！！')
				continue

# 森林
class Forest:
	def __init__(self,monster):
		'''
		森林实例方法
		:param monster: 妖怪实例
		'''
		self.monster = monster

# 创建实例化玩家
player = Player(1000)


