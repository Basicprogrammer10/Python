import string
nounout = []

file = open('ColorGenerator/Nouns.txt', 'r')
nounin = file.readlines()
file.close()

for i in range(len(nounin)):
    nounout.append(string.capwords(nounin[i]))

file = open('ColorGenerator/NounCap.txt', 'w')
file.write(str(nounout))
file.close()
