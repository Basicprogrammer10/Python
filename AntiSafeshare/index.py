############ VARS ############
DEBUG = True

toImport = {'urllib.request': '', 'datetime': 'datetime',
            'sys': ''}
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
        DebugPrint('Startup', 'Please Give a Supported Link', 'red')
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


def doParse(url, data):
    if 'video.link' in url.lower():
        return youtubeParseVL(data)
    elif 'safeshare.tv' in url.lower():
        return youtubeParseSS(data)
    else:
        DebugPrint(
            'URL', 'Error Parsing URL \033[34m(Make sure it is a Supported Link)', 'red')
        return 0


def youtubeParseSS(data):
    DebugPrint('Data Parse', ' Starting Data Parse \033[33mSafe Share', 'cyan')
    try:
        parse = str(data).split('iframe')[18].split(
            '\\')[3].split('?')[1].split('&')[0].split('=')[1]
        DebugPrint('Data Parse', ' Done Parsing: \033[34m'+parse, 'green')
        return parse
    except:
        DebugPrint(
            'Data Parse', ' Error Parsing Webpage \033[34m(Make sure it is a Supported Link)', 'red')
        exit()


def youtubeParseVL(data):
    DebugPrint('Data Parse', ' Starting Data Parse \033[33mVideo Link', 'cyan')
    try:
        parse = str(data).split('<script>')[2]
        parse = str(parse).split(',')[1].split("'")[1].split('\\')[0]
        DebugPrint('Data Parse', ' Done Parsing: \033[34m'+parse, 'green')
        return parse
    except IndentationError:
        DebugPrint(
            'Data Parse', ' Error Parsing Webpage \033[34m(Make sure it is a Supported Link)', 'red')
        exit()
####### MAIN FUNCTION #######


def main():
    DebugPrint(
        'System', '     Welcome To Anti Safe share! \033[34mVersion: 3', 'white')
    getUrl()
    data = doDataGet(url, None,
                     {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}).read()
    result = doParse(url, data)
    print()
    DebugPrint(
        'Result', '     Youtube Link:\033[34m https://www.youtube.com/watch?v='+result, 'green')


if __name__ == "__main__":
    main()
