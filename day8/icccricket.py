# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:20:59 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup
import requests
wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(wiki).text
soup=BeautifulSoup(source,"lxml")
print(soup.prettify()) 
all_tables=soup.find_all('table')
print(all_tables)    
right_table=soup.find('table',class_='table')
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==5:
         A.append(cells[0].text.strip())
         B.append(cells[1].text.strip())
         C.append(cells[2].text.strip())
         D.append(cells[3].text.strip())
         E.append(cells[4].text.strip())
import pandas as pd
from collections import OrderedDict
col_name=["pos","team","weighted matche","points","ratings"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")    


