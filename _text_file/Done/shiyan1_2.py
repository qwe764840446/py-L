# -*- coding: utf-8 -*-
import math
sqrt=math.sqrt

def isprime(i):
    if(i ==2 or i==3 ):
        return True
    if(int(i%6)!= 1 and int(i%6)!= 5):
        return False
    tmp=sqrt(i)
    for k in range(5,int(tmp),6):
        if(int(i%k)==0 or int(i%(k+2))==0):
            return False
    return True


for i in range(101,200):
    if(isprime(i)):
        print(i)