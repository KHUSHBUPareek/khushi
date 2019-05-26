# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:49:14 2019

@author: hp
"""
"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Telecomchurn.csv")
churn1=df['churn'][df['voice mail plan']=='yes'][df['international plan']=='yes'].value_counts()[True]
charge=df["total intl charge"][df['churn']==True].sum()
new_def=df["total intl charge"][df['churn']==True]
new_def.hist(bins=20)
new_df1=df[df['churn']==True]
new_df2=df[df['churn']==False]
night=new_df1["total night minutes"].max()
new_df1["states"]=df["state"]
night1=new_df1["state"][new_df1["total night minutes"]==new_df1["total night minutes"].max()]
nightcl=new_df1["total night calls"].sum()
daycl=new_df1["total day calls"].sum()
evecl=new_df1["total eve calls"].sum()             
cservcl=new_df1["customer service calls"].sum()                                                                                                                   
intlcl=new_df1["total intl calls"].sum()
labels='nightcl','daycl','evecl','cservcl','intlcl'
data=[nightcl,daycl,evecl,cservcl,intlcl]
colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
explode=[0,0.2,0,0,0]
plt.pie(data,labels=labels,colors=colors,shadow=True,explode=explode)
nightcg=new_df1["total night charge"].sum()
daycg=new_df1["total day charge"].sum()
evecg=new_df1["total eve charge"].sum()   
intlcg=new_df1["total intl charge"].sum()
min(nightcg,daycg,evecg,intlcg)
data1=[nightcg,daycg,evecg,intlcg]
labels="nightcg","daycg","evecg","intlcg"
explode=[0,0,0,0.2]
colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.pie(data1,labels=labels,colors=colors,shadow=True,explode=explode)
acc_len=new_df2["account length"].sum()
acc_len1=new_df1["account length"].sum()
max(acc_len,acc_len1)
df.groupby('area code')[df['international plan']=='yes'].max