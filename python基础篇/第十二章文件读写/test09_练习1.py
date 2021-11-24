"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/11
@File   :test09_练习1.py
"""
'''
请编写一个程序，将其中年龄大于50岁的找出来， 并且以这样的格式追加到该文件末尾中。
大于50岁的人有：xxx,xxx,xxx
'''
# 打开文件
f = open('0013_a1.txt','r',encoding='utf8')
# 按行读取文件，返回的是列表
#content = f.read()
#print(content)

# 读取文件字符串 返回 f.read()的是字符串，.splitlines() 字符串 按换行符 进行切割，返回的是一个列表
content = f.read().splitlines()
print(content)
# 创建一个空列表，存储
oldPeople = []

# 循环遍历
for line in content:
    # 去除空格
    line = line.replace(' ','')

    # 如果不是字符串就 continue
    if not line:
        continue

    name,age = line.split(":")
    if int(age) > 50:
        oldPeople.append(name)
print(oldPeople)

# 将列表转换成字符串
oldPeopleStr = '，'.join(oldPeople)
print(oldPeopleStr)
print(f'大于50岁的人有：{oldPeopleStr}')




