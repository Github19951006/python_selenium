"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/21
@File   :test_lx2.py
"""
from pprint import pprint
'''
学习心得：
1、根据什么就去查什么！
	2、根据的东西就作为 key
	3、要查的东西就作为 values
'''
members = {
    1 :{'name':'白月黑羽', 'level':3, 'coins':300},
    2 :{'name':'短笛魔王', 'level':5, 'coins':330},
    3 :{'name':'紫气一元', 'level':6, 'coins':340},
    4 :{'name':'拜月主',   'level':3, 'coins':32200},
    5 :{'name':'诸法空',   'level':4, 'coins':330},
    6 :{'name':'暗光城主', 'level':3, 'coins':320},
    7 :{'name':'心魔尊',   'level':3, 'coins':2300},
    8 :{'name':'日月童子', 'level':8, 'coins':3450},
    9 :{'name':'不死尸王', 'level':3, 'coins':324},
    10:{'name':'天池剑尊', 'level':9, 'coins':13100},
}

# 因为要根据用户名查找用户信息，需要改变字典格式
# 以用户名为key，创建一个字典
nameInfo = {}
for k,v in members.items():
	name = v['name']
	# 将ID 添加到values值的字典中
	v['id'] = k
	# 将values的name作为key，添加到新的列表中
	nameInfo[name] = v
	
# 1 看用户账号信息
def checkAccount():
	nameS = input('输入账号名:')
	# 判断
	if nameS not in nameInfo:
		print(f'对不起，账号：{nameS} 不存在.')
		# return之后的代码是不执行的
		return
	
	# 通过key去找values的值  info:就是我们的values值
	info = nameInfo[nameS] # <class 'dict'>
	print(f'账号: {nameS} , ID : {info["id"]} , 等级：{info["level"]} , 金币：{info["coins"]} ')

# 2 添加用户
def addAccount():
	while True:
		name = input('请输入添加用户的账号:')
		if name in nameInfo:
			print('对不起，该账号已经存在')
		else:
			break
	
	while True:
		level = input('请输入该用户的等级:')
		# 如果不是数字 ， 则输入格式错误
		if not level.isdigit():
			print('对不起，等级必须为一个数字')
		else:
			level = int(level)  # 转化为整数
			break
			
	while True:
		coins = input('请输入该用户的金币数量:')
		# 如果不是数字 ， 则输入格式错误
		if not coins.isdigit():
			print('对不起，金币数 必须为一个数字')
		else:
			coins = int(coins)  # 转化为整数
			break
	
	# 要产生一个不存在的ID号， 这里我们取 当前最大的ID号+ 1
	newId = max(members.keys()) + 1
	# 注意： 两个字典里面都要添加
	members[newId] = {'name': name, 'level': level, 'coins': coins}
	nameInfo[name] = {'name': name, 'level': level, 'coins': coins, 'id': newId}
	print(members)
	print(nameInfo)
	
# 3 删除用户
def delAccount():
	nameS = input('输入账号名:')
	# 判断账号名是否存在字典中
	if nameS not in nameInfo:
		print(f'对不起，账号：{nameS} 不存在.')
		return
	
	# 注意： 两个字典里面都要删除
	theID = nameInfo[nameS]['id']
	nameInfo.pop(nameS)
	members.pop(theID)

# 4 列出所有用户信息
def showTables():
	print('\n现在nameInfo的表内容是：\n')
	pprint(nameInfo)
	print('\n现在members的表内容是：\n')
	pprint(members)

men = '''
请选择操作选项：
   1 查看用户账号信息
   2 添加用户
   3 删除用户
   4 列出所有用户信息
   0 退出
'''

while True:
	choice = input(men)

	# 选择查看查看用户账号
	if choice == '1':
		checkAccount()
	elif choice == '2':
		addAccount()
	elif choice == '3':
		delAccount()
	elif choice == '4':
		showTables()
	elif choice == '0':
		break
