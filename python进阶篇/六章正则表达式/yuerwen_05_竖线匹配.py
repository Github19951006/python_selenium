"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/01
@File   :yuerwen_05_竖线匹配.py
"""
# 解说：|竖线匹配 是优先级最低的匹配
# 表示 或者的意思

import re
names = '''
001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80
99桃子'''
p = re.compile(r'苹果|香蕉|桃子')
print(type(p))  # <class 're.Pattern'>
for one in p.findall(names):
	print(one)

