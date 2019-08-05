#!/user/bin/env python
# -*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
def get_decode(url):
    web = requests.get(url)
    soup = BeautifulSoup(web.text, 'lxml')
    return soup
def get_url_list(soup):
    l1=[]
    link = soup.select('#infolist tr a.t')
    for i in range(len(link) - 1):
        link = soup.select('#infolist tr a.t')[i].get('href')
        l1.append(link)
    return l1
soup=get_decode('https://gz.58.com/pingbandiannao/35182410299596x.shtml')
#title=soup.title.text
#price=soup.select('#basicinfo span.infocard__container__item__main__text--price')[0].get_text
area=soup.select('//*[@id="basicinfo"]/div[3]/div[2]/div[2]/a[1]')


print(area)






"""
#https://gz.58.com/pbdn

#link=soup.select('#infolist tr a.t')[29].get('href')

#print(link)




#basicinfo > div.infocard__container.haveswitch > div:nth-child(2) > div.infocard__container__item__main > a:nth-child(1)
<a href="/baiyun/pingbandiannao/" target="_blank">白云</a>




"""