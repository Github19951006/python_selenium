"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/19
@File   :yuerwen_2删除目录.py
"""
import os
import shutil

#  1、删除文件
# remove: 删除文件（注意不能删除目录）
# os.remove('a.py')

#  2、删除目录
# shutil.rmtree : 可以递归的删除某个目录所有的子目录和子文件
# shutil.rmtree('D:/copy',ignore_errors=True)

# # 3、rmdir删除目录必须是空的，否则会报错
# os.rmdir('D:/copy')

# 修改目录和文件名  同时也当做剪切功能
# rename('旧名字','新名字') 修改文件和目录都可以使用这个方法
os.rename('D:/copy/yyds/yuer/new_wen','D:/wen')