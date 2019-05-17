# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:30:31 2019

@author: hp
"""
"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi
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
import os
import sqlite3
from pandas import DataFrame

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'players.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE rank(
          pos TEXT,team TEXT,weighted_matche TEXT,points TEXT,ratings TEXT)""")

for i in range(1,10):
    c.execute("INSERT INTO rank VALUES('{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i]))
         
c.execute("select * from rank")
columns = ["pos","team","weighted matche","points","ratings"]
df=DataFrame(c.fetchall(),columns=columns)
conn.commit()
conn.close()
    
