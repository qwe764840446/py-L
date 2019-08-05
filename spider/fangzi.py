#!/user/bin/env python
# -*- coding:utf-8 -*-
"""
标题
body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em

地址
body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span

日租金
#pricePart > div.day_l > span
#pricePart > div.day_l > span
#pricePart > div.day_l > span

第一张房源图片链接
#imgMouseCusor
#detailImageBox > div.pho_show_l > div > div:nth-child(2)
#imgMouseCusor

房东性别

名字（用if else 判断）
#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a
#floatRightBox > div.js_box.clearfix > div.w_240 > h6
body > div.wrap.clearfix.con_bg > div.con_r
<div class="day_top clearfix" id="pricePart" style="display: none;">
                 <div class="day_l">¥<span>358</span><em>起</em></div>
                 <div class="day_r">每晚</div>
             </div>
             #pricePart > div.day_l > span

"""
from bs4 import BeautifulSoup
import requests
import re

"""

def analyze(get_url):
    wb_data = requests.get(get_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4')
    address = soup.select('div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
    money = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#detailImageBox > div.pho_show_l > div.pho_show_big > div')
    name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')

    for Titles, Address, Money, Imgs, Name in zip(titles, address, money, imgs, name):
        data = {
            'Title': Titles.get_text(),
            'Address': Address.get_text(),
            'Money': Money.get_text(),
            'Img': Imgs.get('src'),
            'Name': Name.get_text()
        }
        print(data)



if __name__ == '__main__':
    get_url = "https://gz.xiaozhu.com"
    wb_data = requests.get(get_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    target = soup.find_all('li')
    a = str(target)
    resss = r'href="(.*?)"'
    mm = re.findall(resss, a, re.S | re.M)
    list1 = []
    for i in mm:
        if len(i) == 46:
            list1.append(i)
    for i in list1:
        analyze(i)

"""
#http://category.dangdang.com/cp01.31.92.00.00.00.html

def isurl(str1):
    str2 = str(str1)
    m1 = re.match(r'http:\/\/product\.dangdang\.com\/[\d]+.(html)$', str2)
    return m1


l1 = []
wb_data = requests.get("http://product.dangdang.com/25535614.html")
#soup = BeautifulSoup(wb_data.text, 'lxml')
#title=soup.title.text
#describe=soup.select('span.head_title_name')
#price=soup.select('#dd-price')








"""




data={
    'title':title,
    'describe':describe[0].text.replace(' ',''),
    'price':price[0].text.replace(' ','').replace('\\n','')
}

print(data)

title = suop.select("#component_0__0__6612 p a")
for i in title:
    a = i.get('href')
    k = isurl(a)
    if (k != None):
        l1.append(a)
"""

"""
for line in Title:
    title = re.findall(r'^title=[*]+"$', line)
    jpg = re.findall(r'^https:[*]+jpg$', line)
print(title,jpg)

wb_data = requests.get("https://gz.xiaozhu.com/huadou-duanzufang-p1-8/")
soup = BeautifulSoup(wb_data.text, 'lxml')
Title = soup.select('#page_list a')
print(Title)
#pa=re.compile(r'^https:[*]+.jpg',Title.text)
"""
