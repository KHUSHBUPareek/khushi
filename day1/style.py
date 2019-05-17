# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:19:10 2019

@author: hp
"""

Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""
stri=input("enter your name")
dir(str)
str1=stri.lower()
print(str1)
str2=stri.upper()
print(str2)
help(str.title)
str3=stri.title()
print(str3)