"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/01
@File   :test8_03.py
"""
'''
课程例子：
里程      	收费
<= 3公里	    20 元/每公里
>3公里	    15 元/每公里
'''
'''
def charge(miles):
    # 判断操作
    if miles <= 3:
        unit = 20
        # 计算收费
    else:
        unit = 15
    return unit * miles

miles = int(input("输入公里数："))
# 调用函数
print("行驶里程费用：",charge(miles))
'''

'''
课程例子：
如果有更多的判断逻辑，就需要使用 elif 了
<= 3公里	20 元/每公里
>3公里 且 <= 5公里	15 元/每公里
>5公里 且 <= 8公里	12 元/每公里
>8公里	10 元/每公里
'''

def charge(miles):
    # 判断
    if miles <= 3:
        unit = 20
    elif miles <= 5:
        unit = 15
    elif miles <= 8:
        unit = 12
    else:
        unit = 10
    return unit * miles

# 键入公里数
miles = float(input("输入公里数："))
# 调用函数。打印结果
print("行驶里程费用：",charge(miles))