# -*- coding:utf-8 -*-

import pymysql
from sql_injection import global_value as GLOBAL_VALUE


db=pymysql.connect(GLOBAL_VALUE.DB_ADDRESS_IP,GLOBAL_VALUE.DB_USERNAME,\
                   GLOBAL_VALUE.DB_PASSWORD,GLOBAL_VALUE.DB_DATABASES)#开连接
cursor=db.cursor()#创建一个执行命令的对象
cursor.execute('show databases')#命令
data=cursor.fetchall()#取出查询结果
print(data)

cursor.execute('use dvwa')
cursor.execute('show tables')
print(cursor.fetchall())

cursor.execute('show columns from users')
print(cursor.fetchall())

cursor.execute('select * from users;')
print(cursor.fetchall())


print('\n\n\n\n','显示数据库结构内容','\n\n\n\n')
print('创建插入数据')


sql_database_create="""create database if not exists python_connect_test character set utf8"""
ll=cursor.execute(sql_database_create)
print(type(ll))
cursor.execute('show databases')
print(cursor.fetchall())

cursor.execute('use python_connect_test')
sql_table_cerate="""create table addresses(
id_key int primary key auto_increment,
address varchar (50),
data1 varchar (10)
);
"""
cursor.execute(sql_table_cerate)
cursor.execute('show columns from addresses')
print(cursor.fetchall())

sql_data_insert="insert into addresses values (0 ,'jim.com','aaa');"
cursor.execute(sql_data_insert)

cursor.execute('select * from addresses;')
print(cursor.fetchall())





cursor.execute('drop database python_connect_test')
db.close()#关连接






