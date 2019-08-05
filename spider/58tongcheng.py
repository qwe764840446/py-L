#!/user/bin/env python
# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

url='http://bj.58.com/shouji/'
#爬取手机信息
wb_data=requests.get(url)
soup=BeautifulSoup(wb_data.text,'lxml')
Title=soup.select('#infolist .t .t')
Price=soup.select('#infolist .pri')
Area=soup.select('.fl  .c_666')

















