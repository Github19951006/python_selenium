"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/24
@File   :yuerwen_06_多进程.py
"""
# 导入多进程库 Process
from multiprocessing import Process
from time import sleep

def f():
	while True:
		# sleep(0.1)
		print('无限不循环')
	
if __name__ == '__main__':
	plist = []
	for i in range(2):
		p = Process(target=f)
		p.start()
		plist.append(p)
		
		for p in plist:
			p.join()
	
