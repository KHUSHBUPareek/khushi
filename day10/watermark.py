# -*- coding: utf-8 -*-
"""
Created on Sun May 19 10:55:07 2019

@author: hp
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
 
def watermark_text(input_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype("arial.ttf", 40)
    drawing.text(pos, text, fill='#D3D3D3', font=font)
    photo.show()
    photo.save('img5.jpg')
 
 
if __name__ == '__main__':              #whnever a module is run standalone by a user and can perform appropriate action
    img = 'img4.jpg'        
    watermark_text(img, text='www.mousevspython.com',
                   pos=(150, 350))