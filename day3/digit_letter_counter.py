# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:09:57 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Digit Letter Cou+nter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
count=0
flag=0
dicti=dict()

dicti[letter]=0
dicti[digits]=0
stri1=input("enter a string" )
stri2=list(stri1)
for item in stri2:
    if(item in range(0,9)):
        dicti[digits]=count+1
        
    else:
        dicti[letter]=flag+1
        
    
print(dicti['letter'])
print(dicti[digits])              
    
