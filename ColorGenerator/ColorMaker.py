import random
colors = []
file = open('Nouns.txt', 'r')
noun = file.readlines()
file.close()
file = open('Colors.txt', 'r')
color = file.readlines()
file.close()

file = open('NewColors.txt', 'w')
for i in range(1000000):
    print(i)
    if str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)]) not in colors:
        file.write(str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)]))
        colors.append(str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)]))
        file.write("----------\n")
file.close()