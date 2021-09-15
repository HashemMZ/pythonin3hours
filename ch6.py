#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:10:27 2021

@author: HMFR
"""

#Dictionaries also called hashes or hash tables or associative arrays
#dictionary_name = {key_1: value_1, key_N: value_N}. create an empty dictionary, 
# use dictionary_name = {}.
contacts = {'secretary':'5550','sianat':'5512','teleport':'5518','lab':'5521'}
print(contacts['sianat'])
print('dial {} to coordinate for crosspol'.format(contacts['sianat']))

print('-------------------------1')
#change value by key
contacts['sianat']='13728'
print(contacts)

print('-------------------------2')
#adding items to dictionary
contacts['info']='162'
print(contacts)

print('-------------------------3')
#deleting items using del statement
del contacts['lab']
print(contacts)

print('-------------------------4')
#values in the list can be of diff types
contacts['ANT']=['5546','5548']
print(contacts)

print('-------------------------5')
# using 'in' we can access keys
for num in contacts:
    print(num)

print('-------------------------5.5')
# using 'in' we can access values for keys
for num in contacts['ANT']:
    print(num)
#using keys() function to return keys of a dict
print(contacts.keys())

print('-------------------------6')
#value in dictionaey.keys() return True or False
if 'sianat' in contacts.keys():
    print(contacts['sianat'])

print('-------------------------7')    
if 'ANT' in contacts.keys():
    print(contacts['ANT'][1]) #second element of list

print('-------------------------8')
#using values() func for accessing values in dict
print(contacts.values())

print('-------------------------9')
print('5550' in contacts.values())

print('-------------------------10')
#looping through a dict. good pattern to use plural for dict name like contacts
for contact in contacts:
    print('the tel num for {} is {}'.format(contact,contacts[contact]))

print('-------------------------11')
#using items() func to reuten keys and values in pairs 
print(contacts.items())

print('-------------------------12')
#looping through a dict. using two variable in for loop using items()
for name, tel in contacts.items():
    print(name,tel)

print('-------------------------13')
#nesting dicts
contacts = {}
print(contacts)
contacts = {
        'sianat':{
                'email':'sianat@irib.com',
                'tel':'13728'
        },
        'teleport':{
                'email':'tel@irib.ir',
                'tel':'5518'
        },
        'lab':{
                'email':'lab@irib.ir',
                'tel':'5521'
        }
        }
print(contacts)

print('-------------------------14')
for name in contacts:
    print('the section is {}'.format(name))
    print('its email is {}'.format(contacts[name]['email']))
    print('its tel is {}'.format(contacts[name]['tel']))
