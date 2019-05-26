# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:49:11 2019

@author: hp
"""

"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

import pandas as pd
from time import sleep
from selenium import webdriver
import matplotlib.pyplot as plt 
from collections import OrderedDict
wiki="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
driver=webdriver.Chrome("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(wiki)
sleep(2)
state1=[]
nationals=[]
for i in range(1,30):
    state=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+ str(i)+']/td[2]').text
    state1.append(state)
    national=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[5]').text
    nationals.append(national)


col_name = ["State","National share"]
col_data = OrderedDict(zip(col_name,[state1,nationals]))
df = pd.DataFrame(col_data)   
statee=df['National share'].head(6)  
labels=['Rajasthan','Madhya pradesh','maharashtra','uttar pradesh','gujarat','karnataka']
explode=[0.1,0,0,0,0,0]
plt.pie(statee,labels=labels,shadow=True,explode=explode)
