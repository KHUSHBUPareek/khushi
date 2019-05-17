# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:50:16 2019

@author: hp
"""

"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
import re
listi=[]
while(True):
    email1=input("enter your email")
    if(re.findall(r'^[a-zA-Z0-9-_]+@+[a-z0-9A-Z]+\.[0-9A-Za-z]{2,4}$',email1)):
        listi.append(email1)
        
    elif(not email1):
        break
    else:
        continue
 
    
print(listi)    
        
    
    
    