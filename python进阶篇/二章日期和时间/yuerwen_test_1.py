"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/29
@File   :yuerwen_test_1.py
"""
import datetime
import dateutil.parser
from datetime import  timezone
def getDateTime(s):
    d = dateutil.parser.parse(s)
    dt = d.replace(tzinfo=timezone.utc).astimezone(tz=None)
    print(dt.strftime('%Y-%m-%d %H:%M:%S'))
    print(d.strftime('%Y-%m-%d %H:%M:%S'))

getDateTime('19/May/2017:04:10:06 +0000')