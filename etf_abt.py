#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   etf_abt.py
@Time    :   2020/07/11 15:14:44
@Author  :   watalo 
@Version :   1.0
@Contact :   watalo@163.com
'''

import pandas as pd
import tushare as ts


class Abt():
    def __init__(self, token):
        self.df = None
        self.token = token
        self.code_list = []
        self.df_initial()
        

    def df_initial(self):
        pro = ts.pro_api(self.token)
        self.df = ts.get_hist_data(code = self)


        
       

if __name__ == '__main__':