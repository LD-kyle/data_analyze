# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:54:46 2018

@author: Jason
"""

import pandas as pd
import re



def main():
    df=pd.read_csv('data/dongfang_stock2.csv', encoding='gbk').astype(str)
    df=df.replace(to_replace=re.compile(r'.*nan.*'), value='-')
    columns=['营业性现金流(元)', '净现金流(元)', '市盈率(动态)', 
             '今日主力净流入', '5日主力净流入', '10日主力净流入', 
             '投资性现金流(元)','融资性现金流(元)' ]
    for column in columns:
        df=df[df[column]!='-']
    df[columns]=df[columns].astype(float)
    for column in columns[:-4]:
        df=df[df[column]>0]
    s=[]
    for i in range(0, len(df)): 
        a=df.iloc[i]['净利率']
        if '%' in a:
             s.append(float(a[:-1]))
        else:
             s.append(0)
    df['利率值']=s
    df[['市盈率(动态)']]=df[['市盈率(动态)']].astype(float)
    df['利率/市盈率']=df['利率值']/df['市盈率(动态)']
    df=df[df['利率/市盈率']>1]
    df.set_index('标签').to_csv('data/dongfang_stock_select2.csv', encoding='gbk')
    df=df[(df['投资性现金流(元)']>0)&(df['融资性现金流(元)']>0)]
    df.set_index('标签').to_csv('data/dongfang_stock_select3.csv', encoding='gbk')
    df.set_index('标签').to_excel('data/dongfang_stock_select3.xlsx')


if __name__=='__main__':
    main()
