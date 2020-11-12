############ VARS ############
configFile = "config.cfg"

toImport = {'win10toast': 'ToastNotifier',
            'time': '', 'configparser': '', 'os': ''}
########### SETUP ###########
for i in toImport:
    defult = False if toImport[i] != '' else True
    exec(str('from ' if defult == False else 'import ')+str(i) +
         str(' import ' + toImport[i] if defult == False else ''))


def colored(text, color):
    ColorCodes = {'black': '30', 'red': '31', 'yellow': '33', 'green': '32', 'blue': '34',
                  'cyan': '36', 'magenta': '35', 'white': '37', 'gray': '90', 'reset': '0'}
    return '\033[' + ColorCodes[str(color).lower()] + 'm' + str(text) + "\033[0m"


def cls(do):
    if do:
        os.system('cls' if os.name == 'nt' else 'clear')
######### FUNCTIONS #########


def configRead(configFile):
    global logFile, text, index, doClear, delay
    config = configparser.ConfigParser()
    config.read(configFile)
    logFile = config.get('Main', 'logFile')
    text = config.get('Main', 'text')
    index = int(config.get('Main', 'index'))
    delay = int(config.get('Main', 'delay'))
    doClear = bool(config.get('Main', 'doClear'))
    autoPath()


def autoPath():
    global logFile
    if logFile.lower() == "auto":
        logFile = os.getenv('APPDATA')+"\\.minecraft\\logs\\latest.log"


def Alert(Title, Text):
    ToastNotifier().show_toast(Title, Text, icon_path="Icon.ico", duration=30)


def GetData(file):
    data = open(file, 'r').read().split('\n')
    if text in data[len(data)-2]:
        return data[len(data)-2].split(text + ' ')[1]
    else:
        return False

####### MAIN FUNCTION #######


def main():
    configRead(configFile)
    working = ''
    while True:
        data = GetData(logFile)
        if int(data) < index and data != working and data != False:
            working = data
            cls(doClear)
            print(colored('2B2T QUEUE: '+str(data), 'green'))
            Alert("2B2T QUEUE", "Posion: " + str(data))
        elif data != working and data != False:
            cls(doClear)
            print(colored('2B2T QUEUE: '+str(data), 'yellow'))
        time.sleep(delay)


if __name__ == "__main__":
    main()
