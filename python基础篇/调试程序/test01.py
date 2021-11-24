"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/17
@File   :test01.py
"""

'''
三星S8,     110,50,5200
三星Note8,  123,30,6800

华为Mate10, 170,170,4100
华为P10,    167,57,3300

小米 6,     133,81,2200
小米 mix,   173,61,3200
'''
import requests

# 用requests获取销量信息
res = requests.get('http://cdn1.python3.vip/files/py/0016_price')
# 编码转换成 utf8
res.encoding = 'utf8'
content = res.text
# print(content)

# 下面两个变量记录当前找到的销量最多的手机和卖出数量
# 初始值都是None
mostsoldphone = None
mostsoldcount = None

# splitlines() 按行切割获取
for info in content.splitlines():
    info = info.strip()
    # print(info)
    
    # 去掉空行
    if not info:
        continue
        
    # 按逗号切割
    items = info.split(',')
    # 销量在倒数第二列，获取销量信息
    soldcount = items[-2]
    # 型号在 第一列，  获取型号信息
    phonetype = items[0]

    # 如果前面已经有销量最多的手机记录，和当前这款手机销量比较
    if mostsoldphone:
        # 如果当前这款手机销量更高，把它置为最热卖手机
        if int(mostsoldcount) < int(soldcount):
            mostsoldcount = soldcount
            mostsoldphone = phonetype

    # 如果前面没有有销量最多的手机记录，说明这是第一条记录
    # 暂时先把它置为最热卖手机
    else:
        mostsoldcount = soldcount
        mostsoldphone = phonetype

print(f'最热卖手机是: {mostsoldphone}, 销量是: {mostsoldcount}')
