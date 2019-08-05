#!/user/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

id=18089
#双色球开奖期号(从18089期开始)

times=1
#用于接下来判断是否需要换行

while(id>=18001):
    url = "http://kaijiang.500.com/shtml/ssq/"+str(id)+"shtml"
    website_info = urllib.request.urlopen(url).read().decode('GBK')
    #获取也页面,完成GBK转码
    soup=BeautifulSoup(website_info,"html.parser")
    #html.parser解释器
    redballs=soup.find_all('li','ball_red')
    #获取所有li标签中class为ball_red的内容
    file=open(r'C:/User/Frank/Destop/双色球红球.txt', 'a+', encoding='utf-8')
    #要写入文件的地址
    for redball in redballs:
        if times % 6 == 0:
            redball_info = redball.string
            file.write(redball_info+"\n")
            times=times+1
            #判断本次开奖号码已经全部打印完,换行打印下一起
        else:
            redball_info=redball.string
            file.write(redball_info)
            times=times+1
    file.close()
    #关闭打开文件
    id=id-1
else:
    print("done")
    #已完成打印