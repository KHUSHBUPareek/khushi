# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:22:11 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
#without numpy
from collections import Counter
import numpy as np 
#random.random(shape) – creates arrays with random floats over the interval [0,1].
x =-10* np.random.random(40)+15
print (x)
frequency=Counter(x)
print(frequency)
value=frequency.most_common()[0][0]
print(value)


#with numpy
import numpy as np 
#random.random(shape) – creates arrays with random floats over the interval [0,1].
a=-10* np.random.random(40)+15
print (a)
a = np.array(a, dtype=np.int64)
counts = np.bincount(a)
print (np.argmax(counts))