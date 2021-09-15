#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:51:37 2021

@author: HMFR
"""

#modules
'''
A Python module is a file that has a .py extension. 
a set of attributes (variables), methods (functions), and classes (types). 
You can include a module in another Python program 

import module1 
module1.method_name()
module1.attribute_name
'''
#using the asctime() method and the timezone attribute from the time module
#timezone attribute = the number of seconds between UTC and the local time.
import time

print(time.asctime())
print(time.timezone)
print(time.timezone/3600)#convert to hour

#instead of importing the whole module just the required function or method)
#from module_name import method_name
from time import asctime
print(asctime())# no need to repeat module's name

#importing multiple methods 
from time import asctime, sleep #halts your program for n seconds
print('Hello') 
sleep(3)
print('hello again')

#also can use: from module import *  to import everything! but not a good idea
from time import *
print(asctime())

#to see what is inside any module you can use dir() here or on command line
#>>>dir(time)
print(dir(time))

#module are searched in sys.path; differs in diff systems and OS
import sys
for path in sys.path:
    print(path)

#if module does not exist in sys.path it makes an exception
#import sayHello
    
"""
A note on Python std lib
As we’ve worked through previous examples, we have been using the time module
which comes included with Python. In fact, Python is supplied with a large
library of modules for you to take advantage of. I would highly recommend that 
you take some time to really look at what the Python standard library has to 
offer before you even think of writing any of your own code. For example, if 
you are looking to read and write CSV (comma-separated values) files, don’t 
waste your time creating something from scratch when it already exists. Just 
use Python's pre-existing csv module. Are you looking to enable logging in 
your program? Well, there’s a logging module which can help you do that. Do 
you want to make an HTTP request to a web service and then parse the JSON 
response? Try using the urllib.request and json modules. To explore these 
modules and more, check out the list of what is available in the Python 
Standard Library located at https://docs.python.org/3/library/.
"""
#sys.exit() function for terminating a file caused and exception
import sys 
file_name = 'test.txt' 
try: 
    with open(file_name) as test_file: 
        for line in test_file: 
            print(line) 
except: 
    print('Could not open {}.'.format(file_name)) 
    #sys.exit(1)# on exception event usu a non-zero error code is sent. default is zero
    
#make your own modules
#simply save your methods(functions) and ... in file with .py extension
#I have done this for method say_hello() and saved it in a file with the same name
import say_hello
say_hello.say_hello()

#in another file, say_hello2 I defined another say_hello() method 
import say_hello2#importing the method executes the whole python file!
say_hello2.say_hello()

#defineing 'main' part of code 
#see the file say_hello3.py
print(__name__)#variable __name__ is used to control execution of an imported module
import say_hello3
say_hello3.say_hello()

