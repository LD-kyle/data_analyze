# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:18:22 2018

@author: Jason
"""

import crawler_dongfangxaifu as cdf
import stock_analyze1 as sa
import time
import send_email_stock as ses


def main():
     while True:
         while time.strftime("%H")=='15':
             try:
                cdf.crawl()
                sa.main()
                ses.main('更新', ['data/dongfang_stock2.xlsx',
                       'data/dongfang_stock_select3.xlsx'])
             except Exception as e:
                 ses.main(e, [])                
         time.sleep(3000)
         
         
if __name__=='__main__':
    main()
    
    