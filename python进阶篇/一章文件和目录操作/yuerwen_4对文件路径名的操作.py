"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/21
@File   :yuerwen_对文件路径名的操作.py
"""
# 对文件路径名的操作
import os
path = '/Users/beazley/Data/data.csv'

# 获取路径中的文件名部分
print(os.path.basename(path))

# 获取路径中的目录部分
print(os.path.dirname(path))


path1 = 'home'
path2 = 'develop'
path3 = 'code'
# 文件路径的拼接
print(os.path.join(path1,path2,os.path.basename(path)))  # home\develop\data.csv

# 补充学习
path1 = '/home'
path2 = 'develop'
path3 = 'code'
print(os.path.join(path1,path2,os.path.basename(path))) # /home\develop\data.csv

path1 = 'home'
path2 = '/develop'
path3 = 'code'
print(os.path.join(path1,path2,os.path.basename(path)))  # /develop\data.csv


