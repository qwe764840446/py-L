# -*- coding: utf-8 -*-

"""
1、制作趣味模板程序

  需求：等待用户输入名字、地点、爱好、根据用户的名字和爱好进行任意显示

      如：敬爱可亲的xxxx,最喜欢在xxxx地方干xxxx
"""
#name1=input('input your name\n')
#place=input('input your favioute place\n')
#hobby=input('input your hobby\n')
#print('敬爱可亲的{0},最喜欢在{1}地方干{2}'.format(name1,place,hobby))

"""
1、写代码，有如下变量，请按照要求实现每个功能
name = " gouguoQ "
a.移除name变量对应值的两边的空格，并输出移除后的内容
b.判断name变量对应的值是否以"go"开头，并输出结果
c.判断name变量对应的值是否以"Q"结尾，并输出结果
d.将name变量对应的值中的"o"，替换为"p"，并输出结果
e.将name变量对应的值根据"o"分割，并输出结果
g.将name变量对应的值变大写，并输出结果
h.将name变量对应的值变成小写，并输出结果
i.请输出name变量对应的值的第二个字符？
j.请输出name变量对应的值的前三个字符
l.请输出name变量中的值"Q的索引的位置
m.获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
name = " gouguoQ "
"""
name = " gouguoQ "

print('name_:',name)
#a
print(name.strip())
name=name.strip()

#b  True
print(name.startswith('go'))

#c  True
print(name.endswith('Q'))

#d  gpugupQ
print(name.replace('o','p'))

#e  ['g', 'ugu', 'Q']
print(name.split('o'))

#f  GOUGUOQ
print(name.upper())

#g  gouguoq
print(name.lower())

#h  o
print(name[1])

#i  gou
print(name[:3])

#j  仅不包含最后一个字符
print(name[:-1])




"""
2、请用代码实现
a.利用下划线将列表的每一个元素拼接成字符串  li = "gouguoqi"
b.利用下划线将列表的每一个元素拼接成字符串  li = ['gou', 'guo', 'qi']
"""
#a


#b  gouguoqi
str1=''
li = ['gou', 'guo', 'qi']
for i in li:
    str1=str1+i
print(str1)





"""
3 请将a字符串的数字取出，并输出成一个新的字符串。
>>> a = 'aAsmr3idd4bgs7Dlsf9eAF'
"""
#3479
a = 'aAsmr3idd4bgs7Dlsf9eAF'
str2=''
for i in a:
    if(i>='1' and i<= '9'):
        str2=str2+i
print(str2)

"""
4 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {‘a’:4,’b’:2}
a = 'aAsmr3idd4bgs7Dlsf9eAF'
"""
#{'a': 3, 's': 3, 'm': 1, 'r': 1, 'i': 1, 'd': 3, 'b': 1, 'g': 1, 'l': 1, 'f': 2, 'e': 1}
dict1={}
b = 'aAsmr3idd4bgs7Dlsf9eAF'.lower()
for i in b:
    if(i.isalpha()):
        if(i not in dict1.keys()):
            dict1.update({i:1})
        else:
            dict1[i]+=1
print(dict1)
"""
5 请去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’
"""
#aAsmr3id4bg7Dlf9eF
set1=set()
str3=''
for i in a:
    if(i not in set1):
        set1.add(i)
        str3+=i
    else:
        pass
print(str3)


"""
6请将a字符串反转并输出。例：’abc’的反转是’cba’ 
"""
str4=''
print()
