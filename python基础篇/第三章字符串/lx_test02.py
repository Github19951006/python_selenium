"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/07/28
@File   :lx_test02.py
"""
'''
请定义一个函数printlen, 该函数中让用户输入一个字符串， 该函数打印出用户输入的这个字符串的 长度
比如 用户输入 123456789， 该函数应该打印出：长度为9
'''
# 定义创建字符串长度的函数
def printlen():
    strName = input("请输入字符串：")
    return len(strName)
# 将返回的字符串长度，将长度int类型转换为字符串类型
len =  printlen()
# 打印字符串长度的结果
print(f'长度为: {len}')