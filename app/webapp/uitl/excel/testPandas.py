# coding: utf-8

import pandas as pd
import numpy as np
from pandas import Series,DataFrame

def main():
    marks = pd.read_csv("/Users/yinbin/Downloads/flag-0.csv")
    print(marks)



def testS():
    s1 = Series(['刘德华', '发送', '1', 'zoo'])
    # print s1
    s2 = Series(['刘德华', '发送', '1', 'zoo'],index=[1,2,3,4])
    # print s2

    dates=pd.date_range('20180101',periods=6)
    ints=pd.interval_range(1,periods=4)
    # df = pd.DataFrame(np.random.randn(4, 4), index=ints, columns=list('ABCD'))
    df = pd.DataFrame(np.random.random_integers(1,100,10), index=ints, columns=list('ABCD'))
    print(df)

if __name__ == '__main__':
    # main()
    testS()