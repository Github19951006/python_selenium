"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/28
@File   :yuerwen_lx_1.py
"""
'''
请写一个程序，打印出从当天开始，在一年内，所有的周日对应的日期
'''
from datetime import datetime,timedelta

# 获取日期 2021-09-28
now_day = datetime.now().date()  # 2021-09-28

# 循环365天
for i in range(365):
		# 现在的日期 + n day, 0:00:00
		that_day = now_day + timedelta(days=i)
		'''
		1 day, 0:00:00
		2 days, 0:00:00
		'''
		# print(timedelta(days=i))
		# 2021-09-29
		# print(that_day)
		# 判断是不是周日，0：周一，1:周二。。。
		if that_day.weekday() == 6:
			print(that_day.strftime('%Y-%m-%d'))
			
# mktime()方法语法：
# time.mktime(t)  参数：t -- 结构化的时间或者完整的9位元组元素。
import time
print(time.mktime((2009, 2, 17, 17, 3, 38, 1, 48, 0)))


