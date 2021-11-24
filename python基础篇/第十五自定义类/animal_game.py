"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/06
@File   :animal_game.py
"""
'''
用面向对象的设计编写一个python程序，实现一个文字游戏系统。

动物园里面有10个房间，房间号从1 到 10。

每个房间里面可能是体重200斤的老虎或者体重100斤的羊。 游戏开始后，系统随机在10个房间中放入老虎或者羊。

然后随机给出房间号，要求游戏者选择敲门还是喂食。

如果选择喂食： 喂老虎应该输入单词 meat，喂羊应该输入单词 grass 喂对了，体重加10斤。 喂错了，体重减少10斤

如果选择敲门： 敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。

游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。 游戏3分钟结束后，显示每个房间的动物和它们的体重。

其中3分钟结束的实现方法：先获取游戏开始时间，游戏过程中每次用户输入后，再获取时间，减去开始时间， 如果超过3分钟，游戏结束
'''
# 导入生成随机数的类
import random
import time

# 创建老虎的类
class Tiger:
	name = '老虎'
	
	# 初始化方法
	def __init__(self,weight):
		self.weight = weight

# 创建山羊的类
class Sheep:
	name = '山羊'
	
	# 初始化方法
	def __init__(self, weight):
		self.weight = weight
		
# 创建一个房间列表，存储动物
animal_rooms = []

# 游戏开始后，系统随机在10个房间中放入老虎或者羊
for i in range(3):
	result = random.randint(0,1)
	if result == 0:
		animal_rooms.append(Tiger(200))
	else:
		animal_rooms.append(Sheep(100))
for u in animal_rooms:
	print(u.name)

# 如果选择喂食： 喂老虎应该输入单词 meat，喂羊应该输入单词 grass 喂对了，体重加10斤。 喂错了，体重减少10斤
# 如果选择敲门： 敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。

times = time.time()
print(times)

while True:
	# 返回的是动物的实例，但是存储在列表中
	animals = random.choice(animal_rooms)
	animal_room = animal_rooms.index(animals)
	print(f'房间号：{animal_room+1}')
	
	time.sleep(1)
	print(f'{animals.name}')
	choose = input('请选择喂(w)，还是敲门(q)')
	# print(animal)  # [<__main__.Sheep object at 0x0000020D4FD352E0>]
	times1 = time.time()
	if times1 - times > 60*3:
		print('游戏结束，超时！！')
		break
	 # 判断 如果是喂食
	if choose == 'w':
		choose_foods = input('喂老虎应该输入 [ meat ]，喂羊应该输入 [ grass ]')
		times2 = time.time()
		if times2 - times > 60*3:
			print('游戏结束，超时！！')
			break
		
		if choose_foods == 'meat':
			if '老虎' == animals.name:
				animals.weight += 10
				print('喂食成功，给老虎增肌了~~~')
			else:
				print('判断错误了！！')
				animals.weight -= 10
		elif choose_foods == 'grass':
			if '山羊' == animals.name:
				animals.weight += 10
				print('喂食成功，给山羊增肌了~~~')
			else:
				print('判断错误了！！')
				animals.weight -= 10
		else:
			print('输入错误')
			continue
	else:
		if '老虎' == animals.name:
			print('Wow !!')
			print(f'减前体重 {animals.weight}')
			animals.weight -= 5
			print(f'减后体重 {animals.weight}')
		else:
			print('mie~~')
			print(f'减前体重 {animals.weight}')
			animals.weight -= 5
			print(f'减后体重 {animals.weight}')
			
# 循环遍历列表
for animal in animal_rooms:
	print(f'{animal.name}:{animal.weight}')


