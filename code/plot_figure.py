# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:00:31 2018

@author: Administrator
"""

import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go


def plot_pie(df):
    list0=list(df['2018-7'].values)
    list0.sort()
    values=[sum(list0[:-10])]+list0[-10:]
    df=df.reset_index()
    df=df.set_index('2018-7')
    labels=['其他']+[df.loc[x,'车型']  for x in values[1:]]
    plt.pie(values, labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=140)
    plt.savefig('img/test.jpg')
    #trace = go.Pie(labels=labels, values=values)
    #py.iplot([trace], filename='basic_pie_chart')



def get_violin_data1(names,data,title):
    sns.set_style("darkgrid",{"font.sans-serif":['simhei', 'Arial']})
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
    plot=sns.barplot(x="time", y="sales", data=data,ax=axes).set_title(title)
    fig=plot.get_figure()
    fig.savefig('img/'+title+'.jpg')

def main():
    df=pd.read_csv('data/sales_ev.csv',index_col='车型')
    df=df.drop(['长安逸动混动'])
    plot_pie(df)
    df['类型']='纯电动'
    df1=df.groupby('类型').sum()
    n=list(df1.iloc[0][7:])
    n.reverse()
    times=['2016年','2017年','2018年']
    df2=pd.DataFrame({'time':times,'sales':n})
    get_violin_data1(times,df2,'搜狐纯电动汽车销量')

if __name__=='__main__':
    main()
  