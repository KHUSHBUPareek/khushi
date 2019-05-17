# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:07:03 2019

@author: hp
"""
"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
list2=[]
list1 = input("enter list of number separated by space")
print(list1)
list1=list1.split()
print (list1)
for item in list1:
    list2.append(int(item))
    print(list2)

flag=0
for item in list2:
    item1=str(item)
    print(item1)
    if(item<0):
        flag=0
        
    elif(item>0 and item1==item1[::-1]):
        flag=1
        
    else :
        continue
        

if(flag==1):
    print("true")
    
else :
    print("FALSE")    
     
        
         
    