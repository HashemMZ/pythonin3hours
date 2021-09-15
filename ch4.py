#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:34:47 2021

@author: HMFR
"""
#functions
'''
# reuturn value None, when no retuen value exists
def func():
    print('something')

print(func())

#default arg value
# default value >> just one time applies
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1),f(2))

#keyword and positional arg of func.
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
#whether use the position or the keyword to tell the func which arg you mean
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
#invalid
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument

#sending dict in arg
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")      

'''

#define before using them
def sayHello():
    print('hello everyone')
    
print('today is nice')
#using function
sayHello()

# with arguments or also called parameters
def sayHelloTo(name):
    print('hello to {}!'.format(name))
    
sayHelloTo('Hashem')

#with arguments with default value
def sayHelloTo(name='Hasan'):
    print('hello to {}!'.format(name))
    
sayHelloTo('Hashem')
sayHelloTo()

#multiple params
#with arguments
def sayHelloTo(name,age=40):
    print('hello to {} and happy {}th birthday'.format(name,age))
    
sayHelloTo('Hashem')
sayHelloTo('Hashem',39)

# documention string or docstring in function for later help
def sayHi(name,age=40):
    """this function prints name and congrats birthday"""
    print('hello to {} and happy {}th birthday'.format(name,age))
help(sayHi)

# return value of function
def oddoreven(num):
    if num%2 ==0:
        #print('even')
        return 'Even'
    else:
        #print('odd')
        return 'Odd'

oddoreven(12)
print(oddoreven(13))



        

