#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:14:49 2021

@author: HMFR
"""
#boolian variables
truebool = True
falsebool = False

print(truebool,falsebool)

# compare
is2equal3 = 2==3
print('2 is equal 3 is {}'.format(is2equal3))

noteq = 2 != 3
print('2 is not equal  3 is {}'.format(noteq))

#operations
print(52>2)
print(52==52)
print(52!=53)

#and or not
print(2>1 and 5==2+3)
print(not False)
print(2<1 and 5==2 or 6!=1000)

# order of decison: 1.not 2.or 3.and
print(2<1 and 5==2 or 6!=1000 and not 5<2 )

#conditional
age = 110
if age > 80:
    print('he is old')
elif age < 15:
    print('go play football')
else:
    print('you have lots of time to be a programmer')