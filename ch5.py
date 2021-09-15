#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:15:57 2021

@author: HMFR
"""

# Lists
#made by [] and commas,
animals = ['cock', 'hen', 'chicken']
print(animals[0])

animals[0]='rooster'
print(animals[0])

# indices are circular i.e  0 1 2 -1 -2 -3
print(animals[-1])

# append function
animals.append('fox')
print(animals[-1])

#extend function
animals.extend(['snake','rabbit'])
print(animals)

animals.extend(animals)
print(animals)


#insert function
animals = ['rooster', 'hen', 'chicken', 'fox', 'snake', 'rabbit']
animals.insert(0,'bear')
print(animals)

#slices
some = animals[1:4]#from 1 to before 4
print('animals are {}'.format(animals))
print('1 to 4 are {}'.format(some))

slice = animals[4:]#4 to the LAST
print('4: is {}'.format(slice))

slice = animals[-2:]
print('-2: is {}'.format(slice))

# slice from strings
slice = 'Hashem Moradmand'[0:6] #from index 0 to 5
print(slice)

# index function returns the index of occurance of sth
print('chicken is occured at {}'.format(animals.index('chicken')))

# if index func cannot find the value in the list => exception 
#indexat = animals.index('chick')
#print('chick is occured at {}'.format(indexat))

# exception handling: try & except
try:
    indexat = animals.index('chick')
except:
    indexat = 'NA'
print('chick is occured at {}'.format(indexat))

# for loop
# for item_variable in list_name:
for anim in animals:
    print(anim.upper())
    
# while loop
# while condition:
print ('---WHILE LOOP---')
index = 0
while index < len(animals):
    print(animals[index])
    index +=1;
print('end')

#sort() and sorted() functions
animSorted = sorted(animals)
print(animSorted)
print(animals)
animals.sort() #changes the list itself (list will be sorted)
print(animals)

# concatenating two lists
moreanimals = ['dog','cat']
allanimals = animals + moreanimals
print(allanimals)

# append function
allanimals.append('wolf')
#allanimals.append('wolf','tiger') #append takes just one arg
print(allanimals)

#range function
#range(N) produces indices 0 to N-1 totaly N items
for num in range(5):
    print(num)

for num in range(len(animals)):
    print(animals[num])
    
for num in range(2,5):
    print(num)
print('------')
for num in range(10,25,2):
    print(num)

for num in range(0,len(animals),3):
    print(animals[num])
    