"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/28
@File   :yuerwen_4.py
"""
'''
获取某个月总共有多少天
'''
from calendar import monthrange
def Get_year_mon(year,mon):
	# monthrange返回的是元组
	# 返回的结果的第一个元素是指定月第一天是星期几
	# 返回的结果的第二个元素是指定月有多少天
	mr = monthrange(year,mon)
	print(f'{year}年，{mon}月的第一天是星期:{mr[0]+1}')
	print(f'{year}年，{mon}月一共{mr[1]}天')
	
# 调用函数
Get_year_mon(2021,12)