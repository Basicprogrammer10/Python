import datetime
############ VARS ############
Output = 'batterytest.nose'
CsvExport = 'data.csv'
#Delay = '60000'
Delay = '1000'

initialise = {'working':'a'}
toImport = {'time':'','os.path':'','psutil':'','datetime':'datetime'}
########### SETUP ###########
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
    elif initialise[i] == 'a':
        exec(str(i)+'=[]')
    else:
        pass
def colored(text, color):
    code = 'ERROR'
    if color == 'blue':
        code = '\033[34m'
    elif color == 'yellow':
        code = '\033[33m'
    elif color == 'cyan':
        code = '\033[36m'
    elif color == 'magenta':
        code = '\033[35m'
    elif color == 'red':
        code = '\033[31m'
    elif color == 'green':
        code = '\033[32m'
    elif color == 'reset':
        code = '\033[0m'
    return code + str(text) + "\033[0m"
######### FUNCTIONS #########
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def wait(TimeInMs):
    '''Waits...'''
    time.sleep(int(TimeInMs)/1000)
def FileCheck(FileName):
    if os.path.isfile(FileName):
        return 1
    else:
        return 0
def FileWrite(FileName,Data):
    try:
        open(Output,'a').write(Data)
        return 0
    except:
        return 1
def GetTime():
    '''Returns UNIX time in MS'''
    return int(time.time())*1000
def CsvExportData(data,CsvExport):
    try:
        os.remove(CsvExport)
    except:
        pass
    file = open(CsvExport,'a')
    for i in data:
        try:
            file.write(str(i[0])+','+str(i[1])+'\n')
        except IndexError:
            pass
def Init(Filename,CsvExport):
    cls()
    print(colored("Statring...",'green'))
    if True if FileCheck(Filename) == 0 else False:
        print(colored("Createing: ",'magenta') + colored(Filename,'blue'))
        FileWrite(Filename,'~~Battery Test Data - For ConnorsBatteryTester~~\n')
    else:
        print(colored(Filename,'blue') + colored(" already exists",'magenta'),end=' ')
        if True if str(input(colored("Would you like to overwright it ",'magenta')+colored("(Y/N) ",'magenta'))).lower() == 'y' else False:
            os.remove(Filename)
            FileWrite(Filename,'~~Battery Test Data - For ConnorsBatteryTester~~\n')
        else:
            data = open(Filename,'r').readlines()
            if data[0] == '~~Battery Test Data - For ConnorsBatteryTester~~\n':
                print(colored("\nFormatting Data",'green'))
                working = []
                for i in data:
                    working.append(i.replace('\n','').split(','))
                cls()
                if True if str(input(colored("Would you like to Export the Test DATA ",'magenta')+colored("(Y/N) ",'magenta'))).lower() == 'y' else False:
                    CsvExportData(working,CsvExport)
                cls()
                print(colored('#################### RESULTS ####################','yellow'))
                print(colored("Start Time:   ", 'blue') + colored(datetime.utcfromtimestamp(int(working[1][0])/1000).strftime('%Y-%m-%d %H:%M:%S') + ' (' + str(int(working[1][0])/1000) + ')','magenta'))
                print(colored("End Time:     ", 'blue') + colored(datetime.utcfromtimestamp(int(working[len(working)-1][0])/1000).strftime('%Y-%m-%d %H:%M:%S') + ' (' + str(int(working[len(working)-1][0])/1000) + ')','magenta'))
                print(colored("Elapsed Time: ", 'blue') + colored(datetime.utcfromtimestamp(int(int(working[len(working)-1][0])/1000) - int(working[1][0])/1000).strftime('%H:%M:%S') + ' (' + str(int(working[len(working)-1][0])/1000 - int(working[1][0])/1000) + ')', 'magenta'))

                #print(working)#FIXME:
            else:
                print(colored("Exiting...",'red'))
            quit()
####### MAIN FUNCTION #######
def main():
    Init(Output,CsvExport)
    print(colored("Starting Testing!\n\n",'green'))
    while True:
        wait(int(Delay)-500)
        print(colored('Logging','cyan'),end='\r')
        FileWrite(Output,str(str(GetTime()) +','+ str(psutil.sensors_battery().percent)+'\n'))
        wait(500)
        print(colored('          ','cyan'),end='\r')
if __name__ == "__main__":
    main()