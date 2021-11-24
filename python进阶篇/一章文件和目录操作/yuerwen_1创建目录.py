"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/19
@File   :yuerwen_1创建目录.py
"""
import os
# mkdir: 方法在创建多层目录时如果前面的目录不存在的话就会创建失败
# makdirs: 可以递归创建文件目录

# 单级创建文件目录
# os.mkdir('test/yuer/wen')  报错：os.mkdir('test/yuer/wen')

try:
	os.mkdir('test1/yuer/wen')
except Exception as e:
	print('创建文件失败！！')

# 可以递归创建文件目录
os.makedirs('test/yuer/wen',exist_ok=True)