# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:38:33 2019

@author: hp
"""


"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
list1=[]
dicti=dict()
file=open("romeo.txt","rt")
for item in file:
    list1.append(item.split(" "))
    
for item in list1:
    for item1 in range(0,len(item)):
         dicti[item[item1]]=int(dicti.get(item[item1],0))+1
        

        
    
    
    #print(item1)
    