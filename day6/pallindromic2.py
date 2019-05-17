# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:13:49 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
list1=[]
list2=[]
inp=input("enter the list of numbers").split(" ")
print(inp)
for item in inp:
    inp1=int(item)
    list1.append(inp1)
    
print(list1)
c=all(item1>0 for  item1 in list1)
for item3 in list1:
    inp2=str(item3)
    list2.append(inp2)
    
d=any(item4==item4[::-1] for item4 in list2)        
if(c==d):
    print("true")
else:
    print("false")    