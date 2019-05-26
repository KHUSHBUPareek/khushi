# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:30:51 2019

@author: hp
"""

"""
Code Challenge 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts

"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
img=Image.open("cer.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 70)
institute=input("INSTITUTE-->")
draw.text( (400,250),   institute  , (0,0,0), font=font)
font = ImageFont.truetype("arial.ttf", 50)
name=input("enter name-->")
draw.text( (160,400), "THIS IS TO CERTIFY THAT MR/MRS  "+ name +" \n \n HAS PARTICIPATED IN BOOTCAMP CONDUCTED BY \n\n FORSK TECHNOLOGIES."  , (0,0,0), font=font)
img3 = Image.open("sign.png")
offset=(180,900)
img.paste(img3,offset)
img4 = Image.open("stamp.png")
offset=(1480,900)
img.paste(img4,offset)
img.save("certificate3.jpg")


# save the edited image
 
