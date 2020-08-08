############ VARS ############
Textfile = 'text.nose'
initialise = {'working':'s'}
toImport = {'easygui':'*','psutil':'','os':'','time':''}
##############################
for i in toImport:
    if toImport[i] == '':
        exec('import '+i)
    else:
        exec('from '+i+' import '+toImport[i])
for i in initialise:
    if initialise[i] == 's':
        exec(str(i)+'=""')
    elif initialise[i] == 'i':
        exec(str(i)+'=0')
    elif initialise[i] == 'b':
        exec(str(i)+'=None')
    else:
        pass
def ask(message,title):
    if ccbox(message,title):
        return True
    else:
        return False
def getTextLine(file,line):
    global working
    text = open(file,'r', encoding="utf-8").readlines()[line]
    working = str(text.replace('"','')).replace(str('\n'),'')
    if '#' in working:
        getTextLine(file,line+1)
    else:
        return working
def isRunning(program):
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
        except:
            pass
        if p.name() == program:
            return True
    return False
def removeDir(path):
    os.system(path)
def main():
    while True:
        if isRunning('Zoom.exe'):
            if ask(getTextLine(Textfile,2),getTextLine(Textfile,1)):
                removeDir("%appdata%\\Zoom\\uninstall\\Installer.exe")
            else:
                pass
        time.sleep(5)

if __name__ == "__main__":
    main()