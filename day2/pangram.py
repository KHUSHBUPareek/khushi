# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:16:22 2019

@author: hp
"""
"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
    """
 list2=[] 
 list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 for item in list1:
     item1=item.upper()
     print(item1)
     list2.append(item1)    
     print(list2)
 
flag=0    
statem=input("enter a statement ")
for item in list1:
      if(item in statem):
         flag=1
         continue
          
      else:
          flag=0
          break
      
 
 if(flag==1) :
    print("PANGRAM")
    
 else :
     print("NOT PANGRAM")
        
          