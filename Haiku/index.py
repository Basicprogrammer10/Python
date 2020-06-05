import random

words = {'nose':1,'cat':1,'dog':1,'noser':2,'apple':2}


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
        
print(nose(words,5))
print(nose(words,7))
print(nose(words,5))