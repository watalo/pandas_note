#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/07/11 15:57:56
@Author  :   watalo 
@Version :   1.0
@Contact :   watalo@163.com
'''

import tushare as ts
import pandas as pd

#登陆tushare
pro = ts.pro_api('1bc4c4461d146a89d4eff3439af2aa231ea14de187eb1b011ee34963')

#获取上证50ETF的DateFrame
# df510050 = ts.get_hist_data('510050')
# print(df510050)
#获取上证50ETF份额数据
file_path1 = '/Users/watalo/Desktop/sz50con.xlsx'
df510050 = pd.read_excel(file_path1)

df510050['value'] = df510050['收盘价'] * df510050['份额'] # df两列相乘
df510050['合成'] = 0


# 通过读取excel文件获得成分股的代码及权重
file_path= '/Users/watalo/Desktop/sz50etf.xlsx' # excel文件地址
df_xlsx = pd.read_excel(file_path)
print(df_xlsx)

# df_name = locals() # locals()：全局的变量名称存储在这里
for i in df_xlsx['股票代码']:
    # df_name['df%s'%str(i)] = ts.get_hist_data(str(i))
    print(df_xlsx['持股数量'][df_xlsx['股票代码']==i])

    







