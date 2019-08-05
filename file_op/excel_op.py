# -*- coding:utf-8 -*-
"""
@author: jim

"""

import os
import openpyxl

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



