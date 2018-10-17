# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:52:39 2018

@author: Administrator
"""

import pandas as pd
import re
import numpy as np


def main():
    df=pd.read_csv('data/table_merge.csv')
    df1=df[df['车型_S'].notna()]
    for x in df1.index:
        s=re.findall('\d+\.+?\d*',df.loc[x,'售价(万)_S'])
        s=[float(i) for i in s]
        df.loc[x,'车系配置数量_S']=len(s)
        df.loc[x,'最低价格匹配(万)_S']=min(s)
        df.loc[x,'最高价格匹配(万)_S']=max(s)
        df.loc[x,'平均价(万)_S']=np.mean(s)
    df.to_csv('data/table_merge_change.csv')
    df.to_excel('data/table_merge_change.xlsx')
  
if __name__=='__main__':
    main()
