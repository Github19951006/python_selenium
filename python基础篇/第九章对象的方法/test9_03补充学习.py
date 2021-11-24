"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/03
@File   :test9_03补充学习.py
"""

# 关键字 in
str = input('请输入您的身高 和 体重， 用逗号隔开:')
if '，' in str:
    print('您的输入包含了逗号')
elif '，' not in str:
    print('输入的不包含逗号')
else:
    pass