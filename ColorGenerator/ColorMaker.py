import random
colors = []
file = open('ColorGenerator/Nouns.txt', 'r')
noun = file.readlines()
file.close()
file = open('ColorGenerator/Colors.txt', 'r')
color = file.readlines()
file.close()

file = open('ColorGenerator/NewColors.txt', 'w')
#color = file.readlines()
for i in range(1000):
    if str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)]) not in colors:
        file.write(str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)]))
        colors.append(str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)]))
        file.write("----------\n")
file.close()