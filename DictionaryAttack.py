#import hashlib
import crypt


listOfWords = list()

with open('commonPasswdFile.txt', "r", encoding = "ISO-8859-1") as f: 
    for password in f: 
        word1 = password
        listOfWords.append(word1.rstrip())#should I use the rstrip() cause that gets rid of the \n and idk if it was hashed with \n in mind

saltv = "$1$l3RgvDgR$"
#var = (listOfWords[0] + saltv).encode('utf-8')
#hashed = hashlib.md5(var).hexdigest()
hashed = crypt.crypt("123456", salt = saltv)
#print(listOfWords[0])
#.jp4EA47X38Yny8reSbi71
print(hashed)

#print(hashed)

############################

lines = list()
salts = list()#list to hold the salts

with open("shadowfile copy.txt", "r") as f:#reads the file that I made that has pairs of words and stores it in lines
    #lines = f.readlines()
    
    for line in f.readlines()[2:]:
        ind = line.find("$1$")
        word1 = line[ind + 3:ind + 11]#creates first word
        salts.append(word1)
        lines.append(line)
        
##############################

#for i in range(len(listOfWords)):
#    for j in range(len(salts)):
#        var = (listOfWords[i] + salts[j]).encode('utf-8')
#        hashed = hashlib.md5(var).hexdigest()
#        #print(hashed)
#        if(any(hashed in string for string in lines)):
#            print("yuh")
