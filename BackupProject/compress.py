import tarfile
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('V:/Programming/Python'):
    f.extend(filenames)
    break
print(f)
#tar = tarfile.open("Compressed.tar.gz", "w:gz")
#tar.add("", arcname="TarName")
#tar.close()