# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:54:57 2019

@author: hp
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
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
