# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:41:41 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
def teen(num):
    if (num in range(13,19) and num==15):
        num=15
    elif (num in range(13,19) and num==16):
        num=16
    elif(num in range(13,19)):
        num=0
    else :
        num=num
    
    return num    
    
dicti=dict()
b=0
i=1
while(i<=3):
    user_input=input("enter key and value separeted by :")
    key,value=user_input.split(":")
    dicti[key]=value
    print(dicti[key])
    num=int(dicti[key])
    a=teen(num)
    b=b+a
    i=i+1
        
    
print(b)      
 

