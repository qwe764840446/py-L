# -*- coding: utf-8 -*-
class Employee:
    def __init__(self,name,age,salary):#初始化
        print('Created a class:',self.__class__)#打印类名字
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


class Manager(Employee):#继承了Employee类的所有方法
    def __init__(self,name,age,salary,bouns):#重载初始化方法增加bouns属性
        print('Created a class:',self.__class__)
        self.name=name
        self.age=age
        self.salary=salary
        self.bouns=bouns
    def set_bouns(self,bouns):
        self.bouns=bouns
    def getter_bouns(self):
        return self.bouns
#下面测试所有类方法是否正确
print("#############    This is a test    ##################\n\n")
xiaozhang=Employee('xiaozhang',20,1000)
print('get my name',xiaozhang.getter_name())
print('get my age',xiaozhang.getter_age())
print('get my salary',xiaozhang.getIncome())
print('set my name',xiaozhang.set_name('person'))
print('set my age',xiaozhang.set_age(21))
print('set my salary',xiaozhang.set_salary(2000))
print('after set my name my name is:',xiaozhang.getter_name())
print('after set my my age is:',xiaozhang.getter_age())
print('after set my salary my salary is:',xiaozhang.getIncome())
print('')



laoban=Manager('laoban',50,300000,10000)
print('get my name',laoban.getter_name())
print('get my age',laoban.getter_age())
print('get my salary',laoban.getIncome())
print('get my bouns',laoban.getter_bouns())
print('set my name',laoban.set_name('boss'))
print('set my age',laoban.set_age(51))
print('set my salary',laoban.set_salary(20000))
print('set my bouns',laoban.set_bouns(10000))
print('after set my name my name is:',laoban.getter_name())
print('after set my my age is:',laoban.getter_age())
print('after set my salary my salary is:',laoban.getIncome())
print('after set my my bouns is:',laoban.getter_bouns())
print('')





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

list1=Mylist(1,2,3,4,5,6,7,8,9,10)
yy=list1.__add__(10)
print(yy)








"""
	请编写一个职工类Employee，要求其包含name、age和salary（月薪），并且完成相应getter、setter方法和获得收入getIncome的方法与构造器。职工的收入就是工资。
	请编写一个经理类Manager，要求其包含name、age和salary（月薪）、bonus（奖金），并且完成获得收入等的方法与构造器。


重载运算符

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
        pass

    def __mul__(self,x):
        pass
     def __div__(self,x):
        pass
     def __mod__(self,x):
        pass
     def __pow__(self,x):
        pass
     def show(self):   #显示列表中的数值
        print(self.__mylist)

if __name__ == '__main__':   #通过name的内置属性
    l = Mylist(1,2,3,4,5)  #定义一个列表对象
    l+10
l.show()


"""