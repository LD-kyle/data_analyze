# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:49:26 2018

@author: Jason
"""

import requests
import csv
import pandas as pd
from lxml import etree
from urllib.parse import unquote
from urllib.parse import quote
import json
import re
import time
import  demjson
from bs4 import BeautifulSoup


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Apple'
                      'WebKit/537.36 (KHTML, like Gecko) Chrome/68.0.'
                      '3440.75 Safari/537.36'}


def jsonp_to_json(jsonp, jsonp_begin, jsonp_end):
    return demjson.decode(jsonp.strip()[len(jsonp_begin): -len(jsonp_end)])


def get_page(page):
    r = requests.get('http://nufm.dfcfw.com/EM_Finance2014NumericApplication'
                     '/JS.aspx?cb=jQuery112407152721447023387_1538805851727&'
                     'type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCO'
                     'IATC&js=(%7Bdata%3A%5B(x)%5D%2CrecordsFiltered%3A(tot)'
                     '%7D)&cmd=C._A&st=(ChangePercent)&sr=-1&p={}&ps=20&_=153'
                     '8805851728'.format(page), headers=headers)
    return jsonp_to_json(r.text, 'jQuery112407152721447023387_1538805851727(',
                                                    ')')
    
def get_detail(s):
    content=[]
    dict0=s['data']
    for x in dict0:
        a=x.split(',')
        content.append(a[:13] + a[14:18])
    return content
        
        
        
    
    
    

def get_money_flow(r):
    r.encoding='gbk'
    s = r.text.split('\n')
    d, f='', ''
    columns=['ReportDate', 'BasicEPS', 'NetAssetPerShare', 
             'CashFlowPerShare', 'WeightedYieldOnNetAssets',
             'ProfitsYOYRate', 'IncomeYOYRate', 'SalesGrossMargin',
             'mainBusinessIncome', 'contributionMargin', 'retainedProfits',
             'totalAssets', 'totalLiabilities', 'shareholdersEquityTotal',
             'NetCFFromOperatingActivities', 'NetCFFromInvestingActivities',
             'NetCFFromFinancingActivities', 'SumActivities']
    for x in s:
        try:
            if  'var zjlxData' in x:
                f=x.replace('var zjlxData=', '{"data":').replace(';\r', '}')
                f=json.loads(f)
            if 'var cwzyData' in x:
                d=x.replace('var cwzyData =', '{"data":').replace('\r', '}')
                d=json.loads(d)
                break
        except Exception as e:
            print(e)
    if (type(d) is dict)&(type(f) is dict):
        detail=[]
        dict0=d["data"][0]
        #for dict0 in s1:
        for column in columns:
            detail.append(dict0[column])
        for i in range(0, 3):
            detail.append(f["data"][i].split(',')[5])
        return detail
    else:
        return ['-' for i in range(0, 21)]


    
   


def get_column():
    
    url='http://data.eastmoney.com/bbsj/yjbb/300071.html'
    s=requests.Session()
    r=s.get(url,headers=headers)
    r.encoding='gbk'
    soup=BeautifulSoup(r.text, 'html.parser')
    div = soup.find_all('div', {'class': 'content'})
    trs=div[1].table.thead.find_all('tr')
    ths=trs[0].find_all('th')
    for th in ths:
        column.append(th.text.strip().replace(' ', '').
                      replace('\r', '').replace('\n', ''))


def get_data(r):
    r.encoding='gbk'
    soup=BeautifulSoup(r.text, 'html.parser')
    div = soup.find_all('div', {'class': 'box-x1 mb10'})[1]
    trs=div.div.table.tbody.find_all('tr')
    trs=div.div.table.tbody.find_all('tr', recursive=False)
    detail=[]
    for tr in trs:
        tds=tr.find_all('td')
        #detail = detail + [tuple(td.text.split('：')) for td in tds] 
        detail = detail + [td.text.split('：')[1] for td in tds]
    return detail
    

def crawl():
    content=[]
    for i in range(1, 180):
        content= content + get_detail(get_page(i))
        
    column0=['标签', '代码' , '名称' , '最新价', '涨跌额' ,'涨跌幅',
             '成交量(手)',
             '成交额(万)', '振幅', '最高', '最低', '今开', '昨收', 
             '量比', '换手率', '市盈率(动态)', '市净率']
    column1=['收益(二)', 'PE(动)', '净资产', '市净率', '营收', '营收同比',
     '净利润', '净利润同比', '毛利率', '净利率', 'ROE', '负债率', '总股本',
     '总值', '流通股', '流值', '每股未分配利润', '上市时间']
    column2=['报告时间', '基本每股收益(元)', '每股净资产(元)', 
              '每股现金流(元)', 'ROE(%)', '净利润同比(%)', 
              '营收同比率(%)', '毛利率(%)', '总营收(万)', '总利润(万)',
              '净利润(万)', '总资产(万)', '总负债(万)', 
              '股东权益合计(万)', '营业性现金流(元)', '投资性现金流(元)', 
              '融资性现金流(元)', '净现金流(元)', '今日主力净流入', 
              '5日主力净流入', '10日主力净流入']
    s=requests.Session()
    with open('data/dongfang_stock2.csv', 'w', newline='') as csvfile:
        detail_wirter = csv.writer(csvfile, dialect=csv.excel())
        detail_wirter.writerow(column0+column1+column2)
        for i in range(0, len(content)):
            x=content[i][:2]
            print(x[1])        
            #url='http://quote.eastmoney.com/sz300071.html'
            done=True
            while done:
                try:
                    if x[0]=='1':
                       r=s.get('http://quote.eastmoney.com/sh{}.'
                               'html'.format(x[1]), 
                                 headers=headers, timeout=10)
                    else:
                       r=s.get('http://quote.eastmoney.com/sz{}.'
                               'html'.format(x[1]), 
                             headers=headers, timeout=10)
                    r1 = s.get('http://data.eastmoney.com/stockdata/{}'
                           '.html'.format(x[1]), 
                              headers=headers, timeout=10)
                    time.sleep(1)
                    #content[i] = content[i] + get_detail(r) + 
                               #get_money_flow(r1)
                    detail_wirter.writerow(content[i] + get_data(r) + 
                                          get_money_flow(r1))
                    done=False
                except Exception as e:
                    print(e, x[1])
                    time.sleep(60)
                
            
       
    
    #df=pd.DataFrame(content, columns=column0+column1+column2)
    #df=df.set_index('标签')
    #df.to_csv('data/dongfang_stock2.csv',encoding='gbk')
    #df.to_excel('data/dongfang_stock2.xlsx')


if __name__=='__main__':
     crawl()
      
    
        
    
       

    