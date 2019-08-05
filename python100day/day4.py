# -*- coding:utf-8 -*-
"""
@author: jim

"""

'''循环语句'''





#判断素数
#
def is_prime():
    from math import sqrt
    is_prime = int(input('输入正整数:'))
    if (is_prime == 2 or is_prime == 3):
        return str(is_prime)+'is prime'
    elif (is_prime % 6 != 1 and is_prime % 6 != 5):
        return str(is_prime)+'is not prime'
    else:
        sq = int(sqrt(is_prime)) + 1
        prime=True
        for i in range(1, sq):
            if (is_prime // i == 0):
                prime=False
                return str(is_prime)+'is not prime'
        if(prime):
            return str(is_prime) + 'is prime'



#打印三角形
def print_triangle():
    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()



print_triangle()