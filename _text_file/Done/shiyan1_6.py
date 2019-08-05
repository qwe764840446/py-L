# -*- coding: utf-8 -*-
for i in range(101,201):
    a=2
    while a<i: #
        if i%a==0:break
        else:a=a+1
    if a==i:
        print(i)