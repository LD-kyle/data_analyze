# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 23:09:18 2018

@author: Administrator
"""

import numpy as np
import pandas as pd

# import package for upload data to mysql
import pymysql
from sqlalchemy import *


# database setting

user_SQL = 'likai'
pass_SQL = '2017422100'
host = 'rm-2ze86u1j19c151g4dmo.mysql.rds.aliyuncs.com:3306/'
database = 'lk_test'

tablename_announce = 'scw'       # 公告
common_col_announce = 'scw.产品型号'
tablename_evpromot = 'tablename_evpromot'       # 新能源汽车推广应用推荐车型目录
common_col_evpromot = 'tablename_evpromot.产品型号_X'
tablename_taxfree = 'tablename_taxfree'        # 新能源汽车免征购置税目录
common_col_taxfree ='tablename_taxfree.车辆型号_M'

SQLengine = 'mysql+pymysql://' + user_SQL + ':' + pass_SQL + '@'+ host + database + '?charset=utf8'

engine = create_engine(SQLengine,echo=True)

df_evpromot= pd.read_sql_query('SELECT * FROM '+ tablename_evpromot,engine).set_index('企业_X')
df_evpromot.to_csv('data/tablename_evpromot.csv')
#df_taxfree= pd.read_sql_query('SELECT * FROM '+ tablename_taxfree,engine).set_index('车辆型号_M')
#df_taxfree.to_csv('tablename_taxfree.csv')
#df_announce= pd.read_sql_query('SELECT * FROM '+ tablename_announce,engine).set_index('企业名称')
#df_announce.to_csv('tablename_announce.csv')
def main():
   df=pd.read_sql_query('SELECT * FROM '+ tablename_announce+' WHERE (产品名称 LIKE "%%乘用车%%" or 产品名称 LIKE "%%轿车%%") and (产品名称 LIKE "%%纯电动%%")'
                                  ,engine)
   for i in range(0, len(df.columns)):
             df.rename(columns={df.columns[i]: df.columns[i]+'_G'}, inplace=True)
   df.set_index('企业名称_G').to_csv('data/table_announce_ev.csv')
   df=pd.read_sql_query('SELECT * FROM '+ tablename_evpromot+' WHERE (类型_X LIKE "%%乘用车%%" or 类型_X LIKE "%%轿车%%") and (类型_X  LIKE "%%纯电动%%")'
                                  ,engine).set_index('企业_X')
   df.to_csv('data/table_evpromot_ev.csv')

main()
#writer = pd.ExcelWriter('table_announce_cut.xls')
#df_announce_cut.to_excel(writer)
#writer.save()
#sea.main('table_announce_cut.xls')

