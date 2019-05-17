# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:28:22 2019

@author: hp
"""


"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
file=input("enter which file you want to open")
fp=open(file,"rt")
line=(fp.readlines())
print(line[-1])
fp.close()
