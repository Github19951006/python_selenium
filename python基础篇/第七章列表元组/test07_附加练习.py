'''
学完 列表元组 那一章， 做这题补充练习，做好后把代码发给我，先通过几次练习，我大体了解一下你的编程能力
http://v3.byhy.net/prac/pri546/py/002c21/

请把询问每个学生的身高体重 做到函数 askInfo 中，
返回值可以返回一个元组，包括身高、体重两个信息。
然后主体代码调用 3次 这个函数，得到3个学生的身高体重，再计算平均值
'''
def askInfo(a):
    # 请输入学员1的身高:
    height = int(input('请输入学员%d的身高:'%a))
    # 请输入学员1的体重:
    weight = int(input('请输入学员%d的体重:'%a))
    # 元组存储身高、体重
    #tuplenew = (height,weight)
    # 返回一个元组，包括身高、体重
    return height,weight

# 创建空列表，用于存储身高和体重
newlist = []
# 循环调用函数
i = 0
while i < 3:
    i += 1
    ret= askInfo(i)
    newlist.append(ret)
# print(newlist)

# 累加定时器
age = 0
withage = 0
# 从列表中循环获取身高和体重
for i in range(len(newlist)):
    sumHeight = newlist[i][0]
    sumWeight = newlist[i][1]
    age += sumHeight
    withage += sumWeight
# 输出结果
print('平均身高是%.1f'%(age/3))
print('平均体重是%.1f'%(withage/3))

