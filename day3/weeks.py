# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:41:18 2019

@author: hp
"""
"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
tup3=[]
tuple1=('mon','tues','wed','thurs','frid','sat','sun')
tup2=input("enter week days")
tup2=tup2.split(',')
for item in tup2:
    tup3.append(item)
      
print(tup3)        
tuple1=list(tuple1)
print(tuple1)      
for item in tuple1:
    if(item not in tup3):
        tup3.append(item)
        
print(tup3)       
tup3=tuple(tup3)
print(tup3)