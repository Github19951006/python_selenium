"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/24
@File   :yuerwen_05_多进程.py
"""

from threading import Thread
from time import sleep

def f():
	while True:
		b = 5 * 8
		
if __name__ == '__main__':
	plist = []
	# 启动10个线程
	for i in range(100):
		p = Thread(target=f)
		p.start()
		plist.append(p)
	
	for p in plist:
		p.join()
