# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:52:09 2019

@author: hp
"""

"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""
my_list=[]
from functools import reduce
result=1
list1=[2,3,4,5,6,7,8]
def f_func(x):
    if(x%2==1):
      return x
my_list= list(filter(f_func,list1))
print(my_list)    
def r_func(result,y):
    result *= y
    return result

print(reduce(r_func,my_list))
