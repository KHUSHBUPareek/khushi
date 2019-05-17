# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:23:15 2019

@author: hp
"""

"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""
from PIL import Image
import requests
from io import BytesIO
URL="http://forsk.in/images/Forsk_logo_bw.png"
response=requests.get(URL)
image=(Image.open(BytesIO(response.content)))
image.save("hello.png")
image.close()