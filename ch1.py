# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#stringsرشته ها
quote="Hashem is the owner of the 'World'"
print(quote)

quote2 = 'not only the best one in the world but entire "galaxy"'
print(quote2)

#indexing
str1 = 'asparagus'
print(str1[0],str1[1])
print('asparagus'[0])

print('Hashem')


print(len(str1))

#string functions
name = 'Hashem'
print(name.lower())
print(name.upper())
print('Hashem'.upper())

print('today '+'is '+'Wed')

#repeat
print('Hashem ' * 5)
strHello = 'Hello '*2

#str function 
nFriends = 5
print('hello to my '+ str(nFriends) + " friends")


#format
print('I said you {} times that you have not to go'.format('1000'))
#print('we are {0}, {1} and {2}.\n{2} is the latests'.format('Hashem','Sohrab','Kourosh'))
'''
#formatting output length to be equal; good for make tables look nice
print('{0:9},{1:12} is an engineer'.format('Hashem','Moradmand'))
print('{0:9},{1:12} is an actor'.format('Javad','Razavian'))

#formatting left < right > or middle ^ alignment
print('{0:>9},{1:>12} is an engineer'.format('Hashem','Moradmand'))
print('{0:>9},{1:>12} is an actor'.format('Javad','Razavian'))

#formatting output length to be equal; good for make tables look nice
print('{0:6},{1:1.2f} is an engineer'.format('Hashem', 1.82))
print('{0:6},{1:1.4f} is an actor'.format('Javad',1.6235))


#input function
name = input('enter your name: ')
print('your name is {}'.format(name))

'''