import smtplib
import ssl
import random
from datetime import date

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "sladefoodbot@gmail.com"
#receiver_email = ["turtleslade@gmail.com", "connorslade@email.com", "4jackslade@gmail.com"]
receiver_email = ["turtleslade@gmail.com"]
password = "74DiMmTZkAgxPPJLBidJZATVCD4xDjVSzJXG52NTTf7M6MKXJ5u5chyD8cVq6wMzNsuTSoPQCQj2DDsmizeXbcFNu4mAzLq63rea"

def rem(filename,excludedWord):
    f = open(filename,'r')
    lines = f.readlines()
    f.close()

    nose = 1
    newLines = []
    for line in lines:
        if nose == 0:
            newLines.append(' '.join([word for word in line.split() if word != excludedWord]))
        else:
            newLines.append(' '.join([word for word in line.split()]))

        if excludedWord in newLines:
            nose = 1
    f = open(filename, 'w')
    for line in lines:
        f.write("{}\n".format(line))
    f.close()
my_file = open("food/Dessert.nose", "r")
dessert = my_file.read()
dessert = dessert.split('\n')
drand = random.randint(0, len(dessert)-1)
#rem("food/Dessert.nose",dessert[drand])

my_file = open("food/Protein.nose", "r")
protein = my_file.read()
protein = protein.split('\n')
prand = random.randint(0, len(protein)-1)

my_file = open("food/Breakfast.nose", "r")
breakfast = my_file.read()
breakfast = breakfast.split('\n')
brand = random.randint(0, len(breakfast)-1)

my_file = open("food/Veggie.nose", "r")
veggie = my_file.read()
veggie = veggie.split('\n')
vrand = random.randint(0, len(veggie)-1)

my_file = open("food/Grain.nose", "r")
grain = my_file.read()
grain = grain.split('\n')
grand = random.randint(0, len(grain)-1)


def debug():
    print(prand)
    print(vrand)
    print(grand)
    print(drand)


message = """\
Subject: Dinner For """+str(date.today())+"""

Today ("""+str(date.today())+""") for dinner you will be having the following...

Protein: """+protein[prand]+"""

Veggie: """+veggie[vrand]+"""

Grain: """+grain[grand]+"""

Dessert: """+dessert[drand]+"""
"""

print(message)


def sendmail(sender_email, message, password, receiver_email):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        for i in receiver_email:
            server.sendmail(sender_email, i, message)

#sendmail(sender_email, message, password, receiver_email)