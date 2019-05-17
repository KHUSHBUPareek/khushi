# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:57:59 2019

@author: hp
"""
"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
"""
import pandas as pd
from time import sleep
from selenium import webdriver
from collections import OrderedDict
wiki="https://bidplus.gem.gov.in/bidlists"
driver=webdriver.Chrome("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(wiki)
righttable=driver.find_element_by_class_name('tab-content')
print(righttable)
sleep(2)
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in range(1,11):
    b_id=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    list1.append(b_id)
    quant=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]').text
    list2.append(quant)
    address=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]').text    
    list3.append(address)
    start_date=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text
    list4.append(start_date)
    end_date=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text
    list5.append(end_date)
col_name = ["b_id","quantity","address","start_date","end_date"]
col_data = OrderedDict(zip(col_name,[list1,list2,list3,list4,list5]))
df = pd.DataFrame(col_data) 
df.to_csv("bid_plus.csv")


from pandas import DataFrame
import mysql.connector
conn=mysql.connector.connect(user='khushbu', password='9460535599Krish@',
                              host='db4free.net', database = 'khushbu1')
c=conn.cursor()
c.execute ("""CREATE TABLE data1(
        b_id TEXT,
        quantity TEXT,
        department_name TEXT,
        start_date TEXT,
        end_date TEXT
          )""")
c.execute("DROP TABLE data1" )
for i in range(1,10):
    c.execute("INSERT INTO data1 VALUES('{}','{}','{}','{}','{}')".format(list1[i],list2[i],list3[i],list4[i],list5[i]))
c.execute("select * from data1")
columns = ["b_id","quantity","department_name","start_date","end_date"]
df=DataFrame(c.fetchall(),columns=columns)
conn.commit()
conn.close()
