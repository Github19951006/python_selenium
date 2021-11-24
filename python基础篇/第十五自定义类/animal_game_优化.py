"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/08
@File   :animal_game_优化.py
"""
from random import randint
import time
# 老虎类
class Tiger:
	# 类的静态属性
	class_name = '老虎'
	
	# 自定义方法
	def __init__(self,weigth = 200):
		self.weight = weigth
		
	# 敲门的方法
	def rora(self):
		print('wow!!')
		self.weight -= 5
	
	# 喂食物方法
	def food(self,foods):
		if foods == 'meat':
			self.weight += 10
			print('喂食成功，给老虎增肌了~~~')
		else:
			print('判断错误，喂食失败，给老虎减肌了~~~')
			self.weight -= 10


# 山羊类
class Sheep:
	# 类的静态属性
	class_name = '山羊'
	
	# 自定义方法
	def __init__(self, weigth=100):
		self.weight = weigth
	
	# 敲门的方法
	def rora(self):
		print('mie!!')
		self.weight -= 5
	
	# 喂食物方法
	def food(self, foods):
		if foods == 'grass':
			self.weight += 10
			print('喂食成功，给山羊增肌了~~~')
		else:
			print('判断错误，喂食失败，给山羊减肌了~~~')
			self.weight -= 10
			
# rooms 房间的方法
class Rooms:
	'''
	number:房间号
	animal:具体的动物
	'''
    # 自定义方法
	def __init__(self,number,animal):
		self.number = number
		self.animal = animal

rooms_list = []

# 随机产生10个房间，每个房间随机存储动物
for num in range(10):
	if randint(0,1):
		anim = Tiger(200)
	else:
		anim = Sheep(100)

	# 实例化房间
	room = Rooms(num,anim)
	rooms_list.append(room)
 
# 统计开始时间
start_time = time.time()
while True:
	# 统计结束时间
	end_time = time.time()
	
	if end_time - start_time > 3:
		print('游戏结束------，超时了')
		for index,room in enumerate(rooms_list):
			print(f'{index + 1}==》{room.animal.class_name}:{room.animal.weight}')
			
		break
	
	room_number = randint(1,10)
	# 通过下标获取对象
	# 表示下标：room_number -1
	animal_oo =rooms_list[room_number -1]
	choose = input(f'欢迎来到{room_number}房间，请选择喂(w)，还是敲门(q)')
	if choose == 'q':
		animal_oo.animal.rora()
	
	choose_foods = input('喂老虎应该输入 [ meat ]，喂羊应该输入 [ grass ]')
	animal_oo.animal.food(choose_foods.strip())
		