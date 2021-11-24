"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/17
@File   :yuerwen_test_01.py
"""

import time

# 定义一个装饰器函数
def sayLocal(func):
    def wrapper():
        curTime = func()
        return f'当地时间： {curTime}'
    return wrapper

def getXXXTime():
    return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())

# 没有装饰的函数
print(getXXXTime())

# 装饰 getXXXTime
getXXXTime_decorator = sayLocal(getXXXTime)
print(getXXXTime_decorator())