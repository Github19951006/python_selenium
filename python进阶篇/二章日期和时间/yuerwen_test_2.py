"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/29
@File   :yuerwen_test_2.py
"""
from datetime import datetime,timedelta

# 要计算出 2018年6月24日 是星期几
thatDay = "2018-6-24"
# 先把字符串表示的日期转化为 datetime 对象
theDay = datetime.strptime(thatDay, "%Y-%m-%d")
#再获取星期几
print(theDay)


# 今天是星期几
datetime.now().weekday()
print(f'今天是星期:{datetime.now().weekday()+1}')

# 明天或昨天是星期几
tm_dt = datetime.now().date() + timedelta(days=1)
print(f'明天是星期:{tm_dt.weekday()+1}')

bf_dt = datetime.now().date() - timedelta(days=1)
print(f'昨天是星期:{bf_dt.weekday()+1}')

# 从某个时间点往前或者后推 一段时间,再判断是什么日期和星期几
that_day = '2019-10-01'
# 将字符串转换成数据对象
object_dt = datetime.strptime(that_day,'%Y-%m-%d').date()
print(object_dt)
# 后推120天 的日期
days = object_dt + timedelta(days=120)
print(days)
# 120天后是星期几
print(f'120天后是星期:{days.weekday()+1}')

# 往前推120天 的日期
days = object_dt - timedelta(days=120)
print(days)
# 往前120天后是星期几
print(f'往前120天后是星期:{days.weekday()+1}')