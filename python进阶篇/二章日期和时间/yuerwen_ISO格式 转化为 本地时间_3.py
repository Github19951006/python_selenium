"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/27
@File   :yuerwen_ISO格式 转化为 本地时间_3.py
"""
# 很多时候，程序获取的时间是 ISO 8601 格式的字符串
'''
2008-09-03T20:56:35.450686+00:00
2008-09-03T20:56:35.450686Z
'''
# 注意：下载dateutil库  使用:pip3 install python-dateutil  这个命令行下载才不会报错
from datetime import timezone
import dateutil.parser

# 将字符串时间 转化为 datetime 对象
dateObject = dateutil.parser.isoparse('2021-09-03T20:56:35.450686Z')
# print(dateObject)  2021-09-03 20:56:35.450686+00:00

# 根据时区 转化为 datetime 数据
localdt = dateObject.replace(tzinfo = timezone.utc).astimezone(tz=None)
# print(localdt)  # 2021-09-04 04:56:35.450686+08:00

# 产生本地格式 字符串
print(localdt.strftime('%Y-%m-%d %H:%M:%S'))
