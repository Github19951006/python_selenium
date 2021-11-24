"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/23
@File   :yuerwen_02_共享数据.py
"""

from threading import Thread
from time import sleep
print('主线程 开始！')
bank = {
	'yuer':0
}

# 定义一个函数，作为新线程的调用
def deposit(threadIdex,amount):
	# 取出字典中的values
	balance = bank['yuer']
	
	sleep(0.1)
	
	# 对值进行累加
	bank['yuer'] = balance + amount
	print(f'子线程 {threadIdex} 结束！')
	
threadList = []
for idex in range(100):
	# 创建一个线程对象
	thread  = Thread(target = deposit,
	                 args = (idex,1))
	
	# 开始执行线程对象，返回线程对象
	thread.start()
	threadList.append(thread)
	
for thread in threadList:
	thread.join()
	
print('主线程 结束！')
print(f'最后我们的账号余额为 {bank["yuer"]}')
