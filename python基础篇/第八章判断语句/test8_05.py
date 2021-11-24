"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/02
@File   :test8_05.py
"""

'''
课内练习：
请大家实现一个程序， 对天气的人体舒适度进行评估。 该程序运行起来先询问用户

请输入今天气温（单位 摄氏度）:
用户输入气温（比如28.3）后，再询问用户

请输入今天气压（单位 帕）:
用户输入气压（比如270）后进行如下判断：

如果气温 > 30 或者 < -8：显示：不舒适
如果气压 > 300 或者 < 20： 显示：不舒适
如果 25 < 气温 <= 30 并且 200 < 气压 <= 300：显示：比较舒适
如果 10 < 气温 <= 25 并且 100 < 气压 <= 200： 显示：特别舒适
如果 -8 <= 气温 <=10 并且 20 <= 气压 <= 100： 显示：比较舒适
其他情况： 显示 本程序不能判断
'''
'''
def beautiful(qiwen,qiya):
    if qiwen >30 or qiwen < -8:
        print("不舒适")
        return
    if qiya > 300 or qiya < 20:
        print("不舒适")
        return
    # 判断 气温
    if qiwen >25 and qiwen <= 30:
        if qiya >200 and qiya <= 300:
            return '比较舒适'

    if qiwen >10 and qiwen <= 25:
        if qiya >100 and qiya <= 200:
            return '特别舒适'

    if qiwen >-8 and qiwen <= 10:
        if qiya >20 and qiya <= 100:
            return '比较舒适'
    else:
        print('无法判断')
        
qiwen = int(input("请输入今天气温（单位 摄氏度）:"))
qiya = int(input("请输入今天气压（单位 帕）:"))
print(beautiful(qiwen,qiya))
'''
# -------------------------------------------------if-elif的写法-----------------------------------------------
# 使用if-elif的写法：
def beautiful(qiwen,qiya):
    if qiwen > 30 or qiwen < -8:
        print("不舒适")
    elif qiya > 300 or qiya < 20:
        print("不舒适")

    elif 25 < qiwen <= 30 and 300 < qiya < 20 :
        print('比较舒适')
    elif 10 < qiwen <= 25 and 100 < qiya < 200 :
        print('比较舒适')
    elif -8 < qiwen <= 10 and 20 < qiya < 100 :
        print('比较舒适')
    else:
        print('无法判断')


qiwen = int(input("请输入今天气温（单位 摄氏度）:"))
qiya = int(input("请输入今天气压（单位 帕）:"))
beautiful(qiwen,qiya)