"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/13
@File   :yuerwen_test.py
"""
import json
import time
from pprint import pprint

import xlwt

def analyzeFile2Excel():
    # 数据字段映射表
    fieldMap = {
        'dynamicTime' : '计划时间',
        'shipNameCn' : '中文船名',
        'shipNameEn' : '英文船名',
        'shipFlag' : '国籍(地区)',
        'shipLength' : '船长',
        'draft' : '吃水',
        'dynamicName' : '动态',
        'startBerth' : '起点泊位',
        'endBerth' : '终点泊位',
        'master' : '主引',
        'assistant' : '副引',
        'assistant2' : '其它引水',
        'orgShort' : '代理',
        'dTelephone' : '代理电话',
        '+++1' : '交通船',
        'channelName' : '航道',
        'headThruster:tailThruster' : '侧推',
        'remarks' : '备注',
    }

    # 创建一个Excel workbook 对象
    book = xlwt.Workbook()
    # 增加一个名为 '年龄表' 的sheet
    sh = book.add_sheet('引航')

    # 写标题栏
    for column, heading in enumerate(fieldMap.values()):
        sh.write(0, column, heading)
        
    # 打开文件
    with open('info1.txt','r',encoding='utf8') as f:
        row = 0
        while True:
            # 读入一行
            oneline =  f.readline()
            
            if not oneline:
                break

            # 一行对应1天的数据
            oneday = json.loads(oneline)

            # 再获取当天 的每行数据
            for line in oneday:
                row += 1
                # time.strftime('%Y%m%d %H:%M', time.localtime(int(line['dynamicTime'] / 1000)))
                # pprint(line)
                for column, field in enumerate(fieldMap.keys()):
                    # print(f'1================{column}')
                    # 没有的，暂时填空
                    if field not in line:
                        value = ''
                    else:
                        value = line[field]

                    # 计划时间要特殊处理
                    if field == 'dynamicTime' :
                        value = time.strftime('%Y%m%d %H:%M', time.localtime(int(line['dynamicTime'] / 1000)))
                        # print(value)
                    # 侧推要特殊处理
                    if field == 'headThruster:tailThruster' :
                        if 'headThruster' not in line:
                            hvalue = '无'
                            # print(hvalue)
                        else:
                            hvalue = line['headThruster']
                        if 'tailThruster' not in line:
                            tvalue = '无'
                        else:
                            tvalue = line['tailThruster']
                            # print(tvalue)
                        value = f"首：{hvalue} 尾：{tvalue}"
                        print(value)

                    sh.write(row, column, value)

    # 保存文件
    book.save('引航表.xls')

# getAllInfo2Text()
analyzeFile2Excel()

print('\n\n === 完成 ==== \n\n')