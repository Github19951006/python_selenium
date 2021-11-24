"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :1.py
"""
content = '''苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的'''

import re
p = re.compile(r'^(.*)，', re.MULTILINE)
# for one in  p.findall(content):
q = p.findall(content)[0]
print(q)