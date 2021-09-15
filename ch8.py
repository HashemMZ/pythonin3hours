#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 09:11:30 2021

@author: HMFR
"""

#file I/O
#open(path) opens a file in path; path can be absolute or relative
#absolute paths:from root file system in linux or a drive in win
#ex: /var/log/messages    C:\Log\messages
#relative path from current working dir; ex: /log/messages
#python knows forward slashes as well: c:/log/messages

#open() return file or stream object
hosts = open('/etc/hosts')
#hosts = open('C:/Windows/System32/drivers/etc/hosts') #for Windows

print('-------------------------1')
#read() func to read entire file
hostfile_contents = hosts.read();
print(hostfile_contents)

print('-------------------------2')
#python keeps track of the location in the file
#with read() it goes to the end of file
#tell() shows the location
print(hosts.tell())
print(len(hostfile_contents))
#not always the same. especially in UTF-8, eastern lang and prob Persian

print('-------------------------3')
#now it is at the end of file so there is nothing to read
hostfile_contents = hosts.read();
print(hostfile_contents)

print('-------------------------4')
#seek(offset) func sends to offset byte from the beginning
hosts.seek(0)
print(hosts.tell())

print('-------------------------5')
#read(n) a defined number of bytes
hostfile_contents = hosts.read(10);
print(hostfile_contents)

print('-------------------------6')
#close() a file after use
hosts.close()

print('-------------------------7')
#file object has a boolean attribute called 'closed' to show its situation
print(hosts.closed)

print('-------------------------8')
#use 'with' statement for automatically close file after use and in exceptions
del hosts
with open('/etc/hosts') as hosts:
    hostfile_contents = hosts.read();
    print(hostfile_contents)
print(hosts.closed)

print('-------------------------9')
#reading ONE line at a time with for loop
with open('note.txt') as fileobj:
    for line in fileobj:
        print(line)#no need to read(); for loop does this

print('-------------------------10')
#to remove blank character like CR carriage return and newline use rstrip()
with open('note.txt') as fileobj:
    for line in fileobj:
        print(line.rstrip())
"""
file modes:
r Open for reading (default). 
w Open for writing, truncating the file first. 
x Create a new file and open it for writing.exception if already exists
a Open for writing, appending to the end of the file if it exists. 
b Binary mode. t Text mode (default).
+ Open a disk file for updating (reading and writing).
rb means read binary
ab append binary
"""

print('-------------------------11')
#mode attribute of file object
with open('note.txt') as fileobj:
    print(fileobj.mode)

print('-------------------------12')
#write() function with w mode
with open('note.txt','w') as fileobj:
    fileobj.write('I am Hashem Moradmand')#overwrites the file
    fileobj.write('I am Javad Razavian')
with open('note.txt') as fileobj:
    print(fileobj.read())
    
print('-------------------------13')
# newline char \n linux \r\n for Win
with open('note.txt','w') as fileobj:
    fileobj.write('I am Hashem Moradmand\n')#new line char
    fileobj.write('I am Javad Razavian')
with open('note.txt') as fileobj:
    print(fileobj.read())
  
print('-------------------------14')  
#with binary switch  read() functions considers bytes instead of chars
#binary switch is usu for pictures, videos, compressed files and so on
with open('pig.jpg','rb') as fobj:
    fobj.seek(2)
    fobj.read(4)#read 4 bytes
    print(fobj.tell())

print('-------------------------15')
#working with files is always risky so use try/except
try:
    #opens for reading (default) but does not exist    
    contacts = open('contacts.txt').read() 
except:
    contacts = []
print(len(contacts))
        