"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/13
@File   :yuerwen__practice.py
"""
'''
请大家写一个程序，依次打印出里面的每一行内容的字符串长度。

注意： 这个文件应该是UTF8编码的格式，但是，由于历史原因，可能里面有些字符不是UTF8编码。

要求大家再解码每行内容的时候，如果UTF8解码错误，捕获该类型的错误，打印出 错误编码在文件中的行数，并且能够继续进行后续行的处理。
'''
with open('0019.txt','rb') as f:
	# 按行读取数据，返回一个列表 <class 'list'>
	bytesLines  = f.read().splitlines()
	# print(type(bytesLines))

# 计数器，统计行数
lineIdx = 1
for l in bytesLines:
	# print(type(l))  # <class 'bytes'>
	# 编码成utf8格式
	try:
		infoStr  = l.decode('utf8')
		print(f'第{lineIdx:04}行，有{len(infoStr)}个字符')
	except Exception:
		print(f'第{lineIdx:04}行，有非UTF8编码字符 ！！！')
	lineIdx += 1