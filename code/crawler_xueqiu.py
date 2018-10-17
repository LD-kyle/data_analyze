# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:55:58 2018

@author: Jason
"""

import requests
import pandas as pd
from lxml import etree
from urllib.parse import unquote
from urllib.parse import quote
import json
import re
import time

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}


def get_page(page,s):
    r = s.get('https://xueqiu.com/stock/cata/stocklist.json?page={}&size=30&order=desc&orderby=percent&type=11,12&_=1535607899672'.format(page),headers=headers)
    return r.json(),r.status_code

def get_attention(uid,s):
    r = s.get('https://xueqiu.com/recommend/pofriends.json?type=1&code={}&start=0&count=14'.format(uid),headers=headers,timeout=10)
    return r.json(),r.status_code

def crawl(t):
    url0='https://xueqiu.com/hq'
    url='https://xueqiu.com/S/'
    s=requests.Session()
    r=s.get(url0,headers=headers)
    list1,list2,list3=[],[],[]
    if r.status_code==200:      
        for i in range(1,186):
              dict0,c=get_page(i,s)
              if c!=200:
                  break
              list0=dict0["stocks"]  
              for x in list0:
                   list1.append(x["symbol"])
                   list2.append(x["name"])
        print(len(list1))
    r=s.get(url+list1[0],headers=headers, timeout=10)
    for x in list1:
       done,a=True,0 
       while done: 
         try:
           #r=s.get(url+x,headers=headers, timeout=10)
           dict1,c1=get_attention(x,s)
           if c1==200:
              list3.append(dict1["totalcount"])
              print(x)
              done=False
         except Exception as e:
             a+=1
             print(x,e)
             if ('Read timed out' not in str(e))&(a>10):
             #if ('list index out of range' not in str(e))&(a>10):
               if 'line 1 column 1' in str(e):
                   time.sleep(60)
               else:
                 list3.append('')
                 done=False
    df=pd.DataFrame({'股票名称':list2,'股票代码':list1,'关注人数':list3}).set_index('股票名称')
    df.to_csv('data/stock'+t+'.csv')
    df.to_excel('data/stock'+t+'.xlsx')
              
        
        
if __name__=='__main__':
    while True:
      crawl(time.strftime('%Y_%m_%d_%H_%M_%S'))
      time.sleep(14400)
      