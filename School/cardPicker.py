############ VARS ############
Num  = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
Face = {'Clubs':'Squats', 'Diamonds':'Bear Crawls', 'Hearts':'Jumping Jacks', 'Spades':'Reverse Crunches'}

initialise = {}
toImport  =  {'random':'*'}
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
def getNum(Num):
    return Num[randint(0,len(Num)-1)]

def getFace(Face):
    return list(Face)[randint(0,len(Face)-1)]
####### MAIN FUNCTION #######
def main():
    cards = []
    for i in range(10):
        a = getNum(Num)
        b = getFace(Face)
        print(colored(a+' of '+b+' - '+a+' '+Face[b],'green'))
if __name__ == "__main__":
    main()