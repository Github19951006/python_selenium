"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/14
@File   :test01_link.py
"""
def savetofile(nameList, avgFree):
    with open('record.txt','a',encoding='utf8') as f:
        # 通过列表推导式，产生    人：费用  这样的列表
        recordList = [f'{member}:{avgFree}' for member in nameList]
        f.write(' | '.join(recordList) + '\n')