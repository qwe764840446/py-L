# -*- coding:utf-8 -*-
"""
@author: jim

验证url是否正确访问(status)
广度爬取



"""

import requests
import re


class spider():
    #属性

    url=''
    head = {
        'Host': '127.0.0.1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'close',

    }

    #功能
    def __init__(self,url):
        self.url = url

        #after test delete
        print('init..........spider class')

    def is_status_200_get(self):
        if(requests.get(self.url).status_code==200):
            return True
        else:
            return False
    def is_status_200_post(self):
        if (requests.post(self.url).status_code == 200):
            return True
        else:
            return False

    def get_page_link(self,url):
        page_source=requests.get(url).text
        print(page_source)
        regular_expression=re.compile(r'href=\"http://.*?\"')
        links=re.findall(regular_expression,page_source)
        print('***********line***********',links)


if __name__ == '__main__':
    url = 'https://www.taiyangd.com/'
    s1=spider(url)
    print(s1.is_status_200_get())
    s1.get_page_link(s1.url)