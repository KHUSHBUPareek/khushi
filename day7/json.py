# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:38:15 2019

@author: hp
"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""



import json
faculty="""
{
    "fac":{
     "first_name":"khushbu",
     "last_name":"pareek",
     "photo":"https://www.google.com/search?tbm=isch&sa=1&ei=2U_aXIy7Cc3Zz7sPnZa6wAY&q=photos+of+faculty#",
     "Department":"cs",
     "research":["ml","python"],
     "contact details":94629980
      },
     "fac2":{
     "first_name":"ishita",
     "last_name":"tiwari",
     "photo":"https://www.google.com/search?tbm=isch&sa=1&ei=2U_aXIy7Cc3Zz7sPnZa6wAY&q=photos+of+faculty#",
     "Department":"cs",
     "research":["ml","python"],
     "contact details":94629980      
       }
     
}
"""
student="""
{
     "student1":{
     "first_name":"priya",
     "last_name":"pareek",
     "photo":"https://www.google.com/search?tbm=isch&sa=1&ei=2U_aXIy7Cc3Zz7sPnZa6wAY&q=photos+of+faculty#",
     "Department":"cs",
     "research":["ml","python"],
     "contact details":94629980
      },
     "student2":{
     "first_name":"prena",
     "last_name":"pareek",
     "photo":"https://www.google.com/search?tbm=isch&sa=1&ei=2U_aXIy7Cc3Zz7sPnZa6wAY&q=photos+of+faculty#",
     "Department":"cs",
     "research":["ml","python"],
     "contact details":94629980
      }
}"""
my_data=json.loads(student)
my_json_string=json.dumps(my_data)












