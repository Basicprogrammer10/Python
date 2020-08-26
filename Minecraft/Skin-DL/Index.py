############ VARS ############
DEBUG = True
OutputFile = 'Skin.png'
Name = 'Sigma76'
shellFunctions = ['nameuuid','exit']
toImport  =  {'base64':'','requests':'','json':'','time':'gmtime, strftime, time','PIL':'Image','re':'','datetime':'datetime'}
########### SETUP ###########
for i in toImport:
    defult = False if toImport[i] != '' else True
    exec(str('from ' if defult == False else 'import ')+str(i)+str(' import ' + toImport[i] if defult == False else ''))
def colored(text, color):
    ColorCodes = {'black':'30','red':'31','yellow':'33','green':'32','blue':'34','cyan':'36','magenta':'35','white':'37','gray':'90','reset':'0'}
    return '\033[' + ColorCodes[str(color).lower()] + 'm' + str(text) + "\033[0m"
######### FUNCTIONS #########
def DebugPrint(Catagory,Text,Color):
    if DEBUG == True:
        print(colored('['+datetime.now().strftime("%H:%M:%S")+'] ','yellow')+colored('['+Catagory+'] ','magenta')+colored(Text,Color))
def APIdataGet(UUID):
    DebugPrint('Mojang API','Requesting Infomation for UUID: \033[34m' + str(UUID),'cyan')
    data = requests.get('https://sessionserver.mojang.com/session/minecraft/profile/'+UUID)
    if data.status_code == 200:
        DebugPrint('Mojang API','Success','green')
        return data.text
    else:
        DebugPrint('Mojang API','Error: ' + data.status_code,'red')
        return None
def Base64DECODE(data):
    DebugPrint('Base64 Decode','Decodeing...','cyan')
    base64_bytes = data.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decode = message_bytes.decode('ascii')
    DebugPrint('Base64 Decode','Finished Decodeing','green')
    return decode
def JsonParse(data):
    return json.loads(data)
def SkinDL(File,SkinURL):
    if File == None:
        DebugPrint('Skin DL','No Output File','red')
        exit()
    DebugPrint('Skin DL','Downloading Skin','cyan')
    skin = requests.get(SkinURL)
    open(File,'wb').write(skin.content)
    DebugPrint('Skin DL','Download Complete','green')
def NametoUUID(Name):
    DebugPrint('Mojang API','Name to UUID: \033[34m'+Name,'cyan')
    data = requests.get('https://api.mojang.com/users/profiles/minecraft/'+Name)
    DebugPrint('Mojang API','Done!','green')
    try:
        return JsonParse(data.text)['id']
    except:
        DebugPrint('Mojang API','Player Not Found','red')
def UUIDtoName(UUID):
    DebugPrint('Mojang API','UUID to Name: \033[34m'+UUID,'cyan')
    data = requests.get('https://api.mojang.com/user/profiles/'+UUID+'/names')
    DebugPrint('Mojang API','Done!','green')
    try:
        return JsonParse(data.text)[len(data)-1]['name']
    except:
        DebugPrint('Mojang API','Player Not Found','red')
def ImageOpen(FileName):
    DebugPrint('Image Open','Opening Image','cyan')
    im = Image.open(FileName)  
    im.show()
    DebugPrint('Image Open','Image Opend!','green')
###### Shell FUNCTIONS ######
def exit(user):
    DebugPrint('Shell','Exiting...','red')
    quit()
def nameuuid(user):
    uuid = user[1]
    if len(uuid) <= 16:
        DebugPrint('NameUUID',NametoUUID(uuid),'white')
    elif len(uuid) > 16:
        DebugPrint('NameUUID',UUIDtoName(uuid),'white')
####### MAIN FUNCTION #######
def main():
    #SkinDL(OutputFile if 'OutputFile' in globals() else None,JsonParse(Base64DECODE(JsonParse(APIdataGet(NametoUUID(Name)))['properties'][0]['value']))['textures']['SKIN']['url'])
    while True:
        try:
            userin = str(input(colored("\n>>>", 'green')))
        except:
            exit([])
        PATTERN = re.compile(r'''((?:[^;"']|"[^"]*"|'[^']*')+)''')
        user = PATTERN.split(userin)[1::2]
        command = user[0].lower()
        if command in shellFunctions:
            exec(command+'('+str(user)+')')
        else:
            DebugPrint('Shell','\033[34m"'+command+'" \033[31mis not a Valid Command','red')
if __name__ == "__main__":
    main()