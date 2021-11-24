"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_05嵌套循环.py.py
"""
list1 = ['关羽','张飞','赵云','马超','黄忠']
list2 = ['典韦','许褚','张辽','夏侯惇','夏侯渊']

# 嵌套循环
for numberLis1 in list1:
    for numberLis2 in list2:
        print(f'{numberLis1} -->大战--> {numberLis2}')
