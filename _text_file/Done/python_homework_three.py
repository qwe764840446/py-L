# -*- coding: utf-8 -*-
import random


def my_sorted(l):
    '''    下面为最简单的冒泡排序    '''
    for i in range(0, len(l) - 1):
        for k in range(i + 1, len(l)):
            if (l[i] > l[k]):
                temp = l[i]
                l[i] = l[k]
                l[k] = temp
    return l


'''用随机数来生成要排序的列表'''
list1 = []
list2 = []
for i in range(0, 10):
    list1.append(random.randint(0, 100))
    list2.append(random.randint(0, 100))

print(list1)
print(my_sorted(list1))
print('👆👆👆👆👆👆👆👆👆👆list1的排序👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆\n')
print(list2)
my_sorted(list2)
print(list2)
print('👆👆👆👆👆👆👆👆👆👆list2的排序👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆\n\n')


def my_reversed(v):
    '''从序列中的最后一个元素开始将元素放进新的列表，并返回这个列表'''
    v_len = len(v)
    list_t = []
    for i in range(0, v_len):
        list_t.append(v[v_len - i - 1])
    return list_t


print(list1)
my_reversed(list1)
print(my_reversed(list1))
print('👆👆👆👆👆👆👆👆👆list1的倒序序👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆\n')
print(list2)
my_reversed(list2)
print(my_reversed(list2))
print('👆👆👆👆👆👆👆👆👆list2的倒序序👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆\n')
