# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import math
import os

"""
@Author:yinbinhome@163.com
@Description:
@Time:2020/02/10 5:21 PM
"""
# all = pd.read_excel("/Users/yinbin/Downloads/all.xls")
dfs=[]

def read():
    df = pd.read_excel("/Users/yinbin/Downloads/bs.xls")
    df2 = pd.read_excel("/Users/yinbin/Downloads/bs-2.xls")

    # 获取最大行，最大列
    nrows = df.shape[0]
    ncols = df.columns.size
    # DataFrame(df).to_excel("/Users/yinbin/Downloads/all.xls", sheet_name='Sheet1', index=False, header=False)
    # DataFrame(df2).to_excel("/Users/yinbin/Downloads/all.xls", sheet_name='Sheet1', index=False, header=False)
    print("=========================================================================")
    print('Max Rows:' + str(nrows)+'Max Columns' + str(ncols))
    # pd.DataFrame(df)
    ds=pd.DataFrame(df2)

    dataF = df.append(ds, ignore_index=True)

    # print(dataF.size)
    # print(dataF2.size)
    dataF.to_excel("/Users/yinbin/Downloads/all.xls", sheet_name='Sheet1', index=False, header=False)

    #
    # # 遍历逐行逐列
    # for iRow in range(nrows):
    #     for iCol in range(ncols):
    #         print(df.iloc[iRow, iCol])


def appendExcel(excelFile):
    dfs.append(pd.read_excel(excelFile))


def listFiles(path):
    for i in os.listdir(path):
        path2 = os.path.join(path,i)  #拼接绝对路径
        if os.path.isdir(path2):      #判断如果是文件夹,调用本身
            listFiles(path2)
        else:
            print(path2)
            if path2.endswith('.xls'):
                dfs.append(pd.read_excel(path2))

if __name__ == '__main__':
    # path='/Users/yinbin/Downloads/药店'
    path = '/Users/yinbin/Downloads/基层医疗机构'
    # file_all = '/Users/yinbin/Downloads/all.xls'
    # df = pd.read_excel(file_all)
    listFiles(path)
    df=pd.concat(dfs)
    df.to_csv("/Users/yinbin/Downloads/all-2.csv",index=False, header=False)