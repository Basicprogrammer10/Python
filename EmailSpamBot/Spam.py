from datetime import date
from datetime import datetime
from termcolor import colored
import os
import random
import smtplib
import ssl
import time

password = "notaspambot@protonmail.com"
port = 587
smtp_server = "smtp.yandex.com"
sender_email = "maxspam227@yandex.com"
receiver_email = ["turtleslade@gmail.com", "connorslade@email.com"]

message = """\
Subject: Dinner For """+str(date.today())+"""

Hello World!!


"""

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
