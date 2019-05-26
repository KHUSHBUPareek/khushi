# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:12:30 2019

@author: hp
"""
"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt 
year=1880
df=pd.DataFrame() 
file_names = os.listdir('baby_names/')
for file in file_names:
    with open(file) as f:
        df[year] = pd.Series(f.readlines())
        year+=1
        if year==2011:
            break

list1=[]
list2=[]
for item in df[2010]:
    item=item.split(",")
    list1.append(item)     
d2=pd.DataFrame(list1,columns=["Name","Sex","Quantity"])
male=d2["Name"][d2["Sex"]=='M'].head(5)
female=d2["Name"][d2["Sex"]=='F'].head(5)
for item in df[2007]:
    item=item.split(",")
    list2.append(item)
d3=pd.DataFrame(list2,columns=["Name","Sex","Quantity"])    
quan=pd.pivot_table(d3,index=["Name","Sex"],values=["Quantity"],aggfunc=np.sum)
data=d3["Quantity"]
plt.hist(data)
    