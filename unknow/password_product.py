# -*- coding: utf-8 -*-

import itertools as its
word=''
for i in range(33,127):
    word += chr(i)
#print(word)
r=its.product(word,repeat=3)

dic=open('G:\hack\弱口令字典\passwd.txt','a')
for i in r:
    dic.write(''.join(i))
    dic.write(''.join('\n'))
dic.close()

