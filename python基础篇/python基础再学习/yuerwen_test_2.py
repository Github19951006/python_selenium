"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/14
@File   :yuerwen_test_2.py
"""
a = [1, 2, 3.14, 'hello', [7,8,9] ]
# 切片
print(a[-3:-1])

str1 = 'yuer  你好 | wen 非常好 | beautiful 漂亮'
# 字符串切割
# split 方法以参数字符串为分割符 ，将字符串 切割为多个 字符串，作为元素存入一个列表，并返回这个列表。
list1 = str1.split('|')
print(list1)  # ['yuer  你好 ', ' wen 非常好 ', ' beautiful 漂亮']

salary = '''
小王  10000元
小李  20000元
小徐  15000元
'''
# splitlines 按照 换行符 进行切割
list2 = salary.splitlines()
print(list2)  # ['', '小王  10000元', '小李  20000元', '小徐  15000元']