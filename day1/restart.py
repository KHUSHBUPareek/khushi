# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:27:24 2019

@author: hp
"""

Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
    
    stri="RESTART"
    s=stri.find('R')
    print(s)
    str1=stri[0:s]
    print(str1)
    str2=stri[s+1:7]
    str3=str2.replace('R','$')
    print(str3)
    str4=stri[s] + str3
    print(str4)