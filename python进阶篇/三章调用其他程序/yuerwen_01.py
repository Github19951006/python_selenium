"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/30
@File   :yuerwen_01_序列化.py
"""
# import os
# cmd = r'D:\tools\wget http://cdn1.python3.vip/files/py/source.zip'
# os.system(cmd)
# print('打印结束！')

# os.system 函数调用外部程序的时候， 必须要等被调用程序执行结束， 才会接着往下执行代码。 否则就会一直等待。
import os
# get_ret = input('输入source:')
# fr 的意思 f是格式化 r是解析路径
cmd = fr'D:\tools\wget http://cdn1.python3.vip/files/py/source.zip'
os.system(cmd)
print('打印结束！')

