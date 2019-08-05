# -*- coding:utf-8 -*-
"""
@author: jim

"""
# 水仙花数       各位数字的立方之和等于本身
def is_Narcissistic():
    from math import pow
    num = input('input an integer number judge whether is it a Narcissistic number:')
    length = len(num)
    slice1 = [pow(int(x), 3) for x in num]
    result = 0
    for x in slice1:
        result += x
    # print(slice1)
    # print(result)
    if (int(num) == result):
        print(num, 'is a Narcissistic number')
    else:
        print(num, 'is not a Narcissistic number')



#完全数
def perfertnumber():
    import math
    for num in range(1, 10000):
        sum = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:#其中一个因子
                sum += factor
                if factor > 1 and num / factor != factor:#非本身
                    sum += num / factor#另一个因子
        if sum == num:
            print(num)









if __name__ == '__main__':
    perfertnumber()












