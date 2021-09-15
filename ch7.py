#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 07:35:33 2021

@author: HMFR
"""

#tuples; cannot be changed; have index; for data that is fixed
#tuple_name = (item_1, item_2, item_N).

months = ('Far','Ord','Khor','Tir','Mor','Shah','Meh','Aba','Aza'
          ,'Dey','Bah','Esf')
print(months[0])
print(months)

print('-------------------------1')
#single value tuple; don't forget the comma
skys = ('sky',) #comma
print(skys)

print('-------------------------2')
#for loop
for month in months:# tuple values are accessed by index
    print(month)
    
print('-------------------------3')
#test changing the tuple: exception
#months[0]='Farvardin'

print('-------------------------4')
#del statement to remove the whole tuple
del months
#print(months)

print('-------------------------5')
#type() func returns type of an object
months = ('Far','Ord','Khor','Tir','Mor','Shah','Meh','Aba','Aza'
          ,'Dey','Bah','Esf')
print(type(months))

print('-------------------------6')
#converting tuple to list using list() func
months_list = list(months)
print(months_list)

print('-------------------------7')
#converitn list to tuple using tuple() func
animals = ['lion','dog','cat']
animals_tuple = tuple(animals)
print(type(animals_tuple))

print('-------------------------8')
#assiging multiple variables
(f,o,k,t,m,s,me,a,az,d,b,e)=months
print(f)
print(me)
print(type((f,o)))
"""any set of objects in ( , , , ) is considered as tuple even without an explicit name"""

print('-------------------------9')
#using lists to set values in tuple
contacts = ['5550','office@irib.ir']
(phone,email)=contacts
print(phone)

print('-------------------------10')
#using tuple for return value of function as set of values
def high_and_low(numbers):
    high = max(numbers)
    low = min(numbers)
    return (high,low)

print('-------------------------11')
nums=[36,25,12,10,8,45]
(Max,Min)= high_and_low(nums)
print(Max,Min)

print('-------------------------12')
#looping through a tuple. using two variable in for loop using items()
contacts = [('صیانت','5512'),('آزمایشگاه','5521')] #a List of tuples
for (name, tel) in contacts:
    print(name,tel)


