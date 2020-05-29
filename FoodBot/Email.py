from datetime import date
from datetime import datetime
from termcolor import colored
import os
import random
import smtplib
import ssl
import time

debug = 0

Hour = 15
Min = 30

if debug == 1:
    Hour = 19
    Min = 35
min = Min
hor = Hour
port = 587
smtp_server = "smtp.gmail.com"
sender_email = "sladefoodbot@gmail.com"
receiver_email = ["turtleslade@gmail.com", "connorslade@email.com", "4jackslade@gmail.com"]
#receiver_email = ["turtleslade@gmail.com", "connorslade@email.com"]
password = "74DiMmTZkAgxPPJLBidJZATVCD4xDjVSzJXG52NTTf7M6MKXJ5u5chyD8cVq6wMzNsuTSoPQCQj2DDsmizeXbcFNu4mAzLq63rea"


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def rem(filename, stopwords):
    file = open(filename, "r")
    words = file.readlines()
    file.close()
    words2 = []
    nose = 0
    for word in list(words):  # iterating on a copy since removing will mess things up
        if word in stopwords:
            if nose == 0:
                words.remove(word)
                words2.append(word)
            else:
                pass
                # words.append(word)
            # iterating on a copy since removing will mess things up
            for word in list(words2):
                if word in stopwords:
                    nose = 1
    file = open(filename, "w")
    for element in words:
        file.write(element)
    file.close()


def sendmail():
    my_file = open("food/Dessert.nose", "r")
    dessert = my_file.read()
    dessert = dessert.split('\n')
    drand = random.randint(0, len(dessert)-1)
    rem("food/Dessert.nose", dessert[drand]+'\n')

    my_file = open("food/Protein.nose", "r")
    protein = my_file.read()
    protein = protein.split('\n')
    prand = random.randint(0, len(protein)-1)
    rem("food/Protein.nose", protein[prand]+'\n')

    my_file = open("food/Breakfast.nose", "r")
    breakfast = my_file.read()
    breakfast = breakfast.split('\n')
    brand = random.randint(0, len(breakfast)-1)
    rem("food/Breakfast.nose", breakfast[brand]+'\n')

    my_file = open("food/Veggie.nose", "r")
    veggie = my_file.read()
    veggie = veggie.split('\n')
    vrand = random.randint(0, len(veggie)-1)
    rem("food/Veggie.nose", veggie[vrand]+'\n')

    my_file = open("food/Grain.nose", "r")
    grain = my_file.read()
    grain = grain.split('\n')
    grand = random.randint(0, len(grain)-1)
    rem("food/Grain.nose", grain[grand]+'\n')

    message = """\
Subject: Dinner For """+str(date.today())+"""

Today ("""+str(date.today())+""") for dinner you will be having the following...

Protein: """+protein[prand]+"""

Veggie: """+veggie[vrand]+"""

Grain: """+grain[grand]+"""

Dessert: """+dessert[drand]+""""""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        num = 1
        for i in receiver_email:
            print(colored("Sending ("+str(num)+"/" +str(len(receiver_email))+") ("+i+")", 'green'))
            server.sendmail(sender_email, i, message)
            num = num + 1


while True:
    now = datetime.now()
    H = int(now.strftime("%H"))
    h = H
    M = int(now.strftime("%M"))
    m = M
    cls()
    ct = m + (h * 60)
    ft = min + (hor * 60)
    tp = ft - ct
    print(chr(27) + "[2J")
    if tp < 0:
        pt = tp + 24 * 60
        ph = pt / 60
        pm = pt % 60
        print(colored(str(int(ph)) + ":" + str(pm), 'cyan'))
    else:
        pt = tp
        ph = pt / 60
        pm = pt % 60
        print(colored(str(int(ph)) + ":" + str(pm), 'cyan'))
    if int(H) == Hour or debug == 1:
        if int(M) == Min or debug == 1:
            print(colored("Sending...", 'blue'))
            try:
                sendmail()
                print(colored("Done!", 'yellow'))
                time.sleep(65)
            except:
                print(colored("Error...", 'red'))
    time.sleep(15)