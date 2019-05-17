# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:25:13 2019

@author: hp
"""

"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
my_filter_list=[]
height_count=[]
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
my_filter_list = list(filter ( lambda x:'height' in x, people))
c=sum(list(map(lambda x: x['height'], my_filter_list)))


print(my_filter_list)
count=0
height_count=list(map(lambda x:len(my_filter_list) , my_filter_list))
print(height_count)
for item in height_count:
     if(item>0):
         average_height=list(map(lambda x:c/item , height_count))
print(average_height)
