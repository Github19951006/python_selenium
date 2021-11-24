"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/18
@File   :test02.py
"""
'''
点击这里下载文件 解压后得到文件 0016_1.txt

这个是一个数据文件，格式如下

薛蟠     4560 42
薛蝌     4460 25
薛宝钗   5776 43
这里面有3列数据，分别 保存了 游戏系统的用户名， 用户积分 ， 年龄

现在要求大家写一个程序，打印出该数据文件中积分最多的用户姓名。

大家使用教程里面推荐的 Pycharm 集成开发环境，创建一个项目文件，并写相应的代码。
'''
with open('0016_1.txt',encoding='utf8') as f:
	# 按行读取数据，splitlines()是按照换行符切割
     infoLine = f.read().splitlines()
# 存储名字
name = []
# 迭代器一个最高的用户积分
maxCoin = 0

for info in infoLine:
	# 去除字符串的左右空格
	infoStrip = info.strip()
	
	# 去除空行
	if infoStrip == '':
		continue
		
	# 按照空格切割，返回一个列表
	infoStripList = infoStrip.split(' ')
	
	# 获取名字
	name1 = infoStripList[0]
	# 获取积分
	Coin = int(infoStripList[-2])
	
	# 比较积分大小 等于 记录积分最大的
	if Coin > maxCoin:
		name = [name1]
		maxCoin = Coin
	elif Coin == maxCoin:
		name.append(name1)
print(name)
		