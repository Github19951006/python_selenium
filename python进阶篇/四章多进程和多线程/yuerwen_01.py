"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/23
@File   :yuerwen_01_序列化.py
"""
# 多进程和多线程
from threading import Thread
from time import sleep

print("开始 执行主进程的代码")

# 定义的一个函数
def threadTest(cas1,cas2):
	print("开始 子线程")
	print(f"子线程的参数 == {cas1}：{cas2}")
	sleep(1)
	print("结束 子线程")

# target参数 是指定新线程的 入口函数
# args 指定了 传给 入口函数threadTest 的参数
thread = Thread(target=threadTest,args=('牛','牯'))

# 调用线程执行
thread.start()

# join的作用就是等待子线程执行结束后  再执行主线程
thread.join()
print("结束 执行主进程的代码")