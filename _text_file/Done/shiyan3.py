# -*- coding:utf-8 -*-
"""
@author: jim
17551117004
陈锦明
17网络工程

"""
import re

#定义字符串
str1 = 'ashdkjhask123145430jlhaskshf//\./.,][\___-lkasdf'
str2 = '_abcd'
str3 = '3=+qwe'



"""
1、判断用户输入的变量名是否合法:
 a.变量名可以由字母,数字或者下划线组成
 b.变量名只能以字母或者下划线开头
"""
# 1. a变量名可以由字母,数字或者下划线组成
pattern1 = re.compile(r'[a-z0-9_]+', re.I)
search = re.search(pattern1, str1)
a = search.group()
if (len(a) != len(str1)):
    print('contain illegal char')

# 1. b变量名只能以字母或者下划线开头
pattern2 = re.compile(r'^[a-z_]', re.I)
try:
    b = re.search(pattern2, str2).group()
except AttributeError:
    print('only start by letter or underline')
else:
    print(b)
print('#############dividing line#####################\n\n')


"""
2、输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。例
如，输入”They are students.”和”aeiou”，
则删除之后的第一个字符串变成”Thy r stdnts.”
"""
shuru1=input('please input first string\n')
shuru2=input('please input second string\n')
for i in shuru2:
    shuru1=shuru1.replace(i,'')
print(shuru1)

'''
3、输入一个字符串，分别统计出其中英文字母、空格、数字和其它字符的个数
'''
shuru3=input('please input a string\n')
num_match=re.compile(r'\d')
letter_match=re.compile(r'\w',re.I)
space_match=re.compile(r' ')
other=0
for i in shuru3:
    if(not shuru3.isalpha() and not shuru3.isspace()):
        other+=1


print('count_num:',len(re.findall(num_match,shuru3)))
print('count_letter:',len(re.findall(letter_match,shuru3)))
print('count_space:',len(re.findall(space_match,shuru3)))
print('count_otherChar:',other)



'''
4、设计一个程序，帮助小学生练习10以内的加法
       a. 随机生成加法题目;
       b.学生查看题目并输入答案;
       c.判别学生答题是否正确?
       d.退出时, 统计学生答题总数,正确数量及正确率(保留两位小数点)；
'''
import random as ra
global begin
def jisuan():
    print('begin:\n')
    a=ra.randint(0,10)
    b=ra.randint(0,10)
    print(a,'+',b,'=')
    sum=input('输入你答案：\n')
    print(sum)
    if((a+b)==int(sum)):
        print('回答正确')
    else:
        print('回答错误')
    begin=input('继续输入1，否则退出')
    return begin



print('小学生计算')
print('\t\t输入1开始\n\t\t输入q或其他退出\n')
begin=input('\n')

while(int(begin)==1):
    begin=jisuan()



'''
5、写一个正则表达式判断一个字符串是否是ip地址
规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255 
例如：255.189.10.37 正确 256.189.89.9 错误
'''
ip_str='255.189.10.37'
no_ip_str='256.189.89.9'
pattern3=re.compile("^(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|[1-9])\\."+"(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\."+"(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\."+"(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)$")
isIP=re.search(pattern3,ip_str)
noIP=re.search(pattern3,no_ip_str)
print(isIP.group(),':is an ip address')
try:
    noIP.group()
except AttributeError:
    print('this string not an ip address!')



'''
6、计算一个字符串中所有的数字的和
例如：字符串是：‘hello90abc 78sjh12.5’ 结果是90+78+12.5 = 180.5
'''
string='hello90abc 78sjh12.5'
pattern4=re.compile(r'\d+\.\d+|\d+',re.ASCII)
num=re.findall(pattern4,string)
sum1=0
print(num)
for i in num:
    k=float(i)
    sum1+=k
print(sum1)




'''
7、写一个正则表达式判断一个字符串是否电话号码
'''
string2='12345671910'
pattern5=re.compile(r'^\d+$',re.ASCII)
isphonenum=re.search(pattern5,string2)
try:
    num=isphonenum.group()
    if(len(num)==11):
        print('you phone number is:', num)
    else:
        print('not a phone number')
except AttributeError:
    print('not a phone number')





"""
8、使用正则表达式匹配合法的邮件地址
假定email地址的必要形式为： 
xxxxxx@（qq|163|126）.xxxxxx 
提取如下字符串中的合法邮件地址
y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
"""
y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
pattern6=re.compile(r'[\w]+@[qq|163|126]+\.com')
ismail=re.findall(pattern6,y)
print('legal email address contain',ismail)









