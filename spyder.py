# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 00:15:53 2018

@author: roy
"""

import json, urllib, numpy as np, matplotlib.pyplot as plt
from urllib import request

a = 'https://www.lnb.com.tw/api/market-place?page='
b = '&per_page=10&sendback='
url = [a+str(i)+b+str(i) for i in range(1, 24)]
def spyder(http):
    try: 
        with request.urlopen(http, timeout = 10) as response:
            content = response.read()
            data_list = json.loads(content)['data']
    except Exception as e:
        content = None
        data_list = None
        print('crawl data exception.' + str(e))
    return data_list

test = [spyder(url[i]) for i in range(len(url))]

ty = [test[i][j]['credit_level'].replace('_NPR', '') for i in range(len(test)) for j in range(len(test[i]))]

level, count = np.unique(ty, return_counts = True)

plt.bar(level, count, width =1/5, color = "blue")