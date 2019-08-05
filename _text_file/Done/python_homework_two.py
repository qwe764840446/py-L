#!/user/bin/env python
# -*- coding:utf-8 -*-


"""
    定义一个判断输入是否是数字的函数
            是返回True
            否返回False
"""
def isnumber(string):
    if (string >= '1' and string <= '9'):
        return True
    else:
        return False


""" 
    将用户输入的字符串放进列表
"""
list1 = list(input('输入列表\n'))


""" 
    用户输入的所有字符都会存在列表中
    将一些没有用的字符移除过滤一下
"""
list1.remove('[')
list1.remove(']')
while (',' in list1):
    list1.remove(',')


""" 
    列表里的全是字符
    需要对所有字符转换为数字
    利用map函数进行批量修改
"""
list2 = map(int, list1)


"""
    list2只是一个迭代对象
    需要用list函数将其实现
"""
list3 = list(list2)


"""
    silce1列表与list1类似
"""
slice1 = list(input('输入两个数字'))
slice1.remove('、')


"""
    此时要用上面定义的函数对slice1接收到的数字进行合法性检测
    非数字这不能进行切片操作
"""
if (isnumber(slice1[0]) and isnumber(slice1[1])):
    print('切片结果：', list3[int(slice1[0]):int(slice1[1]) + 1])
else:
    print('输入错误')

"""



"""





"""导入两个包方便创建随机字典"""
import random
import string

"""
    因为键是不能够重复的所以用集合接收随机的字符

"""
set1 = set(random.choice(string.ascii_letters) for i in range(10))

"""
    键值是可以重复，用列表或元祖接收都可以
"""
list1 = list(random.choice(string.ascii_letters + string.digits) for i in range(10))

"""
    用上面的集合和列表创建一个字典
"""
dict1 = dict(zip(set1, list1))

print(dict1)

keys = input('input you key:\n')
if (keys in dict1):
    print('this keys\'value is:', dict1.get(keys))
else:
    print('you keys is not exist!')

















