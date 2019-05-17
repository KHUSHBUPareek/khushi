# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:57:32 2019

@author: hp
"""
"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""
def bricks(x):
    print(x)
    y=1*x[0]+5*x[1]
    if(y>x[2]):
        print("true")
        
    else:
        print("false")
        
listr=[]
list1=input("no of small bricks ,no of big bricks , target")
list1=list1.split()
print(list1)
for item in list1:
    item=int(item)
    print(item)
    listr.append(item)
    print(listr)
    
bricks(listr)    