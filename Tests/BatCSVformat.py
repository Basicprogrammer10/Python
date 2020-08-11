import datetime, time
############ VARS ############
Input = 'data.csv'
Output = 'FormatedData.csv'

initialise = {'working':'a','data':'a'}
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
        print(i)
        working.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i[0])))))
    print(working)
def WriteData(outFile,data):
    pass
####### MAIN FUNCTION #######
def main():
    ConvertTime(ReadData(Input))
if __name__ == "__main__":
    main()