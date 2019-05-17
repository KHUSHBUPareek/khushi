# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:04:18 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

from collections import OrderedDict
total_billing = OrderedDict()

while(True):
    item=input("enter item_name and net price with it: ")
    if( not  item):
        break
    list1 = item.split()
    price = int(list1[-1])
    product = " ".join(list1[:-1])
    total_billing[product] = total_billing.get(product,0) + price
    
#    if product in total_billing:
#        total_billing[product] = total_billing[product] + price
#    else:
#        total_billing[product] = price

for key, value in total_billing.items():
    print (key+" "+str(value))
##################################

