"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/24
@File   :yuerwen_lx_2.py
"""
import os
'''
题目2
请写一个程序，计算出 下载的source目录里面（不包含子目录）所有的文件的大小之和
'''
'''
1、获取某个目录的下为文件 for f in os.listdir(path) if
'''
path = 'backup/new/source'

# 计数器 统计文件大小的
totalsize = 0

# listdir()：获取的是当前文件夹的所有子目录和文件的 名称
for f in os.listdir(path) :
	# 将路径拼接起来
	filesPath = os.path.join(path,f)
	# 判断拿到的filesPath是不是文件路径名称
	if os.path.isfile(filesPath) :
		# 获取文件内容的大小
		totalsize += os.path.getsize(filesPath)
		
print(f'合计大小为 ：{totalsize} 字节')

'''
练习总结：
1、listdir()：获取的是当前文件夹的所有子目录和文件的 名称
2、os.path.isfile(filesPath)  判断filesPath这个参数路径是不是文件
3、os.path.getsize(filesPath) 获取文件内容的大小
'''
