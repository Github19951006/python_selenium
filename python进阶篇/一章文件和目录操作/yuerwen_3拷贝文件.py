"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/19
@File   :yuerwen_3拷贝文件.py
"""
import shutil

# 拷贝文件
shutil.copyfile('test.txt','D:/test_Copy.txt')

# 拷贝目录
shutil.copytree('D:/test','D:/copy/yyds')
