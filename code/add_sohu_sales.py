# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:32:51 2018

@author: Administrator
"""

import pandas as pd 
import re

def main():

   df=pd.read_csv('data/sales_ev.csv',index_col='车型')
   df1=pd.read_csv('data/sales_ev_par.csv')
   df2=pd.read_csv('data/table_announce_ev_change.csv')
   columns=['车型_S','售价(万)_S','销量2018-7_S', '销量2018-6_S', '销量2018-5_S', '销量2018-4_S', 
         '销量2018-3_S', '销量2018-2_S','销量2018年_S', '销量2017年_S', '销量2016年_S']
   columns1=df.columns[1:]
   for column in columns:
        df2[column]=''
   models=list(set(df1['车型'].values))
   for model in models:
       s=df.loc[model] 
       df11=df1[(df1['车型']==model)&(df1['整备质量'].notna())]
       #df2[(df2['整车长_G_Max']==df11.iloc[1]['长度(mm)'])&(df2['整车宽_G_Max']==df11.iloc[1]['宽度(mm)'])&(df2['整车高_G_Max']==df11.iloc[1]['高度(mm)'])&((df2['最高车速(km/h)_G_Max']==df11.iloc[0]['最高车速']))]
       for i in range(0,len(df11)):
           df3=df2[(df2['整车长_G_Max']==df11.iloc[i]['长度(mm)'])&
                (df2['整车宽_G_Max']==df11.iloc[i]['宽度(mm)'])&
                (df2['整车高_G_Max']==df11.iloc[i]['高度(mm)'])&
                (df2['整备质量(kg)_G_Max']==max([float(x) for x in re.findall(r'\d+?\d*',df11.iloc[i]['整备质量'])]))&
                (df2['轴距(mm)_G_Max']==df11.iloc[i]['轴距(mm)'])]
           try:
              for x in df3.index:
                   df2.loc[x,'售价(万)_S']=df2.loc[x,'售价(万)_S']+df11.iloc[i]['款式']+': '+str(df11.iloc[i]['售价'])+'\n'
                   if df2.loc[x,'车型_S']=='':
                       df2.loc[x,'车型_S']=model
                       for column in columns1:
                           df2.loc[x,'销量'+column+'_S']=s[column]
           except Exception as e:
                print(e,x)                   

   df2.set_index('企业名称_G').to_csv('data/table_merge.csv')
   df_c=df2[df2['车型_S']!='']
   df_c.set_index('企业名称_G').to_csv('data/table_merge_cut.csv')
   #df2.set_index('企业名称_G').to_excel('data/table_merge_ev_cut_change_cal.xlsx')
if __name__=='__main__':
    main()
