# -*- coding: utf-8 -*-
# 17网络工程    17551117004 陈锦明
#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person(object):
    # 属性有姓名、年龄、性别
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    #创建方法personInfo,打印这个人的信息
    def personInfo(self):
        print("我叫%s ，年龄：%s ，性别：%s"%(self.name,self.age,self.sex))




#2、创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来。重写__str__方法，返回student的信息创建Student类，继承Person类
class Student(Person):
    #属性有学院college，班级class1
    def __init__(self, name, age, sex,college,class1):
        self.name = name
        self.age = age
        self.sex = sex
        self.college=college
        self.class1=class1

    #重写__str__方法，返回student的信息
    def __str__(self):
        return "我是一名叫做%s的学生，我的年龄是：%s，我的性别是：%s"%(self.name,self.age,self.sex)


    #重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来。
    def personInfo(self):
        Person.personInfo(self)
        print("我是%s的%s学生"%(self.college,self.class1))

    #在Student类中创建方法study，参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘YYY老师,XXX（此处填写自己姓名）终于学会了！’
    def study(self,Teacher):
        print("我是%s，%s老师%s,我终于学会了！"%(self.name,Teacher.name,Teacher.teachObj()))





#3、创建Teacher类，继承Person类，属性有学院college，专业professional
#，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序’
class Teacher(Person):
    #属性有学院college，专业professional
    def __init__(self, name, age, sex, college, professional):
        self.name = name
        self.age = age
        self.sex = sex
        self.college = college
        self.professional = professional

    #重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。
    def personInfo(self):
        print("我是来自%s的一名%s讲师"%(self.college,self.professional))
    #创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序’
    def teachObj(self):
        return "今天讲了如何使用面向对象设计程序"




#创建三个学生对象，第一个学生的名字是自己
stu1=Student('陈锦明',20,'男','计算机科学系','17网络工程')
stu2=Student('陈凯斌',20,'男','计算机科学系','17网络工程')
stu3=Student('陈若愚',20,'男','计算机科学系','17网络工程')

#分别打印其详细信息
stu1.personInfo()
stu2.personInfo()
stu3.personInfo()

#创建一个老师对象，打印其详细信息
tch=Teacher('熊燕',40,'女','计算机科学系','Python')
tch.personInfo()

#学生对象调用study方法
stu1.study(tch)
stu2.study(tch)
stu3.study(tch)



#将三个学员添加至列表中，通过循环将列表中的对象打印出来，print(Student对象)。
ll=[stu1,stu2,stu3]
for stu in ll:
    print(stu.__str__())

