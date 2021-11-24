"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/02
@File   :test9_01.py
"""
'''
字符串的方法：
1、count
2、find
3、split
4、join
5、strip、lstrip、rstrip
6、replace
7、startswith、
8、endswith
9、isdigit
10、字符串倒序
'''

# 创建字符串
str = '     你好，中国   加油！中国女排加油！yyds     '

#1 count()方法：统计字符串中的指定参数的个数；
ret = str.count('国女')
print(ret) # 返回个数

#2 find()方法：查询指定参数索引下标值（第一次出现的索引）
ret1 = str.find('加油')
print(ret1) # 返回索引下标值

#3 split()方法：以字符串中的元素为分隔符，从字符串中截取我们想要的部分，返回的是列表
listRet = str.split('！')
# 返回的是个列表
print(listRet) # ['你好，中国加油', '中国女排加油', 'yyds']

#4 join()方法：将列表中的字符串元素 以某字符串为连接符， 连接为一个字符串
strRet = '***'.join(listRet)
# 返回的是字符串
print(strRet) # 你好，中国加油***中国女排加油***yyds

#5.1 strip()方法：去除左右两边的空格
ret5= str.strip()
print(ret5)

# 5.2 lstrip()方法：去除左边的空格
ret52 = str.lstrip()
print(ret52)

# 5.3 rstrip()方法：去除左边的空格
ret53 = str.rstrip()
print(ret53)

# replace():用来 替换 字符串里面 所有指定的 子字符串
ret6 = str.replace(' ','')
print(ret6)
