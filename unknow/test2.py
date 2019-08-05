#!/user/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

# /html/body/div[2]
# # body > div.main-content > ul > li:nth-child(2) > img

with open(
        'F:\WorkPlace\作业\学习资料\信安之路\零基础四周实现爬虫\课程资料\Plan-for-combating-master\week1\\1_1\\1_1code_of_video\\the_blah.html',
        'r') as  wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    # print(Soup)
    """
    图片路径
    body > div.main-content > ul > li:nth-child(1) > img
    文字
    body > div.main-content > ul > li:nth-child(1) > h3 > a
    描述
    body > div.main-content > ul > li:nth-child(1) > p 
    """
    # images = Soup.select('body > div.main-content > ul > li:nth-child(1) > img')报错
    # images = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > img')  # 改正
    #                                                               指向一个图片（删除后找到一类图片）
    images1 = Soup.select('body > div.main-content > ul > li > img')
    # print(images)
    # print(images1)
    titles = Soup.select('body > div.main-content > ul > li > h3 > a')
    describes = Soup.select('body > div.main-content > ul > li > p ')
#    print(images1, titles, describes, sep='\n--------------------------\n')

# for title in titles:
#    print(title.get_text())   查看内容

# 字典构造
info=[]
for images, title, describe in zip(images1, titles, describes):
    data = {
        'title': title.get_text(),
        'describe': describe.get_text(),
        'images': images.get('src')

    }
    print(data)
    info.append(data)


