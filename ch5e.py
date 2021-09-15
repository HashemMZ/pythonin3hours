#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:15:57 2021

@author: HMFR
"""

# Lists
#functions on lists
'''
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:]
'''
#========================================================
'''
to faster do pop and push use collections.deque

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival
'''
#=========================================================
#faster making the a list
squares = [x**2 for x in range(10)]
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]


#===============================================================
from math import pi
[str(round(pi, i)) for i in range(1, 6)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]


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
    
