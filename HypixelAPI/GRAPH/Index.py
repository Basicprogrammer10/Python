import csv
############ VARS ############
player = 'Delta68'
dataAPIurl = 'http://mc.connorcode.com:8888/'
initialise = {'working':'s','x':'a','y':'a','y2':'a','y3':'a'}
toImport = {'random':'','matplotlib.pyplot':'','urllib.request':''}
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
plt = matplotlib.pyplot
######### FUNCTIONS #########
def plot(x,y,y2):
    '''Plots some Data'''
    plt.plot(x,y, x,y2)
    plt.show()
def dataGet(dataAPIurl,player):
    '''Gets Data'''
    DataGetURL = dataAPIurl + player.lower() + '.csv'
    update_code = urllib.request.urlopen(DataGetURL)
    code_string = update_code.read().decode()
    return code_string
def parseCSVdata(data):
    '''Parses a CSV2 File...'''
    datas = data.split('\n')
    all_data = []
    for i in datas:
        all_data.append(i.split(","))
    for i in range(len(all_data)-1):
        #x.append(all_data[i][5])
        y.append(i)

        try:
            y2.append(int(all_data[i][1])/int(all_data[i][2]))
        except:
            y2.append(0)
    final = [x,y,y2]
    return final
def main():
    data = parseCSVdata(dataGet(dataAPIurl,player))
    plot(data[0],data[1],data[2])

if __name__ == "__main__":
    main()