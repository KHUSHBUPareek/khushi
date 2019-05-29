# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:54:09 2019

@author: hp
"""

"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("Foodtruck.csv")
df.plot(x='Population', y='Profit', style='o') 
features=df.iloc[:,:-1].values
labels=df.iloc[:,1].values
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 
print(regressor.intercept_)  
print (regressor.coef_)
print (regressor.coef_*3.073 + regressor.intercept_)
print (regressor.predict(3.073))
x = [3.073]
x = np.array(x)
regressor.predict(x.reshape(1,-1))
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 
labels_pred = regressor.predict([[3.073]]) 

#To compare the actual output values for features_test with the predicted values, execute the following script 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print (df) 


