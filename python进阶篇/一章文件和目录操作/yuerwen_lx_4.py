"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/25
@File   :yuerwen_lx_4.py
"""
import shutil
import os
'''
题目4
请写一个程序，找出下载的source目录里面（不包含子目录）所有扩展名为.avi的文件，扩展名改为.dll
'''
# 考察的知识点：修改文件名称
# 目标目录
pathFiler = 'backup/new/source'
# 循环获取文件和目录的名称
for fn in os.listdir(pathFiler):
	# 将路径拼接起来
	filerPaht = os.path.join(pathFiler,fn)
	# 判断
	if os.path.isfile(filerPaht) and filerPaht.endswith('.avi'):
		# 字符串的拼接
		newfilers = filerPaht[:-3] + 'dll'
		# 修改文件名称
		os.rename(filerPaht,newfilers)