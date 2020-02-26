# -*- coding: utf-8 -*-

import os,stat
import urllib.request


"""
@Author:yinbinhome@163.com
@Description:
@Time:2020/01/07 1:18 PM
"""

# 下载存放路径，不存在创建目录
file_path = '/Users/yinbin/Desktop/temp/2.23/'

# 下载链接数组
urls=[
'http://saas-oss.jiuruys.com/rest/crm/oss/contract/downloadUrl?flowId=821019b7a63345199cf7a46443257f87',
'http://saas-oss.jiuruys.com/rest/crm/oss/contract/downloadUrl?flowId=f3bb9858d0ab49848b94a16257242c78',
'http://saas-oss.jiuruys.com/rest/crm/oss/contract/downloadUrl?flowId=229eba8fba8d4b06890cadbc6d188d74',
'http://saas-oss.jiuruys.com/rest/crm/oss/contract/downloadUrl?flowId=4b8ece484e34407098970f8f90e67cc3',
'http://saas-oss.jiuruys.com/rest/crm/oss/contract/downloadUrl?flowId=b141dcb545944d4daa5830e1702f9da7'
]

# 是否有这个路径
if not os.path.exists(file_path):
    # 创建路径
    os.makedirs(file_path)

def loopDown(urls):
    print("开始下载ing")
    cnt=1
    for url in urls:
        print("第" + str(cnt) + "个开始下载")
        print(url)
        downDPF(url,cnt)
        cnt=cnt+1

    print("下载结束.")



def downDPF(url,num):
    try:
        # 拼接文件名（包含路径）
        fname=str(url).split('=')[1]
        filename=file_path+os.sep+fname+'.pdf'
        #print(filename)
        # 下载文件，并保存到文件夹中
        urllib.request.urlretrieve(url, filename=filename)

    except IOError as e:
        print("IOError")
    except Exception as e:
        print("发生异常Exception")

if __name__ == '__main__':
    loopDown(urls)
