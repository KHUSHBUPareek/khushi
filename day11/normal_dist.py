# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:28:54 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(150,20,1000)
print (incomes)
plt.hist(incomes, 100)
plt.show()
std1=np.std(incomes)
var1=np.var(incomes)