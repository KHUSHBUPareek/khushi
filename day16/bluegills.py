# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:38:48 2019

@author: hp
"""
"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
#temp = dataset.values
features = dataset.iloc[:,0].values
features=np.array(features)
features=features.reshape(-1,1)
labels = dataset.iloc[:, -1].values
plt.scatter(features, labels)
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
print (lin_reg_1.predict(features))
-------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
plt.scatter(features,labels,color='red')
plt.plot(features,lin_reg_1.predict(features))   
plt.xlabel('age')  
plt.ylabel('length')  
plt.show()
   

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('age')
plt.ylabel('length')
plt.show()
x=np.array(5)
x=x.reshape(-1,1)
print (lin_reg_2.predict(poly_object.transform(x)))
