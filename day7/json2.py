# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:45:16 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import json
import requests
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
c=response.content        
print(c)        
d=response.json()  
print(d["coord"]) 
print(d["weather"]) 
print(d["wind"])    
print(d["sys"]["sunrise"])     
print(d["sys"]["sunset"])   
        