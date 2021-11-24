"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/01
@File   :test8_04.py
    条件判断嵌套
"""
'''
里程	        时间  	    收费
<= 3公里	    <= 1小时	    20 元/每公里
            > 1小时	    22 元/每公里
            
>3公里	    <= 1小时	    15 元/每公里
            > 1小时	    18 元/每公里
'''

def charge(mile,times):
    # 判断公里
    # <= 3公里
    if mile <= 3:
        # 判断时间
        # <= 1小时
        if times <= 1:
            # 费用
            print("每公里20元")
            return times * 20
        # > 1小时
        else:
            # 费用
            print("每公里22元")
            return times * 22
    # > 3公里
    else:
        # 判断时间
        # <= 1小时
        if times <= 1:
            # 费用
            print("每公里15元")
            return times * 15
        # > 1小时
        else:
            # 费用
            print("每公里18元")
            return times * 18

print('费用：',charge(1,1))