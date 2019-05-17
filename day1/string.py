# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:58:40 2019

@author: hp
"""

Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""
fname=input("enter your fname")
lname=input("enter your lname")
print("first_name->{},last_name{}.".format(fname,lname))
str3=lname + " " + fname
print(str3)
