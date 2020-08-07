from pynput.mouse import Listener
import time, threading
#print(clicktime)

clicks = 0

def on_click(x, y, button, pressed):
    global clicks
    if pressed:
        clicks=clicks+1
def start():        
    with Listener(on_click=on_click) as listener:
        listener.join()

x = threading.Thread(target=start, args=())
x.start()

while True:
    clicktime = time.time()
    #print(str(round(clicktime,0)) + " | " + str(round(time.time(),0)))
    if str(round(clicktime+1,0)) == str(round(time.time(),0)):
        print(str(clicks))
        clicks = 0