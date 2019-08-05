# -*- coding:utf-8 -*-
"""
@author: jim

"""
import re


# 自定义获取文本电子邮件的函数
def get_findAll_emails(text):
    """
    :param text: 文本
    :return: 返回电子邮件列表
    """
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return emails


if __name__ == '__main__':
    content = '123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
    emails = get_findAll_emails(text=content)
    print(emails)













