"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/14
@File   :test01.py
"""

import os
print(f"环境变量 byhy ：{os.environ['byhy']}") # KeyError: 'byhy'
print(f"path:{os.environ['Path']}")
