# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:32:39 2019

@author: hp
"""

Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""

x=input("take a no. bw 1-10")
x=int(x)
i=1
while(i <= x):
        y='*'
        print(y*i)
        i=i+1
       
v=2 * x
count=x
while(i > x and i<=v):
    y='*'
    count=count-1
    print(y*count)
    i=i+1
    
    
    
        
   
       
       

    
    
           
    