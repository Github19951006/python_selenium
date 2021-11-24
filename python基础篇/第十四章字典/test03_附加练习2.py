'''
每次查询时，提示 请输入要查询的股票名称或代码：

当用户输入股票代码（6位全是数字）时，打印出对应的 股票名称和代码

当用户输入股票名称（不全是数字）时，打印出对应的 股票名称和代码
'''
with open('stock.txt',encoding='utf8') as f:
    infoList = f.read().splitlines()
listDic = {}

def getname(num):
    for info in infoList:
        # # 去除左右空格
        # info = info.strip()

        # 去除空行
        if not info:
            continue
        # 切割
        infoSp = info.split('|')

        infoK = infoSp[0].strip()
        infoV = infoSp[-1].strip()
        # print(infoV)
        # 将列表的值 加到 字典中
        if infoK not in listDic:
            listDic[infoK] = infoV
    # print(listDic)
    if num in listDic:
        # print('不在')
        print(f'{num}:{listDic[num]}')
    elif num in listDic.values():
        new_listDic = {v: k for k, v in listDic.items()}
        # new_dict['1001']
        print(f'{new_listDic[num]}:{num}')
    else:
        print('不在')

            # print(f'{listDic[num]}:{infoV}')

while True:
    num = input('请输入要查询的股票名称或代码：')
    getname(num)