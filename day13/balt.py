# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:37:39 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:

import pandas as pd
import requests
import StringIO as StringIO
import numpy as np
        
url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = StringIO.StringIO(r.content)

dataframe = pd.read_csv(data,header=0)

dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))
"""
import pandas as pd
import requests
import numpy as np
df=pd.read_csv("Baltimore.csv")
df['AnnualSalary'] = df['AnnualSalary'].astype(str)
df['AnnualSalary']=df['AnnualSalary'].str.lstrip('$')
df['AnnualSalary'] = df['AnnualSalary'].astype(float)
grouped = df.groupby(['JobTitle','AnnualSalary'])
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])
mannual=aggregated.sort_values(by=['AnnualSalary'],ascending=False)
job=df.groupby(['JobTitle'])
jobst=job.apply(lambda _df: _df.sort_values(by=['JobTitle']))
df['JobTitle'].value_counts()[0:10].plot('bar')
spend=df.sort_values(by=['GrossPay'],ascending=False)
agency_nameid = df[['Agency','AgencyID']]
df['GrossPay'].isnull().sum()