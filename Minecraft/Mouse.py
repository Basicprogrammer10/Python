############ VARS ############
cps = 10
autoEat = False
limit = 3000

initialise = {'running':'False','i':'0'}
toImport  =  {'mouse':'','time':'','keyboard':''}
########### SETUP ###########
for i in toImport:
    defult = False if toImport[i] != '' else True
    exec(str('from ' if defult == False else 'import ')+str(i)+str(' import ' + toImport[i] if defult == False else ''))
def colored(text, color):
    ColorCodes = {'black':'30','red':'31','yellow':'33','green':'32','blue':'34','cyan':'36','magenta':'35','white':'37','gray':'90','reset':'0'}
    return '\033[' + ColorCodes[str(color).lower()] + 'm' + str(text) + "\033[0m"
for i in initialise:
    exec(i + '=' + initialise[i])
####### MAIN FUNCTION #######
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