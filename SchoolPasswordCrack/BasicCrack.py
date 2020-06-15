import random
file = open("BAD-passwords.nose", 'a')

for i in range(1):
    x = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    #file.write(str(30)+x+'\n')
    print(str(30)+x)
