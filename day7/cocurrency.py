# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:14:56 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import json
import requests
url1="http://free.currencyconverterapi.com/api/v5/convert"
url2="?q=USD_INR&compact=y"
url3="&apiKey=93c028f43b63a1d3a9cd"

url=url1+url2+url3
response=requests.get(url)
js=response.json()

