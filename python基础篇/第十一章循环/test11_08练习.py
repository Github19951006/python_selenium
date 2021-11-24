"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_08练习.py
"""
'''
关羽 和张飞 正在玩 剪刀石头布 的游戏。
写一个函数calculate_score， 参数是列表， 里面包含了n个元素也是列表。
比如 像这样 [[“剪刀”, “石头”], [“布”, “剪刀”], [“剪刀”, “剪刀”]]
n 个元素代表 n局 比赛，用列表表示，比如 [“剪刀”, “石头”]
其中第1个元素表示关羽打出的手势，第2个元素是张飞打出的手势。
函数要计算出谁赢得次数多，输出比赛结果。
如果他们打成平手，输出“平局”。

比如：
calculate_score([["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"]]) 
输出应该是： 张飞 3局赢了2局，平手一局，张飞胜出

calculate_score([["布", "石头"], ["石头", "剪刀"], ["石头", "剪刀"]]) 
输出应该是： 关羽 3局赢了3局，关羽胜出
'''
list = [["布", "石头"], ["石头", "剪刀"], ["石头", "剪刀"],["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"],["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"]]
def calculate_score(list1):
    # 赢的计数器
    count = 0
    # 输的计数器
    shu = 0
    # 平的计数器
    ping = 0

    for name in list1:
        if name[0] == '剪刀':
            if name[-1] == '布':
                count += 1
            elif name[-1] == '石头':
                shu += 1
            else:
                ping += 1
        elif name[0] == '布':
            if name[-1] == '剪刀':
                shu += 1
            elif name[-1] == '石头':
                count += 1
            else:
                ping += 1
        else:
            if name[-1] == '剪刀':
                count += 1
            elif name[-1] == '布':
                shu += 1
            else:
                ping += 1
    return count,ping,shu

ret = calculate_score(list)
if ret[0] > ret[-1]:
    print(f'输出应该是： 关羽 {len(list)}局赢了{ret[0]}局，平手{ret[1]}局，关羽胜出')
else:
    print(f'输出应该是： 张飞 {len(list)}局赢了{ret[-1]}局，平手{ret[1]}局，张飞胜出')



