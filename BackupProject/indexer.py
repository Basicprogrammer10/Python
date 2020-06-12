import os

with open("files.nose", "a") as f:
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            f.write(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            f.write(os.path.join(dirname, filename))
