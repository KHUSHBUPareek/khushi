# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:59:35 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
a=[6,9,2,3,5,8,1,5,4]
import numpy as np
x=np.array(a)
print(x)
x1=x.reshape(3,3)
print(x1)
#taking input from user
a=input("enter space separeted values")
list1=a.split(" ")
x=np.array(list1,dtype=int)
print(x)
x1=x.reshape(3,3)
print(x1)