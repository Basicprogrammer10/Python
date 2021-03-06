import datetime, time
############ VARS ############
Input = 'data.csv'
Output = 'FormatedData.csv'

initialise = {'working':'a','data':'a','a':'i'}
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
def ReadData(FileName):
    working = open(FileName,'r').readlines()
    for i in working:
        data.append(i.replace('\n','').split(','))
    return data
def ConvertTime(data):
    for i in data:
        working.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i[0])/1000))))
    return working
def MergeData(time,main):
    a = 0
    for i in main:
        b = str(time[a]) +','+ str(main[a][1])
        working.append(b.split(','))
        a = a + 1
    return working

def WriteData(outFile,data):
    file = open(outFile,'a')
    for i in data:
        file.write(i[0] + ',' + i[1] + '\n')
####### MAIN FUNCTION #######
def main():
    data = ReadData(Input)
    WriteData(Output, MergeData(ConvertTime(data),data))
if __name__ == "__main__":
    main()