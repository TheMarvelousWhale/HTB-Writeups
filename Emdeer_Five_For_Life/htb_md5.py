# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:03:57 2020

@author: sunbean
"""
from selenium import webdriver
import hashlib

""" I did not include the gecko driver in this repo. You can do it"""

Fox = webdriver.Firefox() 
Fox.get("http://178.128.40.63:31234")

src = Fox.find_element_by_xpath('/html/body/h3')  #grab the string
msg = src.text
test = hashlib.md5(msg.encode())                #Now hash it
key = test.hexdigest()
keyhole = Fox.find_element_by_xpath('/html/body/center/form/input[1]')     #fill in the answer
keyhole.send_keys(key)
submit=Fox.find_element_by_xpath('/html/body/center/form/input[2]')       #submit
submit.click()
