"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/31
@File   :words_game.py
"""
from random import randint
import time,sys


# /////////////////////////////////////////  兵的父类  /////////////////////////////////////////////////////

# 兵
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

# ////////////////////////////////////////////  弓箭兵  //////////////////////////////////////////////////

# 弓箭兵
class Arrow_warror(Warriors):
	# 名称
	typeName = '弓箭兵'
	
	# 弓箭兵的雇佣价格
	price = 100
	
	# 最大生命值
	maxStrength = 100
	
	# 初始化方法 生命值，名字
	def __init__(self,name,strength = maxStrength):
		# 先调用父类的初始化方法
		super().__init__(strength)
		self.name = name
	
	# 和妖怪战斗
	def kill_monster(self,monster):
		if monster == '鹰妖':
			self.strength -= 20
		elif monster == '狼妖':
			self.strength -= 80
		else:
			print('未知类型的妖怪！！！')


# //////////////////////////////////////////  斧头兵  ////////////////////////////////////////////////////

# 斧头兵
class Axe_warror(Warriors):
	# 名称
	typeName = '斧头兵'
	
	# 弓箭兵的雇佣价格
	price = 120
	
	# 最大生命值
	maxStrength = 120
	
	# 初始化方法 生命值，名字
	def __init__(self, name, strength=maxStrength):
		# 先调用父类的初始化方法
		super().__init__(strength)
		self.name = name
	
	# 和妖怪战斗
	def kill_monster(self, monster):
		if monster == '鹰妖':
			self.strength -= 80
		elif monster == '狼妖':
			self.strength -= 20
		else:
			print('未知类型的妖怪！！！')



# /////////////////////////////////////////  兵的父类  /////////////////////////////////////////////////////
# 玩家
class Player:
	# 初始化方法
	def __init__(self,stoneNum):
		# 灵石费
		self.stoneNum = stoneNum
		# 拥有的战士，包括弓箭兵和斧头兵
		self.warriors = {}
	
# /////////////////////////////////////////  鹰妖  /////////////////////////////////////////////////////
# 鹰妖
class Eagle():
	typeName = '鹰妖'

# //////////////////////////////////////////  狼妖  ////////////////////////////////////////////////////

# 狼妖
class Wolf():
	typeName = '狼妖'

# //////////////////////////////////////////  森林  ////////////////////////////////////////////////////
# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster
	    
player = Player(1000)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
	# random.randint(a, b)  其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
    typeName = randint(0,1)
    if typeName == 0:
	    # 鹰妖
        forestList.append( Forest(Eagle()) )
    else:
	    # 狼妖
        forestList.append( Forest(Wolf()) )

    notification += f'第{i+1}座森林里面是 {forestList[i].monster.typeName} '
	
print('''
***************************************
****           游戏开始             ****
***************************************

''')

time.sleep(3)

'''
方法：生成雇佣兵，给他起一个名字。
	 对象作为values，名字作为key，存储到拥有的战士的字典中
	 玩家的石费stoneNum减数
'''
def hirworrior(arrow_num, axe_num, player):
	for i in range(1, arrow_num + 1):
		arrow_name = f'弓箭兵{i}'
		# 把弓箭兵的对象作为values，名字作为key，存储到拥有的战士的字典中
		player.warriors[arrow_name] = Arrow_warror(arrow_name)
		player.stoneNum -= 100
	
	for j in range(1, axe_num + 1):
		axe_name = f'斧头兵{j}'
		player.warriors[axe_name] = Axe_warror(axe_name)
		player.stoneNum -= 120
	print('购买成功！！')

# 玩家雇佣兵
while True:
	arrow_num = int(input('计划购买-|弓箭兵|-的数量：'))
	axe_num = int(input('计划购买-|斧头兵|-的数量：'))
	arrow_num, axe_num = arrow_num, axe_num
	if player.stoneNum - (100 * arrow_num + 120 * axe_num) < 0:
		print(f'对不起，您的灵石不够购买士兵，还少{(100 * arrow_num + 120 * axe_num) - player.stoneNum}钱，请重新输入：')
		continue
	else:
		# 调用生成士兵，给士兵起名字
		hirworrior(arrow_num, axe_num, player)
		break

# 显示 妖怪信息
print(notification)

# 通过数
pass_forest = 0
for round in range(forest_num):
	# 如果没有士兵可以，就退出
	if not player.warriors:
		break
	
	while True:
		
		w_name = input(f'当前为第{round + 1}座森林，请输入战士名字{player.warriors.keys()}:')
		# 通过key获取values的对象
		w = player.warriors[w_name]
		# 调用士兵战斗的方法
		w.kill_monster(forestList[round].monster.typeName)
		print(f'{forestList[round].monster.typeName}战后剩余血量: {w.strength}')
	
		# 判断
		if w.strength > 0:
			print(f'第{round + 1}通过')
			pass_forest += 1
			if player.stoneNum > 0:
				stonecount = input('请问是否给战士补充灵石？输入补充的灵石个数，不补充输入0：')
				if stonecount.isdigit() and int(stonecount) < player.stoneNum:
					w.healing(int(stonecount))
					player.stoneNum -= int(stonecount)
				else:
					print('输入灵石个数超范围或格式错误')
			else:
				print('灵石不足，无法给士兵补给！')
			break
		elif w.strength == 0:
			print(f'第{round + 1}通过，但是战士已死')
			del player.warriors[w_name]
			# print(player.warriors)
			break
		else:
			del player.warriors[w_name]
			continue
			
			
if pass_forest == 7 and player.stoneNum >= 0:
	print('通过！')
	print(f'剩余的灵石{player.stoneNum}')
else:
	print('失败！')
	print(f'剩余的灵石{player.stoneNum}')