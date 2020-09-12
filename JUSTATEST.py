#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:50:03 2020

@author: jonmunoz
"""
import hashlib
import crypt
import io


listOfWords = list()

with io.open('words.txt', "r", encoding = "ISO-8859-1") as f: 
    for password in f: 
        word1 = password
        listOfWords.append(word1.rstrip())
            
lines = list()
users = list()

with io.open("UnsaltedPassTable.txt", "r") as f:#reads the file that I made that has pairs of words and stores it in lines
    for line in f.readlines():
        ind = line.find(":")
        word1 = line[:ind]#creates first word
        lines.append(line)
        users.append(word1)
        

for i in range(len(listOfWords)):
    for j in range(len(users)):
        try:
            var = (listOfWords[i]).encode('ISO-8859-1')
            hashed = hashlib.md5(var).hexdigest()
            if(any(hashed in string for string in lines)):
                print(users[j], listOfWords[i])
        except:
            pass
