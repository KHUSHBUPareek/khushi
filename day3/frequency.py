# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:18:43 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
dicti=dict()
stri=input("enter a string")
stri1=set(stri)
for item in stri1:
    for item1 in stri:
        if(item==item1):
            dicti[item]=int(dicti.get(item,0))+1
            
print(dicti)            
            
        

    
    