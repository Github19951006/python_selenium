"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/15
@File   :test04_附加练习.py
"""
'''
题目1
请大家使用 pip install requests 命令安装好 requests 库。
该库可以用来构建http请求发送给服务器，并获取响应消息。 经常用于测试服务端和一些自动化工作。
使用文档可以参考：http://cn.python-requests.org/zh_CN/latest/

新浪提供了股票数据 web API服务， 可以 得到指定股票的最新行情
url为 http://hq.sinajs.cn/list=<股票代码>
以大秦铁路（股票代码：sh601006）为例，如果要获取它的最新行情，只需访问新浪的接口： http://hq.sinajs.cn/list=sh601006
这个url会返回一串文本，例如：

var hq_str_sh601006="大秦铁路, 27.55, 27.25, 26.91, 27.55, 26.20, 26.91, 26.92,22114263, 589824680, 4695, 26.91, 57590, 26.90, 14700, 26.89, 14300,26.88, 15100, 26.87, 3100, 26.92, 8900, 26.93, 14230, 26.94, 25150, 26.95, 15220, 26.96, 2008-01-11, 15:05:32";
这个字符串由许多数据拼接在一起，不同含义的数据用逗号隔开了，按照程序员的思路，顺序号从0开始。

0：”大秦铁路”，股票名字；
1：”27.55″，今日开盘价；
2：”27.25″，昨日收盘价；
后面的字段我们就不需要了

请大家写一个程序，该程序实现一个函数 getStockPrice ，利用 requests库, 获取 指定某只股票的今日开盘价格。该函数的参数为指定股票的代码。
'''
import requests
def  getStockPrice(stockName):
    # 构造 HTTP 请求
    url = f'http://hq.sinajs.cn/list={stockName}'

    # 返回的response 对应响应消息的对象
    response = requests.get(url)  # <Response [200]>

    # print(type(response))  # <class 'requests.models.Response'>

    # 返回的内容在消息体中，通过text属性获取
    info = response.text
    print(info)  # <class 'str'>
    # print(type(info))

    # 返回的是这种格式 大秦铁路, 27.55, 27.25, 26.91,
    # 通过split 方法截取
    price = info.split(',')[1]

    return price

price = getStockPrice('sh601006')
print(f'1:"{price}",今日开盘价；')
