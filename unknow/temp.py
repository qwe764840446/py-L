# -*- coding:utf-8 -*-



import os
import re



def get_path():
    os.chdir('D:\\security\\WooYun漏洞、知识库收集(超详细版)\\WooYun_Bugs(漏洞库)\\test')
    path=os.getcwd()
    files = os.listdir()

    for i in files:
        isfile = os.path.splitext(i)[-1]
        if (isfile == '.html'):
            # 提取文件html的标题
            print(i)



























"""
import os
# import docx
import docx

nowdir=os.chdir('G:\\WorkPlace\\作业\\新建文件夹\\matlab作业\\0606')
print(os.getcwd())
filedir=os.listdir(nowdir)
print(filedir)
name='17551101017 劳浚铭.docx'
file=docx.Document(name)
print(len(file.paragraphs))

"""









