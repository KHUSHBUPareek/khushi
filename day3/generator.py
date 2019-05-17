# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:13:59 2019

@author: hp
"""
"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
list2=[]
list1=input("enter sequence of num" )
list1=list1.split(',')
for item in list1:
    list2.append(item)
   
print(list2)
for item in list2:
     if(item == ',' ):
         list2.remove(',')
         
print(list2) 
tup=tuple(list2)  
print(tup)      