"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/24
@File   :yuerwen_lx_1.py
"""
import os
import shutil
'''
请写一个程序，在当前工作目录下，创建 如下的目录层级结构
backup/new/
然后把整个下载的source目录 内容，拷贝到 backup/new/source 目录里面去。
'''
# 创建层级目录
os.makedirs('backup/new/',exist_ok=True)

# 下载的source目录 内容，拷贝到 backup/new/source 目录里面去
shutil.copytree(r'C:\Users\Administrator\Desktop\source','backup/new/source')
shutil.copyfile()
'''
练习总结：
1、创建目录区别：  mkdir()     makedirs()
2、拷贝文件和拷贝目录的区别：shutil
	拷贝文件：copyfile()
	拷贝目录：copyTree()
'''