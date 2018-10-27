# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 17:13:56 2018

@author: jshannon
"""
import datetime
now = datetime.datetime.now()
year = now.year
name = input("What is your name? ")
age = int(input("How old are you now? "))
Year100 = (year - age) + 100
print("You will turn 100 in",Year100)

