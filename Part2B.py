#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import crypt
import io
import datetime

start = datetime.datetime.now()#start timing the program
print("STARTED")#have this print just so I can know the program started
listOfWords = list()#list that will hold the words found in the text file

#this part reads the 'words.txt' file and stores them
with io.open('words.txt', "r") as f: 
    for password in f: 
        word1 = password
        listOfWords.append(word1.rstrip())#.rstrip() to get rid of the \n
        
#lines and users will hold the users and their hashed passwords from 'UnsaltedPassTable.txt'
lines = list()
users = list()
salts = list()

with io.open("SaltedPassTable.txt", "r") as f:#reads the file that I made that has pairs of words and stores it in lines
    for line in f.readlines():
        ind = line.find(":")#find the index of : which is where the username and hashed password are split
        word1 = line[:ind]#creates the user word
        word2 = line[ind + 1:ind + 9]#creates the salts
        salts.append(word2.strip())#add the password to lines
        users.append(word1)#adds the user to users
        lines.append(line)
        
        
print(salts[0])
print(users[0])
print(lines[0])

numbers = list(range(0,100000000))#create a list up to 8 digit long numbers

#convert the numbers to strings
for i in range(len(numbers)):
     numbers[i] = str(numbers[i])
        
hashed = crypt.crypt("16083058", salts[0])

print(hashed)

var = ("16083058" + "JLELZRph").encode('UTF-8')
hashed2 = hashlib.md5(var).hexdigest()

print(hashed2)
            
#Number passwords
#for i in range(len(salts)):
#    for j in range(9999999, len(numbers)):
#        if(numbers[j] == "16083058"):
#            print("found the number")
#        #var = (numbers[j]).encode('ISO-8859-1')
#        hashed = crypt.crypt(numbers[j], salts[i])#hashed = hashlib.md5(var).hexdigest()#create hashed password
#        if(hashed == lines[i]):#see if there is a match
#            print(users[i], numbers[j])#print result
#            #newUserList.append(newnewlist[i])#add the found user to the newUsersList
#            break

#for i in range(len(listOfWords)):
#    for j in range(len(salts)):
#        #var = (listOfWords[j]).encode('ISO-8859-1')
#        hashed = crypt.crypt(listOfWords[i], salts[j])#hashlib.md5(var).hexdigest()#create hashed password
#        if(any(hashed in string for string in lines)):#hashed == lines[i]):#see if there is a match
#            print(users[j], listOfWords[i])#print result
#            #newUserList.append(users[i])#add the found user to the newUsersList
#            break


# In[ ]:





# In[ ]:




