#!/user/bin/env python
# -*- coding:utf-8 -*-

"""
                                    知识点
                            .   匹配任意字符 除\n
                            [...]匹配字符集
                            \d / \D 匹配数字/非数字
                            \s / \S 匹配空白/非空白字符
                            \w / \W 匹配单词字符[a-zA-Z0-9] / 非单词字符
                            * 匹配前一个字符0次或无限次
                            + 匹配前一个字符1次或无限次
                            ？ 匹配前一个字符
                            {m} / {m,n} 匹配前一个字符m次或n次
                            *? / +? / ?? 匹配模式变成非贪婪(尽可能少匹配)
                            ^ 匹配字符串开头
                            $ 匹配字符串结尾
                            \A / \Z 指定字符串必须出现在开头/结尾

                            | 匹配左右任意一个表达式
                            (ab) 括号中表达式作为一个分组
                            \<number> 引用编号为num的分组匹配到的字符串
                            (?P<name>) 分组起一个别名
                            (?P=name) 引用别名为name的分组匹配字符串

search()再一个字符串中查找匹配
findall()找到匹配，返回所有匹配部分的列表
sub()将字符串中匹配正则表达式的部分替换为其他值
split()根据匹配疯字符串，返回疯字符串组成的列表
"""






"""
def find_start_imooc(fname):
    f = open(fname)
    for line in f:
       if line.startswith('imooc'):
           print(line)

#find_start_imooc('text.txt')


def find_in_imooc(fname):
    f=open(fname)
    for line in f:
        if line.startswith('imooc') and line[:-1].endswith('imooc'):#[:-1]截去换行符
            print(line)

#find_in_imooc('text.txt')

a='_value1'
a and(a[0]=='_' or 'a'<=a[0] <='z')
print(a and(a[0]=='_' or 'a'<=a[0] <='z'))

str1 = 'imooc python'
p1 = str1.find('11')
p2 = str1.find('imooc')
p3 = str1.startswith('imooc')
print(p1, p2, p3)


str1='imooc'
pa=re.compile(r'imooc')#r'imooc使用原字符串       返回一个实例pa    compile匹配的语法
ma=pa.match(str1)
print(ma.group())#s搜索到的字符会存储在group中，调用才会返回搜索到的字符串
print(ma.span())#返回索引位置
print(ma.string)#用来匹配的字符串
pa1=re.compile(r'_')
ma1=pa1.match('_value')
print(ma1.group())
print(ma1.span())



str2='imooc'
pa=re.compile(r'imooc',re.I)#re.I  I=ignorecase忽略大小写
ma=pa.match('imooc python')
ma1=pa.match('ImoOc python')
print(ma.group(),ma1.group())
pa1=re.compile(r'(imooc)',re.I)#加括号后以组的形式返回
ma2=pa1.match(str2)
print(ma2.group(),ma2.groups())


str3 = '{a0b1c2d3}'
print(ma1.group())
报错  字符数量不匹配


ma1 = re.match(r'{\[[\w]\]}', '{[a]}')


ma1 = re.match(r'{\[[\w]\]}', '{[a]}')  # 点匹配大括号里面任意数字或字符
ma2 = re.match(r'[A-Z][a-z]*', 'A')
ma3 = re.match(r'[_A-Za-z]+','_html')
ma4 = re.match(r'[1-9]?[0-9]','09')
ma5=re.match(r'[\w]{6,11}@qq.com','3049004917@qq.com')
print(ma1.group())
print(ma2.group())
print(ma3.group())
print(ma4.group())
print(ma5.group())






a1 = re.match(r'[\w]*@qq.com$', '30490041917@qq.com')
print(a1.group())
a2 = re.match(r'\Aimooc[\w]*', 'imoocpython')
print(a2.group())
a3 = re.match(r'[\w]{4,6}@(163|126).com', 'imooc@126.com')
print(a3.group())
a4 = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>abc</book>')
print(a4.group())


suoyin = str.find('1000')  # 返回索引


str = 'imooc videonum = 99956645'
str2 = 'c++=100,java=90,python=80'
info = re.search(r'\d+', str)
info1 = re.findall(r'\d+', str2)#返回的是一个包含所有找到值的列表
print(info1)
#用列表解析将info1的数字加起来
sums=sum([int(x) for x in info1])
print(sums)



替换
def addl(match):
    val=match.group()
    num=int(val)+100
    return str(num)

str3='imooc videonum = 1000'
info=re.sub(r'\d+',addl,str3)
print(info)

分割
str4='imooc:C C++ Java Python,C#'
a1=re.split(r':| |,',str4)
print(a1)





"""
