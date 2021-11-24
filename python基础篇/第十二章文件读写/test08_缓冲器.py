"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/11
@File   :test08_缓冲器.py
"""
'''
f = open('tmp.txt','w',encoding='utf8')
f.write('白月黑羽：祝大家好运气')
# 等待 30秒，再close文件
import time
time.sleep(30)

f.close()
'''

f = open('tmp.txt','w',encoding='utf8')
f.write('白月黑羽：祝大家好运气')
# 立即把内容写到文件里面
f.flush()

# 等待 30秒，再close文件
import time
time.sleep(30)

f.close()