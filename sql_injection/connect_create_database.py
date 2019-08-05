# -*- coding:utf-8 -*-
"""
@author: jim

完成代码创建数据库
连接信息在global_value改（同新建的数据库名）
创建的数据库表在create_table函数修改

"""
import pymysql
from sql_injection import global_value as GLOBAL_VALUE

def connect(GLOBAL_VALUE=GLOBAL_VALUE):
    db = pymysql.connect(GLOBAL_VALUE.DB_ADDRESS_IP, GLOBAL_VALUE.DB_USERNAME, \
                         GLOBAL_VALUE.DB_PASSWORD, GLOBAL_VALUE.DB_DATABASES)  # 开连接
    return db



def close_connect(db):
    if(db.close()):
        print('close secceed')
    else:
        print('close fail')



def is_succefully_connect(db):

    if(db!=None):
        print('succefully connected to database')
        return True
    return False

def create_database(db,database_name):


    #创建游标
    cursor=db.cursor()

    #创建数据库
    sql_database_create = """create database if not exists %s character set utf8"""%(database_name)

    if (cursor.execute(sql_database_create) == 1):
        print('succefully create database')
        return True
    else:
        print('fail to create database')
        return False

def create_table(db,database_name):

    cursor=db.cursor()
    use_database='use %s;'%(database_name)
    print(use_database)
    cursor.execute(use_database)
    #创建表
    sql_table_create="""create table addresses(
    id_key int primary key auto_increment,
    address varchar (500),
    date_time varchar (100),
    remarks varchar (200)
    );
    """
    cursor.execute(sql_table_create)





def insert_data(db,address='',date_time='',remarks=''):

    cursor=db.cursor()

    sql_insert="insert into addresses values (0 ,'%s','%s','%s');"%(address,date_time,remarks)
    print(sql_insert)

    print(cursor.execute(sql_insert))


    print('insert')

def reset_delete_database(db=connect()):
    sql_delete='drop database %s;'%(GLOBAL_VALUE.DB_CREATE_DATABASE_NAME)

    cursor=db.cursor()
    cursor.execute(sql_delete)

    print('delete database')



#测试完成
if __name__ == '__main__':

    db=connect()

    if(is_succefully_connect(GLOBAL_VALUE)!=True):
        exit()

    create_database(db,GLOBAL_VALUE.DB_CREATE_DATABASE_NAME)
    create_table(db,GLOBAL_VALUE.DB_CREATE_DATABASE_NAME)
    insert_data(db,'陈锦明','2019.7.28','None')

    #测试版   创建完就删除
    reset_delete_database(db)



