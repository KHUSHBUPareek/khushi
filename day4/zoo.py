# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:35:37 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""

import csv
with open("zoo.csv",mode='r')as zoo_file:
    csv_reader=csv.reader(zoo_file,delimiter=",")
    line=zoo_file.readlines()
    print(line)     
       
       
animal=[]   
import csv
with open("zoo.csv",mode='r')as zoo_file:
    csv_reader=csv.reader(zoo_file,delimiter=",")
    next(csv_reader)
    for row in  csv_reader:
        animal.append(row[0])
        
print(animal)  
seti=set(animal)
list2=list(seti) 
print(list2)  

dicti=dict()
with open("zoo.csv",mode='rU')as zoo_file:
    csv_reader=csv.reader(zoo_file,delimiter=",")
    next(csv_reader)
    for row in  csv_reader:
        dicti[row[0]]=int(row[-1])+int(dicti.get(row[0],0))
        
print(dicti)    
    
dicti=dict()
with open("zoo.csv",mode='rU')as zoo_file:
    csv_reader=csv.reader(zoo_file,delimiter=",")
    next(csv_reader)
    for row in  csv_reader:
        
        
print(dicti)        
       

        
    