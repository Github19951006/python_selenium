"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/10
@File   :test05_读2.py
"""
'''
 如果你不想要换行符，可以使用字符串对象的splitlines方法
'''
# 读文件打开
f = open('yuerwen.txt',encoding='utf8')
# 读取文件信息
conten = f.read()
# 关闭文件流
f.close()
# 按行切割，返回列表
lineList = conten.splitlines()
# 循环遍历
for line in lineList:
    print(line)

