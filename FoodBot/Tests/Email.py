import smtplib, ssl
from datetime import date

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "sladefoodbot@gmail.com"
receiver_email = ["turtleslade@gmail.com", "connorslade@email.com", "4jackslade@gmail.com"]
password = "74DiMmTZkAgxPPJLBidJZATVCD4xDjVSzJXG52NTTf7M6MKXJ5u5chyD8cVq6wMzNsuTSoPQCQj2DDsmizeXbcFNu4mAzLq63rea"
message = """\
Subject: Dinner For """+str(date.today())+"""

Today ("""+str(date.today())+""") for dinner you will be having the following...

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

sendmail(sender_email, message, password, receiver_email)