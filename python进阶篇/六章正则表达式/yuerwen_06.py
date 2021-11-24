"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/03
@File   :yuerwen_06.py
"""
content = '''
<div class="el">
        <p class="t1">
            <span>
                <a>Python开发工程师</a>
            </span>
        </p>
        <span class="t2">南京</span>
        <span class="t3">1.5-2万/月</span>
</div>
<div class="el">
        <p class="t1">
            <span>
                <a>java开发工程师</a>
            </span>
		</p>
        <span class="t2">苏州</span>
        <span class="t3">1.5-2/月</span>
</div>
'''

import re
p = re.compile(r'class=\"t1\">.*?<a>(.*?)</a>', re.DOTALL)
for one in  p.findall(content):
    print(one)