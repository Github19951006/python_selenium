"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/01
@File   :yuerwen_04_匹配尾部的位置.py
"""
import re
names = '''
001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80
'''
# 解说：$表示匹配文本的 结束 位置

# 正则表达式
p = re.compile(r'\d+$',re.MULTILINE) # 第二个参数 re.MULTILINE ，指明了使用多行模式
# 返回的是一个列表
p_list = p.findall(names)
print(p_list)
for one in p_list:
	print(one)
