# -*- coding:utf-8 -*-
"""
@author: jim

"""


"""
介绍变量类型和运算符等
"""











'''day2 练习'''
#温度转换   华氏转摄氏
'''F=1.8C+32'''
F=float(input('输入华氏温度\n'))
C=(F-32)/1.8
print('%.1f华氏度 = %.1f摄氏度' %(F,C))


#半径计算周长面积
from math import pi
radius=float(input('input the radius of circle(cm)\n'))
perimeter=2*pi*radius
area=pi*(radius**2)
print('the perimeter of this circle is %.1f'%(perimeter))
print('the area of this circle is %.1f'%(area))


#判断是否闰年

year=int(input('input a year then judge whether it is a leap year\n'))
is_leap=(year%4==0 and year%100!=0 or year%400==0)
if(is_leap):
    print(str(year)+'is leap year')
else:print(str(year)+'is not leap year')

