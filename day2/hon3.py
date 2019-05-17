# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:55:44 2019

@author: hp
"""

# Make a function days_in_month to return the number of days in a specific month of a year
def days_in_month(y,x):
    list1=['january','march','may','july','august','october','december']
    list2=['april','june','september','november']
    list3=['february']
    if(x in list1):
        print("days are 31")
        
    elif(x in list2):
        print("days are 30")
        
    elif(x in list3 and y % 4 == 0):
        print("29")
        
    else :
       print("28")
       
       
days_in_month(2016,'february')      
    