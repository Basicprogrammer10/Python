import string
from random import *
char=100
allchar = string.allchar
password = "".join(choice(allchar) for x in range(char))
print(password)