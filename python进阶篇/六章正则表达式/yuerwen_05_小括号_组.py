"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/01
@File   :yuerwen_05_小括号_组.py
"""
# 解说：（）表示 组的概念

import re
names = '''苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的
'''

p = re.compile(r'(^.+)，',re.MULTILINE)
# print(p.findall(names))

names_type = '''张三，手机号码15945678901
李四，手机号码13945677701
王二，手机号码13845666901'''

p1 = re.compile(r'(^.+)，.+(\d{11})',re.M)
for one in p1.findall(names_type):
	pass

# 注意：P是大写的
p2 = re.compile(r'^(?P<name>.+)，.+(?P<phone>\d{11})', re.MULTILINE)
for match in p2.finditer(names_type):
    print(match.group('name'))
    print(match.group('phone'))

# import re
# p = re.compile(r'^(?P<name>.+),.+(?P<phone>\d{11})', re.MULTILINE)
# for match in  p.finditer(names_type):
# 	print(match.group('name'))
# 	print(match.group('phone'))
