"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/27
@File   :yuerwen_获取某个时间 对应 的年月日时分秒数字_4.py
"""
# 获取某个时间 对应 的年月日时分秒数字
from datetime import datetime
# 获取年
year = datetime.now().year
print(f'年：{year}')

year = datetime.year
print(f'年：{year}')  # <attribute 'year' of 'datetime.date' objects>

# 获取月
month = datetime.now().month
print(f'月：{month}')

# 获取日
day = datetime.now().day
print(f'日：{day}')

# 获取时
H = datetime.now().hour
print(f'时：{H}')

# 获取分
m = datetime.now().minute
print(f'分：{m}')

# 获取秒
s = datetime.now().second
print(f'秒：{s}')

# 获取毫秒
ms = datetime.now().microsecond
print(f'毫秒：{ms}')

# 获取星期几用 weekday方法
# # 0 代表星期一，1 代表星期二 依次类推
weekday = datetime.now().weekday()
print(f'今天星期：{weekday}')
