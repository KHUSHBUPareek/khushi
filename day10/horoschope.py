# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:46:26 2019

@author: hp
"""

"""Code Challenge 5

Fortune Teller (Horoscope)

A program that checks your horoscope on various astrology sites and puts them 
together for you each day. The code should share the Horoscope on Tweeter account
 of the user.
"""
import pandas as pd
from time import sleep
from selenium import webdriver
from collections import OrderedDict
wiki="https://www.astrology.com"
driver=webdriver.Chrome("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(wiki)
sleep(2)
rashi=input("enter your rashi")
if(rashi=='ARIES'):
    aries=driver.find_element_by_xpath('/html/body/section[1]/div[3]/a[1]')
    aries.click()
    horoscope=driver.find_element_by_xpath('/html/body/section[1]/section[1]/div[2]/main/p')
    print(horoscope)
elif(rashi=='TAURUS'):
    taurus=driver.find_element_by_xpath('/html/body/section[1]/div[3]/a[2]')
    aries.click()   
    horoscope=driver.find_element_by_xpath('/html/body/section/section[1]/div[2]/main/p[1]')
elif(rashi=='GEMINI'):
    gemini=driver.find_element_by_xpath('/html/body/section[1]/div[3]/a[3]')
    gemini.click()
    horoscope=driver.find_element_by_xpath('/html/body/section/section[1]/div[2]/main/p[1] ')
    
sleep(2)    