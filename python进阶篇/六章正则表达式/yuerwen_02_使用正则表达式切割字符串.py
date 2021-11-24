"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/30
@File   :yuerwen_02_使用正则表达式切割字符串.py
"""
# 正则表达式的切割 商品list
import re
list_str = '关羽; 张飞, 赵云,马超, 黄忠  李逵'
# 返回一个列表
p = re.split(r'[;,\s]\s*',list_str)
for one in p:
	print(one,end='  ')
