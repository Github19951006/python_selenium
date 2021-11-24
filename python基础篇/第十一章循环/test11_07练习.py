"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_07练习.py
"""
'''
有如下的字符串，记录了三国人物的名字和年龄

ageTable = '
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'
请写一个程序将其中 30岁以上和以下的人分别打印出来，类似这样

大于等于30岁的人有：
刘备
赵云
张飞
关羽

小于30岁的人有：
诸葛亮
刘琦
'''
ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''
# 将字符串的元素按行取出
line = ageTable.splitlines()
# 创建空列表，目的：存储字符串的元素按行取出的元素
listAge = []
# 循环遍历做过滤
for lineName in line:
    # 对列表的进行去除空格
    lineName = lineName.strip()
    # 如果元素不为空，就存储到列表中
    if lineName != '':
        listAge.append(lineName)

# 创建列表，存储年龄大于30岁的
maxage30 = []
#  创建列表，存储年龄小于30岁的
minage30 =[]
# 循环遍历
for name in listAge:
    # 对元素进行切片处理
    numberName,age = name.split(',')
    # 1、对age进行字符串转换为数字，
    # 2、再判断是否大于等于30
    if int(age) >= 30:
        # 追加到maxage30列表的最后
        maxage30.append(numberName)
    else:
        # 追加到minage30列表的最后
        minage30.append(numberName)

# 遍历列表
def getlist(listName):
    for name in listName:
        print(name)

print('大于等于30岁的人有：')
getlist(maxage30)
print('小于等于30岁的人有：')
getlist(minage30)


