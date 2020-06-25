from datetime import date
from datetime import datetime
from termcolor import colored
import random
import os
import random
import smtplib
import ssl
import time

debug = 0

Hour = random.randint(0,24)
Min = random.randint(0,59)

min = Min
hor = Hour
port = 587
smtp_server = "smtp.gmail.com"
sender_email = "email@domain.com"#Change to sender Email
file = open("SendTo.nose", "r", encoding="ascii",errors='ignore')
receiver_email = file.readlines()
file.close()
print(receiver_email)
password = "Password"#Change to password

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def rem(filename, stopwords):
    file = open(filename, "r", encoding="ascii",errors='ignore')
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
    file = open(filename, "w", encoding="ascii",errors='ignore')
    for element in words:
        file.write(element)
    file.close()


def sendmail():
    my_file = open("Facts.nose", "r", encoding="ascii",errors='ignore')
    dessert = my_file.read()
    dessert = dessert.split('\n')
    drand = random.randint(0, len(dessert)-1)
    rem("Facts.nose", dessert[drand]+'\n')
    message = """\
Subject: Fact of the day for """+str(date.today())+"""                            

Fact of the day: """+dessert[drand]+"""

(This message was sent automatically by Connors Fact Of The Day Bot! There is no way to unsubscribe!)
"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        num = 1
        for i in receiver_email:
            print(colored("Sending ("+str(num)+"/" +str(len(receiver_email))+") "+i+"", 'green'))
            server.sendmail(sender_email, i, message)
            num = num + 1


while True:
    now = datetime.now()
    H = int(now.strftime("%H"))
    h = H
    M = int(now.strftime("%M"))
    m = M
    #cls()
    ct = m + (h * 60)
    ft = min + (hor * 60)
    tp = ft - ct
    print(chr(27) + "[2J")
    if tp < 0:
        pt = tp + 24 * 60
        ph = pt / 60
        pm = pt % 60
        print(colored(str(int(ph)) + ":" + str(pm), 'cyan'), end="\r")
    else:
        pt = tp
        ph = pt / 60
        pm = pt % 60
        print(colored(str(int(ph)) + ":" + str(pm), 'cyan'), end="\r")
    if int(H) == Hour or debug == 1:
        if int(M) == Min or debug == 1:
            print(colored(datetime.now().time(), 'yellow')+" | "+colored("Sending...", 'blue'))

            sendmail()
            print(colored("Done!", 'yellow'))
            Hour = random.randint(0,24)
            Min = random.randint(0,60)
            print("\n")
            time.sleep(65)

    time.sleep(15)