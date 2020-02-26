# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

"""
@Author:yinbinhome@163.com
@Description:
@Time:2020/02/10 4:58 PM
"""

def read():
    df = pd.read_excel("/Users/yinbin/Downloads/bs.xls")
    print(df)
    # 获取最大行，最大列
    nrows = df.shape[0]
    ncols = df.columns.size

    print("=========================================================================")
    print('Max Rows:' + str(nrows))
    print('Max Columns' + str(ncols))

    # 显示列名，以列表形式显示
    print(df.columns)

    # 显示列名，并显示列名的序号
    for iCol in range(ncols):
        print(str(iCol) + ':' + df.columns[iCol])

    # 列出特定行列，单元格的值
    print(df.iloc[0, 0])
    print(df.iloc[0, 1])

    print("=========================================================================")

    # 查看某列内容
    # sColumnName='fd1'
    print(df['标题名称'])

    # 查看第3列的内容，列的序号从0开始
    sColumnName = df.columns[2]
    print(df[sColumnName])

    print('=====================================*****==================================')
    # 查看某行的内容
    iRow = 1
    for iCol in range(ncols):
        print(df.iloc[iRow, iCol])

    # 遍历逐行逐列
    for iRow in range(nrows):
        for iCol in range(ncols):
            print(df.iloc[iRow, iCol])

    print('=====================================End==================================')

if __name__ == '__main__':
    read()