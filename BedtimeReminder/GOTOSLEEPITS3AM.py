############ VARS ############
file = 'Times.nose'

initialise = {}
toImport  =  {'time':'gmtime, strftime','datetime':'datetime','win10toast':'ToastNotifier','time':''}
########### SETUP ###########
for i in toImport:
    defult = False if toImport[i] != '' else True
    exec(str('from ' if defult == False else 'import ')+str(i)+str(' import ' + toImport[i] if defult == False else ''))
def colored(text, color):
    ColorCodes = {'black':'30','red':'31','yellow':'33','green':'32','blue':'34','cyan':'36','magenta':'35','white':'37','gray':'90','reset':'0'}
    return '\033[' + ColorCodes[str(color).lower()] + 'm' + str(text) + "\033[0m"
for i in initialise:
    exec(i + '=' + initialise[i])
######### FUNCTIONS #########
def ReadFile(filename):
    return open(filename,'r',encoding='utf-8').read()
def formtFile(data):
    data = data.split('\n')
    working = []
    for i in data:
        working.append(i.split('|'))
    return working
def GetCurrentTime():
    return datetime.now().strftime('%H:%M')
def checktime(checkTimes):
    for i in checkTimes:
        if str(GetCurrentTime()) == str(i[0]):
            return i
def Message(time):
    try:
        ToastNotifier().show_toast("Bed Time Reminder",str("Its "+GetCurrentTime()+ ' | ' +time[1]),icon_path="BED.ico",duration=30)
    except: pass
####### MAIN FUNCTION #######
def main():
    AlertTimes = formtFile(ReadFile(file))
    while True:
        Message(checktime(AlertTimes))
        time.sleep(60)
if __name__ == "__main__":
    main()