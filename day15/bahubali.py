# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:40:46 2019

@author: hp
"""

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("Bahubali2vsDangal.csv")
df.plot(x='Days', y='Bahubali_2_Collections_Per_day', style='o')  
df.plot(x='Days', y='Dangal_collections_Per_day', style='o')  
features = df.iloc[:,0].values
features=features.reshape(-1,1)  
labels = df.iloc[:, 1].values
#labels=np.array(labels)
#labels=labels.reshape(1,-1)
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

print (regressor.coef_*10 + regressor.intercept_)
x = [10]
x = np.array(x)
print(regressor.predict([[10]]))


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
features1 = df.iloc[:,0].values
features1=features.reshape(-1,1)  
labels1 = df.iloc[:, -1].values
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features1, labels1) 
print (regressor.coef_*10 + regressor.intercept_)
x = [10]
x = np.array(x)
print(regressor.predict([[10]]))




import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
features1 = df.iloc[:,0].values
features1=features.reshape(-1,1)  
labels2 = df.iloc[:,1:].values
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features1, labels1) 
print (regressor.coef_*10 + regressor.intercept_)
x = [10]
x = np.array(x)
print(regressor.predict([[10]]))