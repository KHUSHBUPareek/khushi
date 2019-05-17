# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:41:12 2019

@author: hp
"""

"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""
import os
import sqlite3
from pandas import  DataFrame
conn=sqlite3.connect("db_university")
c=conn.cursor()
c.execute("""CREATE TABLE university(
        name string,
        rollno int,
        student_age int,
        branch string
        
         )""")
c.execute("DROP TABLE university")
c.execute("INSERT INTO university values('khushbu','1600','18','cs')")
c.execute("INSERT INTO university values('kunal','1601','18','cs')")
c.execute("INSERT INTO university values('ishu','1602','18','cs')")
c.execute("INSERT INTO university values('aman','1603','18','cs')")
c.execute("INSERT INTO university values('ishita','1604','18','cs')")
c.execute("INSERT INTO university values('surbhi','1605','18','cs')")
c.execute("INSERT INTO university values('shivam','1606','18','cs')")
c.execute("INSERT INTO university values('bharat','1607','18','cs')")
c.execute("INSERT INTO university values('addy','1608','18','cs')")
c.execute("INSERT INTO university values('arpit','1609','18','cs')")
c.execute("SELECT * FROM university")
df=DataFrame(c.fetchall())
df.columns = ["id","first","last","pay"]
conn.commit()
conn.close()


from pandas import DataFrame
import mysql.connector
conn=mysql.connector.connect(user='khushbu', password='9460535599Krish@',
                              host='db4free.net', database = 'khushbu1')
c=conn.cursor()
c.execute ("""CREATE TABLE university(
        name TEXT,
        rollno INTEGER,
        student_age INTEGER,
        branch TEXT
          )""")
c.execute("DROP TABLE university")
c.execute("INSERT INTO university values('khushbu','1600','18','cs')")
c.execute("INSERT INTO university values('kunal','1601','18','cs')")
c.execute("INSERT INTO university values('ishu','1602','18','cs')")
c.execute("INSERT INTO university values('aman','1603','18','cs')")
c.execute("INSERT INTO university values('ishita','1604','18','cs')")
c.execute("INSERT INTO university values('surbhi','1605','18','cs')")
c.execute("INSERT INTO university values('shivam','1606','18','cs')")
c.execute("INSERT INTO university values('bharat','1607','18','cs')")
c.execute("INSERT INTO university values('addy','1608','18','cs')")
c.execute("INSERT INTO university values('arpit','1609','18','cs')")
c.execute("SELECT * FROM university")
df=DataFrame(c.fetchall())
df.columns = ["name","rollno","student_age","branch"]
conn.commit()
conn.close()


import pymongo

client = pymongo.MongoClient("mongodb://khushbu:9460535599Krish%40@cluster0-shard-00-00-gkph0.mongodb.net:27017,cluster0-shard-00-01-gkph0.mongodb.net:27017,cluster0-shard-00-02-gkph0.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb=client.yourdbname
def add_student(name,Student_Age, Student_Roll_no, Student_Branch):
    mydb.yourcollectionname.insert_one(
            {"name":name,
             "age":Student_Age,
             "rollno":Student_Roll_no,
             "branchs":Student_Branch
             })


def fetch_all_employee():
    user = mydb.yourcollectionname.find()
    for i in user:
        print (i)




add_student('khushbu','1600','18','cs')
fetch_all_employee()