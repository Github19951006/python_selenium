"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/26
@File   :yuerwen_07_补充学习.py
"""
from threading import Thread
from time import sleep

print('主线程 开始！')

# 定义一个类 继承Thread类
class MyThread(Thread):
	# 重写父类的方法 取代父类run方法
	def run(self):
		print('子线程 开始')
		print(f'线程函数参数是：{self._args}  ')
		sleep(2)
		print('子线程 结束')
	
# 创建MyThread类的实例对象
# 因为 重定义了run 方法，所以无需 指定新线程的入口函数
thread = MyThread(args=('参数1','参数2'))
thread.start()

thread.join()

print('主线程 结束')
	