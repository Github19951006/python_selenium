"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/10
@File   :yuerwen_test01.py
"""

import traceback
'''
try:
	number = int(input('请输入数字：'))
	ret = 100/number
	print(ret)
except ZeroDivisionError:
	print('您输入的数字是0，被除数是不可以为0的')
'''

while True:
	try:
		miles  = input('请输入公里数：')
		km = int(miles)*1988.0987
		print(f'公里数是 ：{km}')
	except Exception as e:
		print(traceback.format_exc())
