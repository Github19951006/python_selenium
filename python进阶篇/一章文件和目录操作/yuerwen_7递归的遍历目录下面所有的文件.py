"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/21
@File   :yuerwen_7递归的遍历目录下面所有的文件.py
"""
import os
# 获取某个目录中所有的 文件， 包括子目录里面的文件。 可以使用 os库中的walk方法

# 要得到某个目录下面所有的子目录 和所有的文件，存放在两个列表中
path = r'D:\test'
files = []
dirs = []

# 下面的三个变量 dirpath, dirnames, filenames
# dirpath 代表当前遍历到的目录名
# dirnames 是列表对象，存放当前dirpath中的所有子目录名
# filenames 是列表对象，存放当前dirpath中的所有文件名
for dirpath,dirnames,filenames in os.walk(path):
	files += filenames
	dirs += dirnames
	# print(dirpath)  深度查找方式

print(f'文件列表：{files}')
print(f'目录列表：{dirs}')

# 要得到某个目录下所有文件的全路径可以这样
for dirpath,dirnames,filenames in os.walk(path):
	for fn in filenames:
		# 把 dirpath 和 每个文件名拼接起来 就是全路径
		fpath = os.path.join(dirpath, fn)
print(fpath)

