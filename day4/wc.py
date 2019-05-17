# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:35:08 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
dicti=dict()
listi=[]
line=0
word=0
list2=[]
sete=set()
character=0
file=input("enter the file you want to open::")
fp1=open(file,"rt")
for item in fp1:
    character+=len(item)
    line+=1
    listi.append(item.split(" "))
    
for item2 in listi :
        word+=len(item2)

for item in listi:
    for item1 in range(0,len(item)):
         dicti[item[item1]]=int(dicti.get(item[item1],0))+1
        
for key in dicti :
    if(int(dicti.get(key))==1):
        list2.append(key)
        
uword=len(list2)        
     
fp1.close()