# Pandas 1.数据读取

 进行数据分析最麻烦的就是数据获取，然后一旦获得了数据，我们就可以很愉快的开始玩耍这些数据。Pandas的IO tools提供了很多的数据源的类型，但实际上，对于我这个初学者可能用的最多可能就是excel文件了。这里就需要用到pandas.read_excel()函数。

## 1.1 pandas.read_excel() 

我们先看下read_excel()的代码：

`pandas.``read_excel`**(***io***,** *sheet_name=0***,** *header=0***,** *names=None***,** *index_col=None***,** *usecols=None***,** *squeeze=False***,** *dtype=None***,** *engine=None***,** *converters=None***,** *true_values=None***,** *false_values=None***,** *skiprows=None***,** *nrows=None***,** *na_values=None***,** *keep_default_na=True***,** *verbose=False***,** *parse_dates=False***,** *date_parser=None***,** *thousands=None***,** *comment=None***,** *skipfooter=0***,** *convert_float=True***,** *mangle_dupe_cols=True***,** ***kwds***)**[[source\]](http://github.com/pandas-dev/pandas/blob/v1.0.5/pandas/io/excel/_base.py#L270-L335)[¶](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html?highlight=read_excel#pandas.read_excel)

那下面我们就来一个个的去了解这个变量的含义。

| def read_excel( | 变量                   | 含义                                            |
| :-------------- | ---------------------- | ----------------------------------------------- |
|                 | io,                    | 数据源文件，可以是url、各种文件类型基本都能适用 |
|                 | sheet_name=0,          |                                                 |
|                 | header=0,              |                                                 |
|                 | names=None,            |                                                 |
|                 | index_col=None,        |                                                 |
|                 | usecols=None,          |                                                 |
|                 | squeeze=False,         |                                                 |
|                 | dtype=None,            |                                                 |
|                 | engine=None,           |                                                 |
|                 | converters=None,       |                                                 |
|                 | true_values=None,      |                                                 |
|                 | false_values=None,     |                                                 |
|                 | skiprows=None,         |                                                 |
|                 | nrows=None,            |                                                 |
|                 | na_values=None,        |                                                 |
|                 | keep_default_na=True,  |                                                 |
|                 | verbose=False,         |                                                 |
|                 | parse_dates=False,     |                                                 |
|                 | date_parser=None,      |                                                 |
|                 | thousands=None,        |                                                 |
|                 | comment=None,          |                                                 |
|                 | skipfooter=0,          |                                                 |
|                 | convert_float=True,    |                                                 |
|                 | mangle_dupe_cols=True, |                                                 |
|                 | **kwds,                |                                                 |
|                 | ):                     |                                                 |

## 1.2 io

基本上能想到的各种类型都可以，可以是表示路径的字符串、文件、对象等等。我选择了最容易让我理解的方式，那就是指定路径的方式：

``` python
import pandas as pd 
excel_path = '/Users/watalo/Desktop/sz50con.xlsx'
# 默认读取第一张表
df1 = pd.read_excel(excel_path)
```

这里我是使用的jupyter notebook，所以创建了一个.ipynb的文件。按下Shift + Enter 得到的结果是默认的“Sheet1”的内容：

## 1.3 sheet_name

```
# 读取excel表格并进行操作
import pandas as pd 
excel_path = '/Users/watalo/Desktop/sz50con.xlsx'
# 1.1 io 读取数据源
df1 = pd.read_excel(excel_path)
df1
```

Out[30]:

|      |       日期 | 收盘价 |  净值 |  溢价率 | 指数涨幅 | 指数PB | 指数PE |    份额 | 份额增长 | 份额涨幅 |
| ---: | ---------: | -----: | ----: | ------: | -------: | -----: | -----: | ------: | -------: | -------: |
|    0 | 2020-07-10 |  3.373 | 3.380 | -0.0021 |  -0.0262 |  1.419 | 11.423 | 1648327 |   -18900 |  -0.0113 |
|    1 | 2020-07-09 |  3.459 | 3.462 | -0.0009 |   0.0035 |  1.465 | 11.818 | 1667227 |   -15300 |  -0.0091 |
|    2 | 2020-07-08 |  3.447 | 3.449 | -0.0006 |   0.0142 |  1.459 | 11.772 | 1682527 |   115020 |   0.0734 |
|    3 | 2020-07-07 |  3.402 | 3.401 |  0.0003 |   0.0023 |  1.395 | 11.628 | 1567507 |   176670 |   0.1270 |
|    4 | 2020-07-06 |  3.469 | 3.394 |  0.0221 |   0.0680 |  1.388 | 11.633 | 1390837 |    33570 |   0.0247 |
|    5 | 2020-07-03 |  3.187 | 3.179 |  0.0025 |   0.0243 |  1.255 | 10.698 | 1357267 |    25200 |   0.0189 |
|    6 | 2020-07-02 |  3.103 | 3.103 |  0.0000 |   0.0247 |  1.231 | 10.574 | 1332067 |    -2340 |  -0.0018 |
|    7 | 2020-07-01 |  3.027 | 3.029 | -0.0007 |   0.0230 |  1.199 | 10.299 | 1334407 |   -13590 |  -0.0101 |
|    8 | 2020-06-30 |  2.956 | 2.961 | -0.0017 |   0.0057 |  1.176 | 10.108 | 1347997 |     9450 |   0.0071 |
|    9 | 2020-06-29 |  2.937 | 2.937 |  0.0000 |  -0.0061 |  1.177 | 10.113 | 1338547 |     7830 |   0.0059 |
|   10 | 2020-06-24 |  2.958 | 2.956 |  0.0007 |   0.0062 |  1.184 | 10.170 | 1330717 |    -6390 |  -0.0048 |
|   11 | 2020-06-23 |  2.930 | 2.929 |  0.0003 |   0.0012 |  1.176 | 10.097 | 1337107 |    -5220 |  -0.0039 |
|   12 | 2020-06-22 |  2.924 | 2.926 | -0.0007 |  -0.0014 |  1.177 | 10.101 | 1342327 |    -5580 |  -0.0041 |
|   13 | 2020-06-19 |  2.927 | 2.930 | -0.0010 |   0.0128 |  1.162 | 10.123 | 1347907 |   -11520 |  -0.0085 |
|   14 | 2020-06-18 |  2.895 | 2.893 |  0.0007 |   0.0027 |  1.153 | 10.016 | 1359427 |    -8910 |  -0.0065 |
|   15 | 2020-06-17 |  2.881 | 2.883 | -0.0007 |   0.0007 |  1.150 | 10.005 | 1368337 |     2430 |   0.0018 |
|   16 | 2020-06-16 |  2.877 | 2.881 | -0.0014 |   0.0142 |  1.151 | 10.018 | 1365907 |     1800 |   0.0013 |
|   17 | 2020-06-15 |  2.847 | 2.841 |  0.0021 |  -0.0158 |  1.136 |  9.892 | 1364107 |     1890 |   0.0014 |
|   18 | 2020-06-12 |  2.891 | 2.885 |  0.0021 |   0.0026 |  1.075 |  9.349 | 1362217 |    -3690 |  -0.0027 |
|   19 | 2020-06-11 |  2.878 | 2.880 | -0.0007 |  -0.0110 |  1.075 |  9.350 | 1365907 |    -1530 |  -0.0011 |
|   20 | 2020-06-10 |  2.908 | 2.910 | -0.0007 |  -0.0068 |  1.086 |  9.446 | 1367437 |    -3240 |  -0.0024 |
|   21 | 2020-06-09 |  2.923 | 2.925 | -0.0007 |   0.0064 |  1.093 |  9.509 | 1370677 |   -12330 |  -0.0089 |
|   22 | 2020-06-08 |  2.905 | 2.907 | -0.0007 |   0.0046 |  1.087 |  9.459 | 1383007 |    -2430 |  -0.0018 |
|   23 | 2020-06-05 |  2.892 | 2.894 | -0.0007 |   0.0045 |  1.081 |  9.417 | 1385437 |    -5400 |  -0.0039 |
|   24 | 2020-06-04 |  2.878 | 2.881 | -0.0010 |  -0.0020 |  1.076 |  9.371 | 1390837 |    -4050 |  -0.0029 |
|   25 | 2020-06-03 |  2.884 | 2.886 | -0.0007 |   0.0011 |  1.079 |  9.405 | 1394887 |    -9450 |  -0.0067 |
|   26 | 2020-06-02 |  2.879 | 2.883 | -0.0014 |   0.0054 |  1.076 |  9.380 | 1404337 |    -5040 |  -0.0036 |
|   27 | 2020-06-01 |  2.864 | 2.868 | -0.0014 |   0.0227 |  1.069 |  9.331 | 1409377 |   -15120 |  -0.0106 |
|   28 | 2020-05-29 |  2.802 | 2.804 | -0.0007 |  -0.0011 |  1.049 |  9.162 | 1424497 |     4680 |   0.0033 |
|   29 | 2020-05-28 |  2.801 | 2.804 | -0.0011 |   0.0051 |  1.054 |  9.200 | 1419817 |     1080 |   0.0008 |
|   30 | 2020-05-27 |  2.792 | 2.790 |  0.0007 |  -0.0048 |  1.047 |  9.141 | 1418737 |   -30240 |  -0.0209 |
|   31 | 2020-05-26 |  2.802 | 2.804 | -0.0007 |   0.0069 |  1.049 |  9.156 | 1448977 |     1710 |   0.0012 |
|   32 | 2020-05-25 |  2.780 | 2.785 | -0.0018 |   0.0050 |  1.044 |  9.109 | 1447267 |     3600 |   0.0025 |
|   33 | 2020-05-22 |  2.768 | 2.771 | -0.0011 |  -0.0249 |  1.041 |  9.093 | 1443667 |    -7560 |  -0.0052 |
|   34 | 2020-05-21 |  2.838 | 2.841 | -0.0011 |  -0.0033 |  1.063 |  9.290 | 1451227 |    13500 |   0.0094 |
|   35 | 2020-05-20 |  2.849 | 2.851 | -0.0007 |  -0.0016 |  1.067 |  9.319 | 1437727 |    -6030 |  -0.0042 |
|   36 | 2020-05-19 |  2.852 | 2.855 | -0.0011 |   0.0083 |  1.067 |  9.325 | 1443757 |     4680 |   0.0033 |
|   37 | 2020-05-18 |  2.833 | 2.832 |  0.0004 |   0.0062 |  1.059 |  9.256 | 1439077 |    14040 |   0.0099 |
|   38 | 2020-05-15 |  2.812 | 2.815 | -0.0011 |  -0.0052 |  1.055 |  9.219 | 1425037 |    11430 |   0.0081 |
|   39 | 2020-05-14 |  2.831 | 2.828 |  0.0011 |  -0.0116 |  1.059 |  9.250 | 1413607 |     -720 |  -0.0005 |
|   40 | 2020-05-13 |  2.860 | 2.862 | -0.0007 |  -0.0007 |  1.070 |  9.350 | 1414327 |   -12870 |  -0.0090 |
|   41 | 2020-05-12 |  2.860 | 2.863 | -0.0010 |  -0.0008 |  1.070 |  9.351 | 1427197 |    -9090 |  -0.0063 |
|   42 | 2020-05-11 |  2.863 | 2.866 | -0.0010 |  -0.0004 |  1.074 |  9.381 | 1436287 |    -3060 |  -0.0021 |
|   43 | 2020-05-08 |  2.863 | 2.867 | -0.0014 |   0.0065 |  1.067 |  9.364 | 1439347 |     3870 |   0.0027 |
|   44 | 2020-05-07 |  2.843 | 2.841 |  0.0007 |  -0.0033 |  1.061 |  9.308 | 1435477 |      990 |   0.0007 |
|   45 | 2020-05-06 |  2.848 | 2.851 | -0.0011 |   0.0007 |  1.064 |  9.343 | 1434487 |     5490 |   0.0038 |
|   46 | 2020-04-30 |  2.852 | 2.849 |  0.0011 |   0.0060 |  1.068 |  9.035 | 1428997 |     1080 |   0.0008 |
|   47 | 2020-04-29 |  2.829 | 2.832 | -0.0011 |   0.0070 |  1.068 |  9.012 | 1427917 |   -11250 |  -0.0078 |
|   48 | 2020-04-28 |  2.810 | 2.813 | -0.0011 |   0.0071 |  1.080 |  8.924 | 1439167 |   -24840 |  -0.0170 |
|   49 | 2020-04-27 |  2.790 | 2.793 | -0.0011 |   0.0105 |  1.078 |  8.897 | 1464007 |     2700 |   0.0018 |

In [39]:

```
# 1.2 sheet_name 参数
"""
sheet_name = "Sheet1"  用表名称指定一张表
sheet_name = 1 用数字指定一张表
sheet_name = [0,"Sheet2"] 指定两种表
sheet_name = None     
"""
df2 = pd.read_excel(excel_path,sheet_name =  "Sheet1")
df2
```

Out[39]:

|      |       日期 | 收盘价 |  净值 |  溢价率 | 指数涨幅 | 指数PB | 指数PE |    份额 | 份额增长 | 份额涨幅 |
| ---: | ---------: | -----: | ----: | ------: | -------: | -----: | -----: | ------: | -------: | -------: |
|    0 | 2020-07-10 |  3.373 | 3.380 | -0.0021 |  -0.0262 |  1.419 | 11.423 | 1648327 |   -18900 |  -0.0113 |
|    1 | 2020-07-09 |  3.459 | 3.462 | -0.0009 |   0.0035 |  1.465 | 11.818 | 1667227 |   -15300 |  -0.0091 |
|    2 | 2020-07-08 |  3.447 | 3.449 | -0.0006 |   0.0142 |  1.459 | 11.772 | 1682527 |   115020 |   0.0734 |
|    3 | 2020-07-07 |  3.402 | 3.401 |  0.0003 |   0.0023 |  1.395 | 11.628 | 1567507 |   176670 |   0.1270 |
|    4 | 2020-07-06 |  3.469 | 3.394 |  0.0221 |   0.0680 |  1.388 | 11.633 | 1390837 |    33570 |   0.0247 |
|    5 | 2020-07-03 |  3.187 | 3.179 |  0.0025 |   0.0243 |  1.255 | 10.698 | 1357267 |    25200 |   0.0189 |
|    6 | 2020-07-02 |  3.103 | 3.103 |  0.0000 |   0.0247 |  1.231 | 10.574 | 1332067 |    -2340 |  -0.0018 |
|    7 | 2020-07-01 |  3.027 | 3.029 | -0.0007 |   0.0230 |  1.199 | 10.299 | 1334407 |   -13590 |  -0.0101 |
|    8 | 2020-06-30 |  2.956 | 2.961 | -0.0017 |   0.0057 |  1.176 | 10.108 | 1347997 |     9450 |   0.0071 |
|    9 | 2020-06-29 |  2.937 | 2.937 |  0.0000 |  -0.0061 |  1.177 | 10.113 | 1338547 |     7830 |   0.0059 |
|   10 | 2020-06-24 |  2.958 | 2.956 |  0.0007 |   0.0062 |  1.184 | 10.170 | 1330717 |    -6390 |  -0.0048 |
|   11 | 2020-06-23 |  2.930 | 2.929 |  0.0003 |   0.0012 |  1.176 | 10.097 | 1337107 |    -5220 |  -0.0039 |
|   12 | 2020-06-22 |  2.924 | 2.926 | -0.0007 |  -0.0014 |  1.177 | 10.101 | 1342327 |    -5580 |  -0.0041 |
|   13 | 2020-06-19 |  2.927 | 2.930 | -0.0010 |   0.0128 |  1.162 | 10.123 | 1347907 |   -11520 |  -0.0085 |
|   14 | 2020-06-18 |  2.895 | 2.893 |  0.0007 |   0.0027 |  1.153 | 10.016 | 1359427 |    -8910 |  -0.0065 |
|   15 | 2020-06-17 |  2.881 | 2.883 | -0.0007 |   0.0007 |  1.150 | 10.005 | 1368337 |     2430 |   0.0018 |
|   16 | 2020-06-16 |  2.877 | 2.881 | -0.0014 |   0.0142 |  1.151 | 10.018 | 1365907 |     1800 |   0.0013 |
|   17 | 2020-06-15 |  2.847 | 2.841 |  0.0021 |  -0.0158 |  1.136 |  9.892 | 1364107 |     1890 |   0.0014 |
|   18 | 2020-06-12 |  2.891 | 2.885 |  0.0021 |   0.0026 |  1.075 |  9.349 | 1362217 |    -3690 |  -0.0027 |
|   19 | 2020-06-11 |  2.878 | 2.880 | -0.0007 |  -0.0110 |  1.075 |  9.350 | 1365907 |    -1530 |  -0.0011 |
|   20 | 2020-06-10 |  2.908 | 2.910 | -0.0007 |  -0.0068 |  1.086 |  9.446 | 1367437 |    -3240 |  -0.0024 |
|   21 | 2020-06-09 |  2.923 | 2.925 | -0.0007 |   0.0064 |  1.093 |  9.509 | 1370677 |   -12330 |  -0.0089 |
|   22 | 2020-06-08 |  2.905 | 2.907 | -0.0007 |   0.0046 |  1.087 |  9.459 | 1383007 |    -2430 |  -0.0018 |
|   23 | 2020-06-05 |  2.892 | 2.894 | -0.0007 |   0.0045 |  1.081 |  9.417 | 1385437 |    -5400 |  -0.0039 |
|   24 | 2020-06-04 |  2.878 | 2.881 | -0.0010 |  -0.0020 |  1.076 |  9.371 | 1390837 |    -4050 |  -0.0029 |
|   25 | 2020-06-03 |  2.884 | 2.886 | -0.0007 |   0.0011 |  1.079 |  9.405 | 1394887 |    -9450 |  -0.0067 |
|   26 | 2020-06-02 |  2.879 | 2.883 | -0.0014 |   0.0054 |  1.076 |  9.380 | 1404337 |    -5040 |  -0.0036 |
|   27 | 2020-06-01 |  2.864 | 2.868 | -0.0014 |   0.0227 |  1.069 |  9.331 | 1409377 |   -15120 |  -0.0106 |
|   28 | 2020-05-29 |  2.802 | 2.804 | -0.0007 |  -0.0011 |  1.049 |  9.162 | 1424497 |     4680 |   0.0033 |
|   29 | 2020-05-28 |  2.801 | 2.804 | -0.0011 |   0.0051 |  1.054 |  9.200 | 1419817 |     1080 |   0.0008 |
|   30 | 2020-05-27 |  2.792 | 2.790 |  0.0007 |  -0.0048 |  1.047 |  9.141 | 1418737 |   -30240 |  -0.0209 |
|   31 | 2020-05-26 |  2.802 | 2.804 | -0.0007 |   0.0069 |  1.049 |  9.156 | 1448977 |     1710 |   0.0012 |
|   32 | 2020-05-25 |  2.780 | 2.785 | -0.0018 |   0.0050 |  1.044 |  9.109 | 1447267 |     3600 |   0.0025 |
|   33 | 2020-05-22 |  2.768 | 2.771 | -0.0011 |  -0.0249 |  1.041 |  9.093 | 1443667 |    -7560 |  -0.0052 |
|   34 | 2020-05-21 |  2.838 | 2.841 | -0.0011 |  -0.0033 |  1.063 |  9.290 | 1451227 |    13500 |   0.0094 |
|   35 | 2020-05-20 |  2.849 | 2.851 | -0.0007 |  -0.0016 |  1.067 |  9.319 | 1437727 |    -6030 |  -0.0042 |
|   36 | 2020-05-19 |  2.852 | 2.855 | -0.0011 |   0.0083 |  1.067 |  9.325 | 1443757 |     4680 |   0.0033 |
|   37 | 2020-05-18 |  2.833 | 2.832 |  0.0004 |   0.0062 |  1.059 |  9.256 | 1439077 |    14040 |   0.0099 |
|   38 | 2020-05-15 |  2.812 | 2.815 | -0.0011 |  -0.0052 |  1.055 |  9.219 | 1425037 |    11430 |   0.0081 |
|   39 | 2020-05-14 |  2.831 | 2.828 |  0.0011 |  -0.0116 |  1.059 |  9.250 | 1413607 |     -720 |  -0.0005 |
|   40 | 2020-05-13 |  2.860 | 2.862 | -0.0007 |  -0.0007 |  1.070 |  9.350 | 1414327 |   -12870 |  -0.0090 |
|   41 | 2020-05-12 |  2.860 | 2.863 | -0.0010 |  -0.0008 |  1.070 |  9.351 | 1427197 |    -9090 |  -0.0063 |
|   42 | 2020-05-11 |  2.863 | 2.866 | -0.0010 |  -0.0004 |  1.074 |  9.381 | 1436287 |    -3060 |  -0.0021 |
|   43 | 2020-05-08 |  2.863 | 2.867 | -0.0014 |   0.0065 |  1.067 |  9.364 | 1439347 |     3870 |   0.0027 |
|   44 | 2020-05-07 |  2.843 | 2.841 |  0.0007 |  -0.0033 |  1.061 |  9.308 | 1435477 |      990 |   0.0007 |
|   45 | 2020-05-06 |  2.848 | 2.851 | -0.0011 |   0.0007 |  1.064 |  9.343 | 1434487 |     5490 |   0.0038 |
|   46 | 2020-04-30 |  2.852 | 2.849 |  0.0011 |   0.0060 |  1.068 |  9.035 | 1428997 |     1080 |   0.0008 |
|   47 | 2020-04-29 |  2.829 | 2.832 | -0.0011 |   0.0070 |  1.068 |  9.012 | 1427917 |   -11250 |  -0.0078 |
|   48 | 2020-04-28 |  2.810 | 2.813 | -0.0011 |   0.0071 |  1.080 |  8.924 | 1439167 |   -24840 |  -0.0170 |
|   49 | 2020-04-27 |  2.790 | 2.793 | -0.0011 |   0.0105 |  1.078 |  8.897 | 1464007 |     2700 |   0.0018 |

In [40]:

```
df3 = pd.read_excel(excel_path,sheet_name =  1)
df3
```

Out[40]:

|      | 股票代码 | 股票名称 | 持股数量 |
| ---: | -------: | -------: | -------: |
|    0 |   600000 | 浦发银行 |     6000 |
|    1 |   600016 | 民生银行 |    12100 |
|    2 |   600019 | 宝钢股份 |     4500 |
|    3 |   600028 | 中国石化 |     5400 |
|    4 |   600029 | 南方航空 |     1800 |
|    5 |   600030 | 中信证券 |     4000 |
|    6 |   600036 | 招商银行 |     5300 |
|    7 |   600048 | 保利地产 |     3600 |
|    8 |   600050 | 中国联通 |     4700 |
|    9 |   600104 | 上汽集团 |     1800 |
|   10 |   600111 | 北方稀土 |     1100 |
|   11 |   600309 | 万华化学 |      200 |
|   12 |   600340 | 华夏幸福 |      600 |
|   13 |   600518 | 康美药业 |     1500 |
|   14 |   600519 | 贵州茅台 |      300 |
|   15 |   600547 | 山东黄金 |      400 |
|   16 |   600606 | 绿地控股 |     1900 |
|   17 |   600837 | 海通证券 |     4200 |
|   18 |   600887 | 伊利股份 |     3100 |
|   19 |   600919 | 江苏银行 |     3500 |
|   20 |   600958 | 东方证券 |     1600 |
|   21 |   600999 | 招商证券 |     1200 |
|   22 |   601006 | 大秦铁路 |     3000 |
|   23 |   601088 | 中国神华 |     1000 |
|   24 |   601166 | 兴业银行 |     6400 |
|   25 |   601169 | 北京银行 |     7500 |
|   26 |   601186 | 中国铁建 |     2400 |
|   27 |   601211 | 国泰君安 |     1900 |
|   28 |   601229 | 上海银行 |      500 |
|   29 |   601288 | 农业银行 |    19600 |
|   30 |   601318 | 中国平安 |     5600 |
|   31 |   601328 | 交通银行 |    14100 |
|   32 |   601336 | 新华保险 |      400 |
|   33 |   601390 | 中国中铁 |     2900 |
|   34 |   601398 | 工商银行 |    11100 |
|   35 |   601601 | 中国太保 |     1600 |
|   36 |   601628 | 中国人寿 |      900 |
|   37 |   601668 | 中国建筑 |     7700 |
|   38 |   601669 | 中国电建 |     2400 |
|   39 |   601688 | 华泰证券 |     1700 |
|   40 |   601766 | 中国中车 |     3700 |
|   41 |   601800 | 中国交建 |      800 |
|   42 |   601818 | 光大银行 |     8100 |
|   43 |   601857 | 中国石油 |     3300 |
|   44 |   601878 | 浙商证券 |      200 |
|   45 |   601881 | 中国银河 |      300 |
|   46 |   601985 | 中国核电 |     2400 |
|   47 |   601988 | 中国银行 |    10800 |
|   48 |   601989 | 中国重工 |     4500 |
|   49 |   603993 | 洛阳钼业 |     1400 |

In [41]:

```
df4 = pd.read_excel(excel_path,sheet_name =  [0,"Sheet2"])
df4
```

Out[41]:

```
{0:            日期    收盘价     净值     溢价率    指数涨幅   指数PB    指数PE       份额    份额增长  \
 0  2020-07-10  3.373  3.380 -0.0021 -0.0262  1.419  11.423  1648327  -18900   
 1  2020-07-09  3.459  3.462 -0.0009  0.0035  1.465  11.818  1667227  -15300   
 2  2020-07-08  3.447  3.449 -0.0006  0.0142  1.459  11.772  1682527  115020   
 3  2020-07-07  3.402  3.401  0.0003  0.0023  1.395  11.628  1567507  176670   
 4  2020-07-06  3.469  3.394  0.0221  0.0680  1.388  11.633  1390837   33570   
 5  2020-07-03  3.187  3.179  0.0025  0.0243  1.255  10.698  1357267   25200   
 6  2020-07-02  3.103  3.103  0.0000  0.0247  1.231  10.574  1332067   -2340   
 7  2020-07-01  3.027  3.029 -0.0007  0.0230  1.199  10.299  1334407  -13590   
 8  2020-06-30  2.956  2.961 -0.0017  0.0057  1.176  10.108  1347997    9450   
 9  2020-06-29  2.937  2.937  0.0000 -0.0061  1.177  10.113  1338547    7830   
 10 2020-06-24  2.958  2.956  0.0007  0.0062  1.184  10.170  1330717   -6390   
 11 2020-06-23  2.930  2.929  0.0003  0.0012  1.176  10.097  1337107   -5220   
 12 2020-06-22  2.924  2.926 -0.0007 -0.0014  1.177  10.101  1342327   -5580   
 13 2020-06-19  2.927  2.930 -0.0010  0.0128  1.162  10.123  1347907  -11520   
 14 2020-06-18  2.895  2.893  0.0007  0.0027  1.153  10.016  1359427   -8910   
 15 2020-06-17  2.881  2.883 -0.0007  0.0007  1.150  10.005  1368337    2430   
 16 2020-06-16  2.877  2.881 -0.0014  0.0142  1.151  10.018  1365907    1800   
 17 2020-06-15  2.847  2.841  0.0021 -0.0158  1.136   9.892  1364107    1890   
 18 2020-06-12  2.891  2.885  0.0021  0.0026  1.075   9.349  1362217   -3690   
 19 2020-06-11  2.878  2.880 -0.0007 -0.0110  1.075   9.350  1365907   -1530   
 20 2020-06-10  2.908  2.910 -0.0007 -0.0068  1.086   9.446  1367437   -3240   
 21 2020-06-09  2.923  2.925 -0.0007  0.0064  1.093   9.509  1370677  -12330   
 22 2020-06-08  2.905  2.907 -0.0007  0.0046  1.087   9.459  1383007   -2430   
 23 2020-06-05  2.892  2.894 -0.0007  0.0045  1.081   9.417  1385437   -5400   
 24 2020-06-04  2.878  2.881 -0.0010 -0.0020  1.076   9.371  1390837   -4050   
 25 2020-06-03  2.884  2.886 -0.0007  0.0011  1.079   9.405  1394887   -9450   
 26 2020-06-02  2.879  2.883 -0.0014  0.0054  1.076   9.380  1404337   -5040   
 27 2020-06-01  2.864  2.868 -0.0014  0.0227  1.069   9.331  1409377  -15120   
 28 2020-05-29  2.802  2.804 -0.0007 -0.0011  1.049   9.162  1424497    4680   
 29 2020-05-28  2.801  2.804 -0.0011  0.0051  1.054   9.200  1419817    1080   
 30 2020-05-27  2.792  2.790  0.0007 -0.0048  1.047   9.141  1418737  -30240   
 31 2020-05-26  2.802  2.804 -0.0007  0.0069  1.049   9.156  1448977    1710   
 32 2020-05-25  2.780  2.785 -0.0018  0.0050  1.044   9.109  1447267    3600   
 33 2020-05-22  2.768  2.771 -0.0011 -0.0249  1.041   9.093  1443667   -7560   
 34 2020-05-21  2.838  2.841 -0.0011 -0.0033  1.063   9.290  1451227   13500   
 35 2020-05-20  2.849  2.851 -0.0007 -0.0016  1.067   9.319  1437727   -6030   
 36 2020-05-19  2.852  2.855 -0.0011  0.0083  1.067   9.325  1443757    4680   
 37 2020-05-18  2.833  2.832  0.0004  0.0062  1.059   9.256  1439077   14040   
 38 2020-05-15  2.812  2.815 -0.0011 -0.0052  1.055   9.219  1425037   11430   
 39 2020-05-14  2.831  2.828  0.0011 -0.0116  1.059   9.250  1413607    -720   
 40 2020-05-13  2.860  2.862 -0.0007 -0.0007  1.070   9.350  1414327  -12870   
 41 2020-05-12  2.860  2.863 -0.0010 -0.0008  1.070   9.351  1427197   -9090   
 42 2020-05-11  2.863  2.866 -0.0010 -0.0004  1.074   9.381  1436287   -3060   
 43 2020-05-08  2.863  2.867 -0.0014  0.0065  1.067   9.364  1439347    3870   
 44 2020-05-07  2.843  2.841  0.0007 -0.0033  1.061   9.308  1435477     990   
 45 2020-05-06  2.848  2.851 -0.0011  0.0007  1.064   9.343  1434487    5490   
 46 2020-04-30  2.852  2.849  0.0011  0.0060  1.068   9.035  1428997    1080   
 47 2020-04-29  2.829  2.832 -0.0011  0.0070  1.068   9.012  1427917  -11250   
 48 2020-04-28  2.810  2.813 -0.0011  0.0071  1.080   8.924  1439167  -24840   
 49 2020-04-27  2.790  2.793 -0.0011  0.0105  1.078   8.897  1464007    2700   
 
       份额涨幅  
 0  -0.0113  
 1  -0.0091  
 2   0.0734  
 3   0.1270  
 4   0.0247  
 5   0.0189  
 6  -0.0018  
 7  -0.0101  
 8   0.0071  
 9   0.0059  
 10 -0.0048  
 11 -0.0039  
 12 -0.0041  
 13 -0.0085  
 14 -0.0065  
 15  0.0018  
 16  0.0013  
 17  0.0014  
 18 -0.0027  
 19 -0.0011  
 20 -0.0024  
 21 -0.0089  
 22 -0.0018  
 23 -0.0039  
 24 -0.0029  
 25 -0.0067  
 26 -0.0036  
 27 -0.0106  
 28  0.0033  
 29  0.0008  
 30 -0.0209  
 31  0.0012  
 32  0.0025  
 33 -0.0052  
 34  0.0094  
 35 -0.0042  
 36  0.0033  
 37  0.0099  
 38  0.0081  
 39 -0.0005  
 40 -0.0090  
 41 -0.0063  
 42 -0.0021  
 43  0.0027  
 44  0.0007  
 45  0.0038  
 46  0.0008  
 47 -0.0078  
 48 -0.0170  
 49  0.0018  ,
 'Sheet2':       股票代码  股票名称   持股数量
 0   600000  浦发银行   6000
 1   600016  民生银行  12100
 2   600019  宝钢股份   4500
 3   600028  中国石化   5400
 4   600029  南方航空   1800
 5   600030  中信证券   4000
 6   600036  招商银行   5300
 7   600048  保利地产   3600
 8   600050  中国联通   4700
 9   600104  上汽集团   1800
 10  600111  北方稀土   1100
 11  600309  万华化学    200
 12  600340  华夏幸福    600
 13  600518  康美药业   1500
 14  600519  贵州茅台    300
 15  600547  山东黄金    400
 16  600606  绿地控股   1900
 17  600837  海通证券   4200
 18  600887  伊利股份   3100
 19  600919  江苏银行   3500
 20  600958  东方证券   1600
 21  600999  招商证券   1200
 22  601006  大秦铁路   3000
 23  601088  中国神华   1000
 24  601166  兴业银行   6400
 25  601169  北京银行   7500
 26  601186  中国铁建   2400
 27  601211  国泰君安   1900
 28  601229  上海银行    500
 29  601288  农业银行  19600
 30  601318  中国平安   5600
 31  601328  交通银行  14100
 32  601336  新华保险    400
 33  601390  中国中铁   2900
 34  601398  工商银行  11100
 35  601601  中国太保   1600
 36  601628  中国人寿    900
 37  601668  中国建筑   7700
 38  601669  中国电建   2400
 39  601688  华泰证券   1700
 40  601766  中国中车   3700
 41  601800  中国交建    800
 42  601818  光大银行   8100
 43  601857  中国石油   3300
 44  601878  浙商证券    200
 45  601881  中国银河    300
 46  601985  中国核电   2400
 47  601988  中国银行  10800
 48  601989  中国重工   4500
 49  603993  洛阳钼业   1400}
```

In [43]:

```
df5 = pd.read_excel(excel_path,sheet_name =  None)
df5
```

Out[43]:

```
{'Sheet1':            日期    收盘价     净值     溢价率    指数涨幅   指数PB    指数PE       份额    份额增长  \
 0  2020-07-10  3.373  3.380 -0.0021 -0.0262  1.419  11.423  1648327  -18900   
 1  2020-07-09  3.459  3.462 -0.0009  0.0035  1.465  11.818  1667227  -15300   
 2  2020-07-08  3.447  3.449 -0.0006  0.0142  1.459  11.772  1682527  115020   
 3  2020-07-07  3.402  3.401  0.0003  0.0023  1.395  11.628  1567507  176670   
 4  2020-07-06  3.469  3.394  0.0221  0.0680  1.388  11.633  1390837   33570   
 5  2020-07-03  3.187  3.179  0.0025  0.0243  1.255  10.698  1357267   25200   
 6  2020-07-02  3.103  3.103  0.0000  0.0247  1.231  10.574  1332067   -2340   
 7  2020-07-01  3.027  3.029 -0.0007  0.0230  1.199  10.299  1334407  -13590   
 8  2020-06-30  2.956  2.961 -0.0017  0.0057  1.176  10.108  1347997    9450   
 9  2020-06-29  2.937  2.937  0.0000 -0.0061  1.177  10.113  1338547    7830   
 10 2020-06-24  2.958  2.956  0.0007  0.0062  1.184  10.170  1330717   -6390   
 11 2020-06-23  2.930  2.929  0.0003  0.0012  1.176  10.097  1337107   -5220   
 12 2020-06-22  2.924  2.926 -0.0007 -0.0014  1.177  10.101  1342327   -5580   
 13 2020-06-19  2.927  2.930 -0.0010  0.0128  1.162  10.123  1347907  -11520   
 14 2020-06-18  2.895  2.893  0.0007  0.0027  1.153  10.016  1359427   -8910   
 15 2020-06-17  2.881  2.883 -0.0007  0.0007  1.150  10.005  1368337    2430   
 16 2020-06-16  2.877  2.881 -0.0014  0.0142  1.151  10.018  1365907    1800   
 17 2020-06-15  2.847  2.841  0.0021 -0.0158  1.136   9.892  1364107    1890   
 18 2020-06-12  2.891  2.885  0.0021  0.0026  1.075   9.349  1362217   -3690   
 19 2020-06-11  2.878  2.880 -0.0007 -0.0110  1.075   9.350  1365907   -1530   
 20 2020-06-10  2.908  2.910 -0.0007 -0.0068  1.086   9.446  1367437   -3240   
 21 2020-06-09  2.923  2.925 -0.0007  0.0064  1.093   9.509  1370677  -12330   
 22 2020-06-08  2.905  2.907 -0.0007  0.0046  1.087   9.459  1383007   -2430   
 23 2020-06-05  2.892  2.894 -0.0007  0.0045  1.081   9.417  1385437   -5400   
 24 2020-06-04  2.878  2.881 -0.0010 -0.0020  1.076   9.371  1390837   -4050   
 25 2020-06-03  2.884  2.886 -0.0007  0.0011  1.079   9.405  1394887   -9450   
 26 2020-06-02  2.879  2.883 -0.0014  0.0054  1.076   9.380  1404337   -5040   
 27 2020-06-01  2.864  2.868 -0.0014  0.0227  1.069   9.331  1409377  -15120   
 28 2020-05-29  2.802  2.804 -0.0007 -0.0011  1.049   9.162  1424497    4680   
 29 2020-05-28  2.801  2.804 -0.0011  0.0051  1.054   9.200  1419817    1080   
 30 2020-05-27  2.792  2.790  0.0007 -0.0048  1.047   9.141  1418737  -30240   
 31 2020-05-26  2.802  2.804 -0.0007  0.0069  1.049   9.156  1448977    1710   
 32 2020-05-25  2.780  2.785 -0.0018  0.0050  1.044   9.109  1447267    3600   
 33 2020-05-22  2.768  2.771 -0.0011 -0.0249  1.041   9.093  1443667   -7560   
 34 2020-05-21  2.838  2.841 -0.0011 -0.0033  1.063   9.290  1451227   13500   
 35 2020-05-20  2.849  2.851 -0.0007 -0.0016  1.067   9.319  1437727   -6030   
 36 2020-05-19  2.852  2.855 -0.0011  0.0083  1.067   9.325  1443757    4680   
 37 2020-05-18  2.833  2.832  0.0004  0.0062  1.059   9.256  1439077   14040   
 38 2020-05-15  2.812  2.815 -0.0011 -0.0052  1.055   9.219  1425037   11430   
 39 2020-05-14  2.831  2.828  0.0011 -0.0116  1.059   9.250  1413607    -720   
 40 2020-05-13  2.860  2.862 -0.0007 -0.0007  1.070   9.350  1414327  -12870   
 41 2020-05-12  2.860  2.863 -0.0010 -0.0008  1.070   9.351  1427197   -9090   
 42 2020-05-11  2.863  2.866 -0.0010 -0.0004  1.074   9.381  1436287   -3060   
 43 2020-05-08  2.863  2.867 -0.0014  0.0065  1.067   9.364  1439347    3870   
 44 2020-05-07  2.843  2.841  0.0007 -0.0033  1.061   9.308  1435477     990   
 45 2020-05-06  2.848  2.851 -0.0011  0.0007  1.064   9.343  1434487    5490   
 46 2020-04-30  2.852  2.849  0.0011  0.0060  1.068   9.035  1428997    1080   
 47 2020-04-29  2.829  2.832 -0.0011  0.0070  1.068   9.012  1427917  -11250   
 48 2020-04-28  2.810  2.813 -0.0011  0.0071  1.080   8.924  1439167  -24840   
 49 2020-04-27  2.790  2.793 -0.0011  0.0105  1.078   8.897  1464007    2700   
 
       份额涨幅  
 0  -0.0113  
 1  -0.0091  
 2   0.0734  
 3   0.1270  
 4   0.0247  
 5   0.0189  
 6  -0.0018  
 7  -0.0101  
 8   0.0071  
 9   0.0059  
 10 -0.0048  
 11 -0.0039  
 12 -0.0041  
 13 -0.0085  
 14 -0.0065  
 15  0.0018  
 16  0.0013  
 17  0.0014  
 18 -0.0027  
 19 -0.0011  
 20 -0.0024  
 21 -0.0089  
 22 -0.0018  
 23 -0.0039  
 24 -0.0029  
 25 -0.0067  
 26 -0.0036  
 27 -0.0106  
 28  0.0033  
 29  0.0008  
 30 -0.0209  
 31  0.0012  
 32  0.0025  
 33 -0.0052  
 34  0.0094  
 35 -0.0042  
 36  0.0033  
 37  0.0099  
 38  0.0081  
 39 -0.0005  
 40 -0.0090  
 41 -0.0063  
 42 -0.0021  
 43  0.0027  
 44  0.0007  
 45  0.0038  
 46  0.0008  
 47 -0.0078  
 48 -0.0170  
 49  0.0018  ,
 'Sheet2':       股票代码  股票名称   持股数量
 0   600000  浦发银行   6000
 1   600016  民生银行  12100
 2   600019  宝钢股份   4500
 3   600028  中国石化   5400
 4   600029  南方航空   1800
 5   600030  中信证券   4000
 6   600036  招商银行   5300
 7   600048  保利地产   3600
 8   600050  中国联通   4700
 9   600104  上汽集团   1800
 10  600111  北方稀土   1100
 11  600309  万华化学    200
 12  600340  华夏幸福    600
 13  600518  康美药业   1500
 14  600519  贵州茅台    300
 15  600547  山东黄金    400
 16  600606  绿地控股   1900
 17  600837  海通证券   4200
 18  600887  伊利股份   3100
 19  600919  江苏银行   3500
 20  600958  东方证券   1600
 21  600999  招商证券   1200
 22  601006  大秦铁路   3000
 23  601088  中国神华   1000
 24  601166  兴业银行   6400
 25  601169  北京银行   7500
 26  601186  中国铁建   2400
 27  601211  国泰君安   1900
 28  601229  上海银行    500
 29  601288  农业银行  19600
 30  601318  中国平安   5600
 31  601328  交通银行  14100
 32  601336  新华保险    400
 33  601390  中国中铁   2900
 34  601398  工商银行  11100
 35  601601  中国太保   1600
 36  601628  中国人寿    900
 37  601668  中国建筑   7700
 38  601669  中国电建   2400
 39  601688  华泰证券   1700
 40  601766  中国中车   3700
 41  601800  中国交建    800
 42  601818  光大银行   8100
 43  601857  中国石油   3300
 44  601878  浙商证券    200
 45  601881  中国银河    300
 46  601985  中国核电   2400
 47  601988  中国银行  10800
 48  601989  中国重工   4500
 49  603993  洛阳钼业   1400}
```

In [ ]:

```
 
```

