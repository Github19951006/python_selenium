"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/21
@File   :test_lx.py
"""
'''
要求大家写一个程序，计算出同一姓氏的人的积分总和。
'''
with open('0016_1.txt',encoding='utf8') as f:
	# 按行读取数据
	infoList = f.read().splitlines()
# 创建字典
coinTable = {}

for info in infoList:
	# 去除左右空格
	info = info.strip()
	# 去除空行
	if not info:
		continue
	# 按照空格符切割
	infoStrip = info.split(' ')  # 返回一个列表
	
	name = infoStrip[0] # 获取名字
	coin = int(infoStrip[-2]) # 获取积分
	
	# 判断  如果名字的第一个字（姓）不在字典中就添加
	if name[0] not in coinTable:
		coinTable[name[0]] = coin
	else:
		coinTable[name[0]] += coin
# 遍历字典
for nameKey,coinValues in coinTable.items():
	print(f'{nameKey} : {coinValues}')

	