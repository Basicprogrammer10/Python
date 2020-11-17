############ VARS ############
DEBUG = True

toImport = {'urllib.request': '', 'datetime': 'datetime',
            'sys': '', 'bs4': 'BeautifulSoup', 'urllib.parse': 'urlparse'}
########### SETUP ###########
for i in toImport:
    defult = False if toImport[i] != '' else True
    exec(str('from ' if defult == False else 'import ')+str(i) +
         str(' import ' + toImport[i] if defult == False else ''))


def colored(text, color):
    ColorCodes = {'black': '30', 'red': '31', 'yellow': '33', 'green': '32', 'blue': '34',
                  'cyan': '36', 'magenta': '35', 'white': '37', 'gray': '90', 'reset': '0'}
    return '\033[' + ColorCodes[str(color).lower()] + 'm' + str(text) + "\033[0m"
######### FUNCTIONS #########


def DebugPrint(Catagory, Text, Color):
    if DEBUG == True:
        print(colored('['+datetime.now().strftime("%H:%M:%S")+'] ', 'yellow') +
              colored('['+Catagory+'] ', 'magenta')+colored(Text, Color))


def getUrl():
    global url
    try:
        url = str(sys.argv[1])
    except IndexError:
        DebugPrint('Startup', 'Please Give Safe share URL', 'red')
        exit()


def doDataGet(url, data, headers):
    DebugPrint('Data Get', '   Downloading Webpage: \033[34m'+url, 'cyan')
    try:
        req = urllib.request.Request(url, data=data, headers=headers)
        data = urllib.request.urlopen(req)
        DebugPrint('Data Get', '   Download Complete!', 'green')
        return data
    except:
        DebugPrint('Data Get', '   Error Downloading Webpage', 'red')
        exit()


def youtubeParse(data):
    DebugPrint('Data Parse', ' Starting Data Parse', 'cyan')
    try:
        soup = BeautifulSoup(data, features="lxml")
        parse = urlparse(soup.find_all(id="iframe-embed")[0].get('src'))
        parse = parse[4].split('&')[0].split('=')[1]
        DebugPrint('Data Parse', ' Done Parsing: \033[34m'+parse, 'green')
        return parse
    except:
        DebugPrint(
            'Data Parse', ' Error Parsing Webpage \033[34m(Make sure it is a SafeShare Link)', 'red')
        exit()
####### MAIN FUNCTION #######


def main():
    getUrl()
    data = doDataGet(url, None,
                     {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}).read()
    result = youtubeParse(data)
    print()
    DebugPrint(
        'Result', '     Youtube Link:\033[34m https://www.youtube.com/watch?v='+result, 'green')


if __name__ == "__main__":
    main()
