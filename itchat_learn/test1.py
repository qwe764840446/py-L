#!/user/bin/env python
# -*- coding:utf-8 -*-

import itchat
import re


itchat.login()
friends = itchat.get_friends(update=True)[0:]

def printsex():
    # 初始化计数器
    male = female = other = 0
    # friends[0]是自己的信息，所以要从friends[1]开始
    for i in friends[1:]:
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    # 计算朋友总数
    total = len(friends[1:])
    print("好友人数:", total)
    # 打印出自己的好友性别比例
    print("男性好友： %.2f%%" % (float(male) / total * 100) + "\n" +
          "女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
          "不明性别好友： %.2f%%" % (float(other) / total * 100))

def printsignature():
    for i in friends:
        # 获取个性签名
        signature = i["Signature"]
    print
    signature
    # 先全部抓取下来
    # 打印之后你会发现，有大量的span，class，emoji，emoji1f3c3等的字段，因为个性签名中使用了表情符号，这些字段都是要过滤掉的，写个正则和replace方法过滤掉

    for i in friends:
        # 获取个性签名
        signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
        # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
        rep = re.compile("1f\d.+")
        signature = rep.sub("", signature)
        print
        signature

if if __name__ == '__main__':
    printsignature()






