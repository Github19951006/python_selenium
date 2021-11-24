"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/10
@File   :test04_读1.py
"""
# 读文件 打开
f = open('yuerwen.txt',encoding='utf8')
# 使用readlines读取每一行，返回列表
lineList = f.readlines()
# 关闭文件流
f.close()

# 循环遍历
for line in lineList:
    print(line)