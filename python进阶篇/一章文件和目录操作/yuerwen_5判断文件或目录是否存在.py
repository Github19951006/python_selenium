"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/21
@File   :yuerwen_5判断文件或目录是否存在.py
"""
import os
path = '/Users/beazley/Data/data.csv'

# 判断文件、目录是否存在
print(os.path.exists('D:/python/01安装与运行'))  # True
print(os.path.exists('D:/python/01安装与运行/test.py'))

# 判断指定路径是否是文件
print(f'''判断指定路径是否是文件: {os.path.isfile('D:/python/01安装与运行/test.py')}''')

# 判断指定路径是否为目录
print(f'''判断指定路径是否为目录: {os.path.isfile('D:/python/01安装与运行')}''')