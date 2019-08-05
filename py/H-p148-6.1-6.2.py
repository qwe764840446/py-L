# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name='', age=20, sex='man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if not isinstance(name, str):
            raise Exception('name must be a string')
        self.__name = name

    def setAge(self, age):
        if type(age) != int:
            raise Exception('age must be an integer')
        self.__age = age

    def setSex(self, sex):
        if sex not in ('man', 'woman'):
            raise Exception('sex must be "man" or "woman"')
        self.__sex = sex

    def show(self):
        print(self.__name, self.__age, self.__sex, sep='\n')

'''


'''
class Student(Person):
    def __init__(self, name='me', age=20, sex='man', profession='计算机科学系'):
        super(Student,self).__init__(name,age,sex)
        self.setProfession(profession)




    def setProfession(self, profession):
        if not isinstance(profession, str):
            raise Exception('profession must be a string')
        self.__profession = profession

    def show(self):
        super(Student,self).show()
        print(self.__profession)


ma=Student('陈锦明',20,'man','化学')
ma.show()
