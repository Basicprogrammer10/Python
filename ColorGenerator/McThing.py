############ VARS ############
WordFile = 'Nouns.txt'
Output = 'Minecraft.txt'
words = 1000

initialise = {'working':'[]'}
toImport  =  {'random':''}
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
def ReadWords(File):
    working = []
    data = open(File).readlines()
    for i in data:
        working.append(i.replace('\n',''))
    return working
def MixWords(data,limit):
    working = []
    for i in range(limit):
        working.append(str(data[random.randint(0,len(data)-1)])+' '+str(data[random.randint(0,len(data)-1)]))
    return working
def WrightWords(data,output):
    for i in data:
        open(output,'a').write(i+'\n')
####### MAIN FUNCTION #######
def main():
    WrightWords(MixWords(ReadWords(WordFile),words),Output)
if __name__ == "__main__":
    main()