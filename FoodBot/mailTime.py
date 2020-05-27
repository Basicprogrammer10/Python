from datetime import datetime
import time

Hour = 15
Min = 0

def now():
    import Email

while True:
    now = datetime.now()
    H = now.strftime("%H")
    M = now.strftime("%M")
    if int(H) == Hour:
        if int(M) == Min:
            now()
            time.sleep(65)
