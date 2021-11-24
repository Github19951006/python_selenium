"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/10
@File   :test07_with.py
"""

'''
with...as...
使用这种方式避免忘记关闭文件流，而导致的问题
'''

with open('yuerwen.txt',encoding='utf8') as f:
    # 按行读取文件,返回的是字符串
    content = f.read()
    # 把字符串 按换行符 进行切割
    content = content.splitlines()
    print(content)  # ['yuerwen,加油！！', 'yuerwen,加油！！', 'yuerwen,加油！！']
    # 列表遍历
    for line in content:
        print(line)