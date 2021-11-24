"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/23
@File   :test_附加1.py
"""
'''
1571713540.9697|API list_order >0.03s|sales_22
1571713569.1041|API list_order >0.05s|sales_3
1571713599.2024|API list_order >0.08s|sales_3
1571713569.1578|API list_order >0.05s|sales_302
1571713571.7784|API list_order >0.1s|sales_29
1571713657.2568|API list_order >0.5s|sales_576
1571713657.4442|API list_order >1s|sales_845
该日志文件记录了 服务端对 各个请求处理 耗费的时间信息。

每行以 | 为分隔符， 记录了3个信息：

时间戳
什么请求处理时间大于多少秒
请求对应的用户
要求你写一个程序，统计

请求处理时间 在 各个时间段的数量，结果格式如下

API list_order >0.03s : 548个
API list_order >0.05s : 274个
API list_order >0.1s : 306个
API list_order >0.08s : 105个
API list_order >0.5s : 157个
API list_order >1s : 2062个
响应超时 : 403个
并且把结果写入文件

注意：你不能假设日志里面的响应时间就是这些内容 ，也可能有 其它的延迟时间，比如

API list_order >1.5s : 2068个
API list_order >1.8s : 2068个
等等
'''
'''
解题思想：
1、读取文件 open()
2、按行读取，返回一个列表
'''
with open('2019-10-22_11.05.40.log',encoding='utf8') as f :
	# 2、按行读取，返回一个列表
	infoList = f.read().splitlines()

# 创建一个空字典
list_orderDic = {}
# 计时器
sum = 1

	# 循环获取列表元素
for info in infoList:
	# 去除字符串左右空格
	info = info.strip()
	
	# 去除空行
	if not info:
		continue
	
	# 切割，将字符串 转换成 列表
	infoSplist = info.split('|')

	
	# 如果不在字典中就加入
	if infoSplist[1] not in list_orderDic:
		# if infoSplist[1] == '110':
		# 	list_orderDic[infoSplist[2]] = sum
		# 	sum += sum
			
		list_orderDic[infoSplist[1]] = sum
		sum += sum
	else:
		list_orderDic[infoSplist[1]] += sum
		# list_orderDic[infoSplist[2]] += sum
		
		
	

for k,v in 	list_orderDic.items():
	print(f'{k} : {v}')
# print(list_orderDic)