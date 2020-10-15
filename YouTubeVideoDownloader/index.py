############ VARS ############
initialise = {}
toImport  =  {'youtube_dl':'','requests':''}
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
def Intro():
    print(colored('Welcome to Connor\'s Youtube Video Downloader!','green')+colored(' V0.1','magenta'))
    print(colored('\nEnter Download Location (Leave Blank For Defult)','cyan'))
    
    print('\n'+colored('Enter Video Link to start!','blue'))
def CheckLink(URL):
    if URL == False:
        quit()
    else:
        return URL
def URLparse(url):
    return url.split('?v=')[1]
def URLdataGet(URL):
    data = requests.get(URL)
    return str(data.content)
def YoutubeDownload(VideoID,Download):
    try:
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
        with ydl:
            result = ydl.extract_info(VideoID,download=Download)
            return result
    except:
        return False
def GetUserLink():
    UserLink = input(colored('>>> ','green'))
    try:
        Link = str(UserLink)
        VideoData = YoutubeDownload(URLparse(Link),False)
        if VideoData != False:
            print(colored("Is this the video you want? ",'cyan')+colored(str(VideoData['title']),'magenta')+colored(' (Y/N)','blue'))
            UserInput = str(input(colored('>>> ','green'))).lower()
            if UserInput == 'y':
                return Link
            else:
                return False
        else:
            print(colored('Invalid Link...','red'))
            return GetUserLink()
    except:
        print(colored('Invalid Link...','red'))
        return GetUserLink()
####### MAIN FUNCTION #######
def main():
    Intro()
    YoutubeDownload(URLparse(CheckLink(GetUserLink())),True)
if __name__ == "__main__":
    main()