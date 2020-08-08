############ VARS ############
OpenFile = ''
CloseFile = 'output2.csv'
initialise = {'working':'s','index':'a','name':'a','f_name':'a','l_name':'a','email':'a','extra':'a'}
toImport = {'random':'','csv':''}
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
    elif initialise[i] == 'a':
        exec(str(i)+'=[]')
    else:
        pass
######### FUNCTIONS #########
def DataGetFromFile(FileName):
    return open(FileName,'r').read()
def parseCSVdata(data):
    '''Parses a CSV2 File...'''
    datas = data.split('\n')
    all_data = []
    for i in datas:
        all_data.append(i.split(","))
    for i in range(len(all_data)-1):
        index.append(i)
        name.append(all_data[i][0])
        f_name.append(all_data[i][1])
        l_name.append(all_data[i][3])
        email.append(all_data[i][30])
        extra.append(all_data[i][34])
    final = [index,name,f_name,l_name,email,extra]
    return final
def NewCsvWrite(data):
    with open(CloseFile,'a') as file:
        for i in data[0]:
            file.write(str(data[0][i])+','+str(data[1][i])+','+str(data[2][i])+','+str(data[3][i])+','+str(data[4][i])+','+str(data[5][i])+'\n')
def FindPasswords(data):
    with open(CloseFile,'a') as file:
        for i in data[0]:
            if str(data[5][i]) != '':
                if str(data[5][i]) != '#':
                    file.write(str(data[0][i])+','+str(data[1][i])+','+str(data[2][i])+','+str(data[3][i])+','+str(data[4][i])+','+str(data[5][i])+'\n')
def main():
    #print(DataGetFromFile('RAW_DATA.csv'))
    data = parseCSVdata(DataGetFromFile('RAW_DATA.csv'))
    #NewCsvWrite(data)
    FindPasswords(data)

if __name__ == "__main__":
    main()