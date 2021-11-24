"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/24
@File   :yuerwen_lx_3.py
"""
import shutil
import os
'''
题目3
请写一个程序，删除掉 下载的source目录里面（不包含子目录）所有的扩展名为bmp的文件
'''

# 目标目录
pathFiler = 'backup/new/source'
# 循环获取文件和目录的名称，针对一个层级的
for filers in os.listdir(pathFiler):
	# 将路径拼接起来
	filesPath = os.path.join(pathFiler, filers)
	# 判断拿到的filesPath是不是文件路径名称 并且是不是.bmp结尾的文件
	if os.path.isfile(filesPath) and filesPath.endswith('.bmp'):
		print(f'删除的文件:{filesPath}')
		# 删除文件
		os.remove(filesPath)
# 获取文件内容的大小

