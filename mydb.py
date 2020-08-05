# coding: utf-8 
# @Time    : 2020/8/4 15:52
# @Author  : Sc
# @Email   : song9624643@163.com
# @File    : mydb.py
# @Software: PyCharm
"""
封装pymysql
"""
import pymysql


class  MyDB():
    #当创建对象时，自动执行
    def __init__(self):
        #连接数据库
        self.db = pymysql.connect(
            host="localhost",
            user="root",  
            password="17851167",
            database="demo1",
            port=3306
        )
        self.cursor=self.db.cursor()
    #查询
    def select(self,sql):
         #执行sql语句
        res=self.cursor.execute(sql)
        print(f"查到了{res}条数据")
        #返回
        data=self.cursor.fetchall()
        for var in data:
            print(var)
    def updata(self,sql):
        res=self.cursor.execute(sql)
        #提交
        self.db.commit()
        return res
    #当所有代码执行完后，自动执行
    def __del__(self):
        #关闭数据库连接
        self.cursor.close()
        self.db.close()


#测试
# obj=MyDB();
# sql="select *from students"
# data=obj.select(sql)
# print(data)