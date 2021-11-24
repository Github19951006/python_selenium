"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/21
@File   :yuerwen_6文件大小和修改日期.py
"""
import os
import time
# 文件大小和修改日期

# 1、获取文件大小
getSize = os.path.getsize('D:/python/01安装与运行/test.py')
print(f'文件内容的大小：{getSize}')

# 2、获取文件最后修改日期，是秒
getTime = os.path.getmtime('D:/python/01安装与运行/test.py')
print(f'获取文件最后修改日期，是秒: {getTime}')

# 可以把秒时间 转化为日期时间
print(time.ctime(getTime))  # Tue Jul 27 21:56:33 2021

# 获取当前的工作目录路径
cwd = os.getcwd()
print(f'获取当前工作目录路径：{cwd}')

