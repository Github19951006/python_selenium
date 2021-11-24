"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/24
@File   :yuerwen_04_daemon线程.py
"""
from threading import Thread,Lock
from time import sleep


# 定义锁对象
threadLock = Lock()
print('主线程 开始')

# 定义函数
def threadFun():
	# 在共享数据前，申请锁
	# threadLock.acquire()
	sleep(2)
	print('子线程 开始')
	
	# 释放锁对象
	# threadLock.release()

# 设置新线程为daemon线程  守护线程
# 创建线程对象
thread = Thread(target= threadFun,daemon=True )

thread.start()
print('主线程 结束')