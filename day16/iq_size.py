# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:50:16 2019

@author: hp
"""

"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('iq_size.csv')
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:, 0].values   
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
print(lin_reg_1.predict([[90,70,150]]))
import statsmodels.formula.api as sm
features_obj = np.append(np.ones((38,1)), features, axis=1)
features_opt = features_obj[:, [0, 1, 2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
"""features_opt = features_obj[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
features_opt = features_obj[:, [1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
features_opt = features_obj[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
"""
list1=[0, 1, 2,3]
list2=list(regressor_OLS.pvalues)
while max(list2) > 0.005:
    index=list2.index(max(list2))
    list1.remove(list1[index])
    list2.remove(list2[index])
    features_opt=features[:,list1]
    
