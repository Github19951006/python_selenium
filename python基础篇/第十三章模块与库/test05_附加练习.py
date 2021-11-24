"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/15
@File   :test05_附加练习.py
"""
'''
如果我们要导入的包不在我们执行文件目录相同，则找不到导包的路径，就会报错如下：
    ModuleNotFoundError: No module named 'getissue'
    

'''
import sys
sys.path.append('c:\lib')
from getissue import getIssueBody

print(getIssueBody(1))