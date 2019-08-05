# -*- coding:utf-8 -*-
"""
@author: jim

"""

import os
import openpyxl
os.chdir('D:\\tmp')
print(os.getcwd())
print(os.listdir(os.getcwd()))

"""
有一个学生成绩的文件，需要你写代码把它都写到excel中，并计算出总分和平均分，
表格的抬头有：'学号','姓名','语文成绩','数学成绩','英语成绩','总分','平均分'
"""
hua = ['小花', 99, 100, 98.5]
wang = ['小王', 90, 30.5, 95]
ming = ['小明', 67.5, 49.6, 88]
json = {
    '1': hua,
    '2': wang,
    '3': ming
}
# print(json)
# os.chdir('D:\\tmp')
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

head=('学号','姓名','语文成绩','数学成绩','英语成绩','总分','平均分')

file=openpyxl.Workbook()
sheet1=file.active
#抬头信息
g=0
for i in sheet1["A:G"]:
    for cell in i:
        cell.value=head[g]
        print(cell.value)
        g+=1
#对数据进行整理
list1=[]
for i in json:
    info=[]
    info.append(i)
    info.append(json.get(i)[0])
    info.append(json.get(i)[1])
    info.append(json.get(i)[2])
    info.append(json.get(i)[3])
    info.append(info[2]+info[3]+info[4])
    info.append(info[5]/3)
    list1.append(info)

# print(list1)
#将整理好的数据插入到execl中
row=2
for i in list1:
    for k in range(1,8):
        #pos是位置每操作一次cell就往右一一个位置
        pos=chr(64+k)+str(row)
        sheet1[pos]=i[k-1]
    row+=1
#保存
file.save('py.xlsx')



"""
假设有一个英文文本文件，编写程序读取其内容，并将其中的大写字母变为小写字母，小写字母变为大写字母。
"""

string=''
with open('tmp_python.txt','w') as f:
    f.write('Wikipedia is a multilingual online encyclopedia, based on open collaboration through a wiki-based content editing system. It is the largest and most popular general reference work on the World Wide Web, and is one of the most popular websites ranked by Alexa as of June 2019.')
with open('tmp_python.txt','r+') as f:
    string = f.readline()

buff = ''
for i in string:
    if(i.islower()):
        buff+=i.upper()
    if(i.isupper()):
        buff+=i.lower()
    if(i.isspace()):
        buff+=i
print(buff)

with open('tmp_python.txt','w+') as f:
    f.write(buff)












