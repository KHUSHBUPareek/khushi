# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:44:28 2019

@author: hp
"""


"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""
def revers(x):
    y=x[::-1]
    print(y)
    
stri=input("enter a string")
print(stri)
revers(stri)    