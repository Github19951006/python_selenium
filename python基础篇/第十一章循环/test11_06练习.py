"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_06练习.py
"""
str1 = '''
熊宁
杰益

王伟伟

青芳

玉琴
焦候涛
莫福
杨高旺
唐欢欢
韩旭
'''

str2 = '''
焦候涛 
熊宁 
玉琴 

骆龙 

韩旭 
杨高旺

杰益  

莫福  

伟伟

李福  
'''
#请写一个程序
#找出 str1 中所有 str2 中不存在的人名，并且
#找出 str2 中所有 str1 中不存在的人名
'''
伪代码：
从str1中获取每一行：
    如果该行中包含改名字
        到str2中查找，看看是否有同样的人名
            如果str2中有改人名，记录下来
'''

#1 将字符串中的元素按行取出，返回列表

def getNameList(nameStr):
    # 创建列表
    listNames = []
    # 将str1和str2中人名存储到列表中
    # 获取字符串中行，返回的是列表
    lineListStr1 = nameStr.splitlines()
    print(lineListStr1)
    # 对列表进行遍历
    for line in lineListStr1:
        # 对列表元素去除空行
        name = line.split()
        # 判断名字是否等于''，如果不等于就追加到列表中
        if name != '':
            listNames.append(name)
    # 返回列表
    return listNames

# 调用执行函数
names1 = getNameList(str1)
names2 = getNameList(str2)

# 做判断
#找出 str1 中所有 str2 中不存在的人名
l1 = []
for name in names1:
    if name not in names2:
        l1.append(name)

#找出 str2 中所有 str1 中不存在的人名
l2 = []
for name in names2:
    if name not in names1:
        l2.append(name)

print(f'str1 中所有 str2 中不存在的人名<====>:{l1}')
print(f'str2 中所有 str1 中不存在的人名<====>:{l2}')


'''
list = []
#list1 = []
for nameStr1 in str1:
    if nameStr1 == '  ':
        continue
    list.append(nameStr1)
print(list)

    for nameStr2 in str2:
        if nameStr2 != nameStr1:
            # str1中没有的名字追加到列表中
            list.append(nameStr1)
        else:
            list1.append(nameStr2)
'''
