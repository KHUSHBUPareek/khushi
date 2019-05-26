# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:36:23 2019

@author: hp
"""
"""
Code Challenge 2

I-Card Generation System

Write a Python code for a system that generates I-card for all studentsof Forsk
Summer Developer Program and store them in image format. 

It must take names and other required information from the user.
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
img=Image.new('RGB',(530,600),color='brown')
draw = ImageDraw.Draw(img)
font1 = ImageFont.truetype("times.ttf", 28)
draw.text( (30,10),"IDENTITY CARD" , font=font1,fill=(236,149,18))
img2=Image.new('RGB',(530,100),color='orange')
offset=(30,50)
img.paste(img2,offset)
font = ImageFont.truetype("arial.ttf", 40)
institute=input("INSTITUTE-->")
draw.text( (30,60), institute  , (0,0,0), font=font)
image3=Image.open("khushipic.jpg")
image3.thumbnail((120,120))
offset=(60,120)
img.paste(image3,offset)
img5=Image.new('RGB',(500,400),color='orange')
offset=(120,250)
img.paste(img5,offset)
name=input("NAME-->")
draw.text( (125,255),"NAME-"+ name , font=font1,fill=(134,7,7))
rollno=input("ROLL NO.-->")
draw.text( (125,310),"ROLL NO.-"+ rollno , font=font1,fill=(134,7,7))
batch=input("BATCH-->")
draw.text( (125,365),"BATCH-"+ batch , font=font1,fill=(134,7,7))
mobileno=input("MOBILE NO-->")
draw.text( (125,420),"MOBILE NO.-"+mobileno, font=font1,fill=(134,7,7))
emailid=input("EMAIL ID-->")
draw.text( (125,475),"EMAILID-"+ emailid , font=font1,fill=(134,7,7))
branch=input("BRANCH-->")
draw.text( (125,530),"BRANCH-"+ branch , font=font1,fill=(134,7,7))
img.save("img4.jpg")