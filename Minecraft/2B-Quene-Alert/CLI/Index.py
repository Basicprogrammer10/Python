############ VARS ############
configFile = "config.cfg"

toImport = {'win10toast': 'ToastNotifier', 'time': '', 'configparser': '', 'os': ''}
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
        print(do)
        os.system('cls' if os.name == 'nt' else 'clear')

######### FUNCTIONS #########


class config():
    def configRead(self, configFile):
        config = configparser.ConfigParser()
        config.read(configFile)
        self.logFile = config.get('Main', 'logFile')
        self.text = config.get('Main', 'text')
        self.index1 = int(config.get('Main', 'index1'))
        self.index2 = int(config.get('Main', 'index2'))
        self.delay = int(config.get('Main', 'delay'))
        self.doClear = True if config.get(
            'Main', 'doClear').lower() == 'true' else False
        if self.logFile.lower() == "auto":
            self.logFile = os.getenv('APPDATA') + \
                "\\.minecraft\\logs\\latest.log"


def printColor(data):
    if data <= config.index1:
        return 'green'
    elif config.index1 < data < config.index2:
        return 'yellow'
    elif config.index2 < data:
        return 'red'


def GetData(file):
    data = open(file, 'r').read().split('\n')
    if config.text in data[len(data)-2]:
        if '§' in data[len(data)-2].split(config.text + ' ')[1]:
            for i in data[len(data)-2].split(config.text + ' ')[1].split('§'):
                if len(i) > 1:
                    return i[-(len(i)-1):]
        else:
            return data[len(data)-2].split(config.text + ' ')[1]
    else:
        return False

####### MAIN FUNCTION #######


def main():
    config.configRead(config, configFile)
    working = ''
    while True:
        data = GetData(config.logFile)
        if data != working and data != False:
            cls(config.doClear)
            print(colored('2B2T QUEUE: '+str(data), printColor(int(data))))
            if int(data) <= config.index1:
                ToastNotifier().show_toast("2B2T QUEUE", "Position: " +
                                           str(data), icon_path="Icon.ico", duration=30)
        time.sleep(config.delay)


if __name__ == "__main__":
    main()
