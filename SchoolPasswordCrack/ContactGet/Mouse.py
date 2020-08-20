import mouse,time,keyboard
############ VARS ############
cps = 1

autoEat = False
limit = 3000

running = False
i = 0
##############################

while True:
    if running:
        time.sleep(1/cps)
        mouse.click('left')
        i = i + 1
        if keyboard.is_pressed('k'):
            running = False
        if i == limit:
            i = 0
            mouse.hold('right')
            time.sleep(5)
            mouse.release('right')
    else:
        if keyboard.is_pressed('j'):
            running = True