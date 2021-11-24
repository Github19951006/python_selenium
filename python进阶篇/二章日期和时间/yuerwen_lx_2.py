"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/29
@File   :yuerwen_lx_2.py
"""
'''
{:target="_blank"} 下载一个日志文件 esn.log

该文件记录了购物平台的购物记录，文件格式如下

1456190061> buy product id=vscwg9mg0rg0vt44z1aq
1456071815> buy product id=35u0c7v9jccbbooabssf
1456622256> buy product id=62amh5za0wp2u7rirz75
1456203485> buy product id=m3m6ctfjqy2ykby20gzi
1456439890> buy product id=gpjr76jn74k287fgvj8f
1456021921> buy product id=d53xy60flulobpxyk95c
其中 每行 尖括号之前为数字时间戳，表示记录该行信息的时间，也就是用户购物的时间。

请写一个程序，分析该日志文件，得出一张表，记录每一天合计的购物次数，输出格式如下：

2016-02-21 : 购物 66 次
2016-03-01 : 购物 99 次
2016-02-23 : 购物 87 次
2016-03-03 : 购物 58 次
'''
import time
dataTabe = {}
# 读取文件
with open('esn.log','r',encoding='utf8') as f :
	rlines = f.read().splitlines()
	
	for line in rlines:
		# 去除空行
		if not line.strip():
			continue
		
		# 按照‘>’,切割获取字符串秒数，强制转换为int类型
		get_second_time = int(line.split('>')[0])
		
		# 将秒数转换成日期格式
		# time.localtime(get_second_time)是格式化时间戳为本地的时间
		data_time = time.strftime('%Y-%m-%d',time.localtime(get_second_time))
		
		# 判断日期data_time是否在dataTab字典中
		if data_time in dataTabe:
			# data_time是作为values值的
			dataTabe[data_time] += 1
		else:
			dataTabe[data_time] = 1
# print(dataTabe)
# 循环遍历字典
for date,times in dataTabe.items():
	print(f'{date} : 购物 {times} 次')