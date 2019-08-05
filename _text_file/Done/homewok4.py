# -*- coding:utf-8 -*-
"""
@author: jim
s='This is is a desk'
print(s)
pattern=re.compile(r'[\w]+ ')
res=re.findall(pattern,s)
for i in range(1,len(res)):
    if(res[i-1]==res[i]):
        s=s.replace(res[i],'',1)
print(s)


"""
import re
q=input('\n')
print(q)
aa=q.split(' ')
for i in aa:
    if(len(i)==3):
        print(i)

"""

"""

