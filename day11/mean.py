# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:27:38 2019

@author: hp
"""
"""
 Code Challenge 

 Find the mean, median, mode, and range for the following list of values:
 13, 18, 13, 14, 13, 16, 14, 21, 13


Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8
"""
from collections import Counter
list1=[13,18,13,14,13,16,14,21,13]
total=0
count=0
for i in list1:
    total=total+i
    count=count+1
    
print(total)
print(count)
mean=(total)/(count)
print(mean)
list1.sort()
if (count)/2 != 0:
    value=int(count/2)
    median=list1[value]
list1=[13,18,13,14,13,16,14,21,13]    
frequency=Counter(list1)
print(frequency)
for key,value in dict(frequency).items():
    print (key,value)
mode=max(frequency[key])