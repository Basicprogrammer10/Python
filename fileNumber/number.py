import os
num = 1
for filename in os.listdir("."):
    os.rename(filename, str(num)+'.jpg')
    num = num + 1