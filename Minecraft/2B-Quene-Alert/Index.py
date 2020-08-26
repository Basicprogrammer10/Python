############ VARS ############
Index = 50
LogFile = "C:\\Users\\turtl\\Software\\MultiMC\\instances\\1.12.2\\.minecraft\\logs\\latest.log"

initialise = {}
toImport  =  {'win10toast':'ToastNotifier','time':''}
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
def Alert(Title,Text):
    ToastNotifier().show_toast(Title,Text,icon_path="Clock.ico",duration=30)
def GetData(file):
    data = open(file,'r').read().split('\n')
    if "[CHAT] Position in queue:" in data[len(data)-2]:
        return data[len(data)-2].split('[CHAT] Position in queue: ')[1]
    else:
        return 0

####### MAIN FUNCTION #######
def main():
    working = ''
    while True:
        data = GetData(LogFile)
        if int(data) < Index and data != working:
            working = data
            print(colored('2B2T QUEUE: '+str(data),'green'))
            Alert("2B2T QUEUE","Posion: " + str(data))
        elif data != working:
            print(colored('2B2T QUEUE: '+str(data),'yellow'))
        time.sleep(5)
if __name__ == "__main__":
    main()