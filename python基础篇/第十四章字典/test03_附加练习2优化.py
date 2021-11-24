'''
每次查询时，提示 请输入要查询的股票名称或代码：

当用户输入股票代码（6位全是数字）时，打印出对应的 股票名称和代码

当用户输入股票名称（不全是数字）时，打印出对应的 股票名称和代码
'''
with open('stock.txt',encoding='utf8') as f:
    infoList = f.read().splitlines()
listDicName = {}
listDicCode = {}

def getname(num):
    for info in infoList:
        # # 去除左右空格
        # info = info.strip()

        # 去除空行
        if not info:
            continue
        # 切割
        infoSp = info.split('|')
        '''
        优化
        '''
        infoKeys = infoSp[0].strip()
        infoValues = infoSp[-1].strip()
        
        listDicName[infoKeys] = f'{infoKeys}:{infoValues}'
        listDicCode[infoValues] = f'{infoKeys}:{infoValues}'
    
    if num.isdigit():
        # 一定要写全6位股票代码
        if len(num) < 6:
            print('请写全6位股票代码')
            # continue
        elif num in listDicCode:
            print(listDicCode[num])
        else:
            print('找不到该股票代码')
        # 如果不全是数字，作为股票名称处理
    else:
        if num in listDicName:
            print(listDicName[num])
        else:
            print('找不到该股票名称')

while True:
    num = input('请输入要查询的股票名称或代码：')
    num = num.strip()
    getname(num)