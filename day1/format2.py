# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:07:13 2019

@author: hp
"""

Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""
dir(str)

str1=input("enter the string-")
print(str1)
str2=str1.replace(' ','*')
print(str2)