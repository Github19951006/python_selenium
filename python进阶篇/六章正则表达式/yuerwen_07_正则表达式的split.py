"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/03
@File   :yuerwen_07_正则表达式的split.py
"""
# 需求：下面字符串中提取武将的名字
import re

content = '关羽; 张飞, 赵云,马超, 黄忠  李逵'

p_list = re.split(r'[;,\s]\s*',content)
for one in p_list:
	print(one,end=' ')