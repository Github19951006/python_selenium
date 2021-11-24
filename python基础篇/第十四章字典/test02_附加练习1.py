import pprint
with open('2019-10-22_11.05.40.log',encoding='utf8') as f:
    infoList = f.read().splitlines()

infoDic = {}

for info in infoList:
    info = info.strip()

    if not info:
        continue

    infoSplit = info.split('|')
    kName = infoSplit[1]
    coin = 1
    # print(kName)

    if infoSplit[1] not in infoDic:
        # 将name作为key 分数作为value
        infoDic[infoSplit[1]] = coin
    else:
        infoDic[infoSplit[1]] += coin


for k,v in infoDic.items():
    print(f'{k} : {v} 个')