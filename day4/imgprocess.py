# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:49:58 2019

@author: hp
"""

"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""
from PIL import Image
import os
img = Image.open('sample1.jpg')
img_rotate=img.transpose(Image.ROTATE_90)
print(img_rotate)
img_rotate.save('sample12.jpg')

from PIL import Image
import os
img = Image.open('sample2.jpg')
width,height=img.size
left=(width-160)/2
top=(height-204)/2
right=(width+160)/2
bottom=(height+204)/2
img.crop((left,top,right,bottom))

img = Image.open("sample3.jpg")
img.thumbnail((75,75 ))
print(img.width, img.height)
img.save('thumb_sample13.jpg')