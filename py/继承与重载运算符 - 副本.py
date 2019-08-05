# -*- coding: utf-8 -*-
class Employee:
    def __init__(self,name,age,salary):
        print('Created a class:',self.__class__)
        self.name=name
        self.age=age
        self.salary=salary
    def getter_name(self):
        return self.name
    def getter_age(self):
        return self.age
    def getIncome(self):
        return self.salary
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_salary(self,salary):
        self.salary=salary


class Manager(Employee):
    def __init__(self,name,age,salary,bouns):
        print('Created a class:',self.__class__)
        self.name=name
        self.age=age
        self.salary=salary
        self.bouns=bouns
    def set_bouns(self,bouns):
        self.bouns=bouns
    def getter_bouns(self):
        return self.bouns




class Mylist:  #定义类Mylist
    __mylist = []

    def __init__(self,*args):
        self.mylist = []
        for arg in args:
            self.__mylist.append(arg)

    def __add__(self,x):   #定义操作+
        for i in range(0,len(self.__mylist)):  #依次遍历列表，执行加操作
            self.__mylist[i] = self.__mylist[i]+x
        return self.__mylist

    def __sub__(self,x):
        for i in range(0, len(self.__mylist)):  # 依次遍历列表，执行加操作
            self.__mylist[i] = self.__mylist[i] - x
        return self.__mylist

    def __mul__(self,x):
        for i in range(0, len(self.__mylist)):  # 依次遍历列表，执行加操作
            self.__mylist[i] = self.__mylist[i] * x
        return self.__mylist
     def __div__(self,x):
         for i in range(0, len(self.__mylist)):  # 依次遍历列表，执行加操作
             self.__mylist[i] = self.__mylist[i] / x
         return self.__mylist
     def __mod__(self,x):
         for i in range(0, len(self.__mylist)):  # 依次遍历列表，执行加操作
             self.__mylist[i] = self.__mylist[i] % x
         return self.__mylist
     def __pow__(self,x):
         for i in range(0, len(self.__mylist)):  # 依次遍历列表，执行加操作
             self.__mylist[i] = self.__mylist[i] ** x
         return self.__mylist
     def show(self):   #显示列表中的数值
        print(self.__mylist)