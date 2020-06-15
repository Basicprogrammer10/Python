import random
import progressbar
file = open("BAD-passwords.nose", 'a')
output = []
for i in progressbar.progressbar(range(100000)):
    x = str(random.randint(0, 9))+str(random.randint(0, 9)) + \
        str(random.randint(0, 9))+str(random.randint(0, 9))
    y = str(30)+x+'\n'
    if y not in output:
        file.write(y)
        output.append(y)
    else:
        pass
