# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:43:10 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

file=open("write.txt","wt")
file.write("this is my india")
file.write("hello everyone")
file.close()
fp=open("write1.txt","wt")
file=open("write.txt","rt")
for text in file:
    fp.write(text)
    
fp.close()

