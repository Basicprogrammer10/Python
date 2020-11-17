import datetime
from time import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QtWidgets
import sys
import ctypes
import threading
from PyQt5.QtGui import QIcon


myappid = 'connorcode.2b2t.queueAlert.001'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QApplication(sys.argv)
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
        if '§' in data[len(data)-2].split(text + ' ')[1]:
            for i in data[len(data)-2].split(text + ' ')[1].split('§'):
                if len(i) > 1:
                    return i[-(len(i)-1):]
        else:
            return data[len(data)-2].split(text + ' ')[1]
    else:
        return False

####### MAIN FUNCTION #######


def main():
    configRead(configFile)
    working = ''

    appExexThread = threading.Thread(target=app.exec)
    widget = QWidget()
    layout = QVBoxLayout()'
    Form = QtWidgets.QWidget()
    ui = ui_Form()
    app.setStyle('Fusion')
    # app.setWindowIcon(QIcon('Icon.ico'))
    # app.setStyleSheet("QLabel { color:#13a10e; }")
    # app.setStyleSheet("QLabel { color:#E5AF09; }")
    textLabel = QLabel(widget)
    textLabel.setTextFormat(3)
    textLabel.setText("# Position in queue: 100")
    layout.addWidget(textLabel)
    widget.setLayout(layout)
    widget.setWindowTitle("2B2T Queue Alert | Sigma76")
    data = 100000
    widget.show()
    textLabel.setText("# Position in queue: 99")
    widget.show()
    time.sleep(5)
    while True:
        # data = GetData(logFile)
        data = data - 1
        # if int(data) < index and data != working and data != False:
        #    working = data
        #    cls(doClear)
        #    print(colored('2B2T QUEUE: '+str(data), 'green'))
        #    Alert("2B2T QUEUE", "Posion: " + str(data))
        # elif data != working and data != False:
        if True:
            print(colored('2B2T QUEUE: '+str(data), 'yellow'))
            textLabel.setText("# Position in queue: " + str(data))
            timer = QtCore.QTimer()
            timer.timeout.connect(update_label)
            timer.start(100)  # every 10,000 milliseconds
            widget.show()
        time.sleep(1)
        # sys.exit(app.exec_())


if __name__ == "__main__":
    main()
