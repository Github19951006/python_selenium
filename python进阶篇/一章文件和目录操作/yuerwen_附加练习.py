"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/25
@File   :yuerwen_附加练习.py
"""
'''
下载zip包，解压后出现一个 prac_re 目录，该目录中有很多文件。
请写代码，检查目录中所有文件，找出包含如下格式的文本
https://www.bilibili.com/video/av74106411/?p=60
将数字的值改为 +3， 比如，上面的链接就需要改为
https://www.bilibili.com/video/av74106411/?p=63
如果链接后面的是 p=1 就要改为 p=4, 是 p=99 就要改为 p=102,
最后将修改结果写回文件。
'''
import time
import os
"""
@Project ：python
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/25
@File   :yuerwen_附加练习.py
"""
'''
下载zip包，解压后出现一个 prac_re 目录，该目录中有很多文件。
请写代码，检查目录中所有文件，找出包含如下格式的文本
https://www.bilibili.com/video/av74106411/?p=60
将数字的值改为 +3， 比如，上面的链接就需要改为
https://www.bilibili.com/video/av74106411/?p=63
如果链接后面的是 p=1 就要改为 p=4, 是 p=99 就要改为 p=102,
最后将修改结果写回文件。
'''
import os

# 目标路径
path = 'prac_re'

def getCopy(number):
	newStr = ''
	# 递归的遍历目录下面所有的文件
	# 下面的三个变量 dirpath, dirnames, filenames
	# dirpath 代表当前遍历到的目录名
	# dirnames 是列表对象，存放当前dirpath中的所有子目录名
	# filenames 是列表对象，存放当前dirpath中的所有文件名
	for (dirpath,dirname,filesname) in os.walk(path):
		for filename in filesname:
			# filename是代表文件的名称
			# os.path.join 是文件路径的拼接
			fpath = os.path.join(dirpath,filename)
			# utf8编码 读取文件
			with open(fpath,'r',encoding='utf8') as f:
				# splitlines() 是按换行符切割，得到一行行的元素存储到列表中
				flist = f.read().splitlines()
				

				for f  in flist:
					if 'https://www.bilibili.com/video/av74106411/?p=' in f:

						# 3.1 用find()方法定位到 https://www.bilibili.com/video/av74106411/?p= 的索引位置location
						location = f.find('https://www.bilibili.com/video/av74106411/?p=')

						# 3.2 得到数字的起始位置 locationStar = location + len(https://www.bilibili.com/video/av74106411/?p=)
						locationStar = location + len('https://www.bilibili.com/video/av74106411/?p=')

						# 3.3 得到数字结束的位置 locationEnd
						# 3.3.1 循环判断 locationStar开始后的每个字符isdigit()
						locationEnd = locationStar
						while f[locationEnd].isdigit():
							locationEnd += 1

						# 3.4 得到具体的数字 number[locationStar:locationEnd]
						if int(f[locationStar:locationEnd]) == 1:
							numberRet = int(f[locationStar:locationEnd].replace(int(f[locationStar:locationEnd]),4))
						elif int(f[locationStar:locationEnd]) == 99:
							numberRet = int(f[locationStar:locationEnd].replace(int(f[locationStar:locationEnd]),102))
						else:
							numberRet = int(f[locationStar:locationEnd]) + number

						# 4、将字符串拼接 lines[:locationStar] + 替换的数字 + lines[locationEnd:]
						str2 = f[:locationStar] + str(numberRet) + f[locationEnd:]

						# 5、将拼接的字符串，存储到空字符串中
						newStr += str2

						# 6、通过w写入文件中
						with open(fpath, 'w', encoding='utf') as f1:
							f1.write(newStr)
getCopy(3)