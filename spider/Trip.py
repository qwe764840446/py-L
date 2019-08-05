#!/user/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

"""
print(soup)
titles=soup.select('#taplc_attraction_coverpage_attraction_0 > div > div:nth-of-type(1) > div > div > div.shelf_item_container > div:nth-of-type(1) > div.poi > div > div.item.name > a')
"""

titles = soup.select('div.item.name > a')
imgs = soup.select('img[width="200"]')
cates = soup.select('div.detail')
#print(titles, imgs, cates)
print(imgs)
for title, img, cate in zip(titles, imgs, cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings)

    }
    print(data)

