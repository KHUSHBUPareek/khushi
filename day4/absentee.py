# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:16:52 2019

@author: hp
"""
"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
file=open("absentee.txt","wt")
i=1
while(i<=10):
    student=input("enter the student absent")
    file.write(student)
    file.write("\n")
    if(not student):
        break
    i=i+1
    
file.close()      
file=open("absentee.txt","rt")
line=file.readlines()
print(line)   
 
 
