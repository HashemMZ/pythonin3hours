#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:58:21 2021

@author: HMFR
"""

def say_hello(): 
    print('Hello! from 3 :)))')
    print('you are in',__name__)#returns the name of this module say_hello3

def main(): 
    print('Hello from say_hello3.py!') 
    say_hello() 
#if variable __name__ is equal to __main__ then main() method is executed
if __name__ == '__main__': main()
