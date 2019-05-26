# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:16:30 2019

@author: hp
"""

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import csv
import numpy as np
import pandas as pd      
df=pd.read_csv("Automobile.csv")
df['price'] = df['price'].fillna(df['price'].mean())
#price1=df.loc[:,'price']
array1=np.array(df["price"])
df['price'].min()
df['price'].max()
df['price'].mean()
df['price'].var()
df['price'].std()