import random
import csv 
import time
import progressbar
  
filename ="words.csv"

with open(filename, 'r') as data: 
      
    for line in csv.DictReader(data): 
        words = line 

#words = {'nose':1,'cat':1,'dog':1,'noser':2,'apple':2}


def nose(words,sila):
    wordlist = []
    for x in words:
        wordlist.append(x)

    sil = 0
    line = []

    for i in wordlist:
        x = random.randint(0,len(wordlist)-1)
        line.append(wordlist[x])
        sil = sil + int(words[wordlist[x]])
        
        if sil == sila:
            return line
        elif sil > sila:
            return nose(words, sila)
        else:
            pass


f = open("Haiku.nose", "a")
linelen = [5,7,5]
for c in progressbar.progressbar(range(100000)):
    for a in linelen:
        for i in nose(words,a):
            f.write(i+' ')
        f.write('\n')
    f.write('----------\n')
f.close()