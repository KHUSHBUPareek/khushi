# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:20:11 2019

@author: hp
"""

Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""
A1=input("enter the score of ass1-")
print(float(A1))
A1=float(A1)
A2=input("enter the score of ass3-")
print(float(A2))
A2=float(A2)
A3=input("enter the score of ass3-")
print(float(A3))
A3=float(A3)
E1=input("enter the score of EXAM1-")
print(float(E1))
E1=float(E1)
E2=input("enter the score of EXAM2-")
print(float(E2))
E2=float(E2)
WA1=(float(A1*(10/100.0)))
print(WA1)
WA2=(float((10/100)*A2))
WA3=(float((10/100)*A3))
WE1=(float((35.0/100)*E1))
WE2=(float((35.0/100)*E2))
WE=(WA1+WA2+WA3+WE1+WE2)
print(WE)
