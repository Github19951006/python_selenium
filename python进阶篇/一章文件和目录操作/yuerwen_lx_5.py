"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/25
@File   :yuerwen_lx_5.py
"""
import os
'''
题目5
请写一个程序，找出下载的source目录里面（包含子目录）所有扩展名为.avi的文件，扩展名改为.dll
'''
pathfiles = 'backup/new/source'
files = []
for (dirpath,dirname,filername) in os.walk(pathfiles):
	files += filername
	for fname in files:
		if fname.endswith('.avi'):
			# backup/new/source\sub1\sub11\d1.avi
			filerPaht = os.path.join(dirpath,fname)
			# print(filerPaht)
			# 字符串的拼接
			newfilers = fname[:-3] + 'dll'
			endfilers = os.path.join(dirpath,newfilers)
			# print(endfilers)
			# 修改文件名称
			os.rename(filerPaht,endfilers)
		