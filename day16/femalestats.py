# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:53:49 2019

@author: hp
"""
"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Female_Stats.csv")
features1 = df.iloc[:, 1:].values
labels = df.iloc[:, 0].values
#import statsmodels.api as sm
#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)

#adds a constant column to input data set.
#features1 = sm.add_constant(features)


import statsmodels.formula.api as sm
features_obj = np.append(np.ones((214,1)), features1, axis=1)
features_opt = features_obj[:, [0, 1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
---------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Female_Stats.csv")
df["momheight1"]=df["momheight"]+1
features = df.iloc[:,2:].values
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
print "Predicting result with Linear Regression",
print (lin_reg_1.predict(features).mean())
----------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Female_Stats.csv")
df["dadheight1"]=df["dadheight"]+1
features2 = df.iloc[:,2:].values
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
print ("Predicting result with Linear Regression"),
print (lin_reg_1.predict(features).mean())