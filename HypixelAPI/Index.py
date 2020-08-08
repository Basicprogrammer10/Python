import requests, json, os, inquirer, configparser
from datetime import datetime, date
############ VARS ############
configfile = 'config.ini'
name = 'Delta68'
#key = '671c96d4-c517-4dfb-a5ce-edbe0e7c0003'
##############################
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
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
cls()
config = configparser.ConfigParser()
config.read_string(open(configfile,'r').read())
info_options = config.get('options', 'infomation')
key = config.get('API', 'key')
info = []
for i in info_options:
    info.append(i)

questions = [inquirer.Checkbox('Info',message="What Infomation are you interested in?",choices=[('Options', 'O'),('Info', 'I'),('Bedwars', 'B'),],default=info)]
answers = inquirer.prompt(questions)
config['options']['infomation'] = ''
for i in answers['Info']:
    config['options']['infomation'] = config['options']['infomation'] + str(i)
with open(configfile, 'w') as configfilew:    # save
    config.write(configfilew)
    configfilew.close()
if 'O' in answers["Info"]:
    cls()
    questions = [inquirer.Checkbox('Options',message="What Settings do you want to change?",choices=[('API Key'),('Save Loctation')])]
    answers2 = inquirer.prompt(questions)
    if 'API Key' in answers2['Options']:
        print(colored("Current Key is: ",'blue') + colored(str(key),'magenta'))
        input_key = input(colored("Enter New key:  ",'blue')+"\033[32m")
        config['API']['key'] = input_key
        key = input_key
        with open(configfile, 'w') as configfilew:
            config.write(configfilew)
            configfilew.close()
        print(colored('','reset'),end='')
    elif 'Save Loctation' in answers2['Options']:
        pass
    else:
        pass
cls()
print(colored("Getting Player Data...",'green'))
try:
    response = requests.get("https://api.hypixel.net/player?key="+str(key)+"&name=" + str(name.lower()))
except:
    print(colored("Error...",'red'))
    quit()
data = json.loads(response.text)

if data["player"] == None:
    print(colored(name,'magenta') + colored(" Has never Joined Hypixel.",'red'))
    quit()
else:
    print(colored("Sucess!",'green'))


cls()
lastLogin = data["player"]["lastLogin"]
lastLogin = datetime.fromtimestamp(lastLogin/1000)
lastLogout = data["player"]["lastLogout"]
lastLogout = datetime.fromtimestamp(lastLogout/1000)
online = True if lastLogin > lastLogout else False
print(colored("Player: ",'blue')+colored(name,'green' if online else 'red')+"\n")
if "I" in answers["Info"]:
    #INFO
    lastLogin = data["player"]["lastLogin"]
    lastLogin = datetime.fromtimestamp(lastLogin/1000)
    firstLogin = data["player"]["firstLogin"]
    firstLogin = datetime.fromtimestamp(firstLogin/1000)
    lastLogout = data["player"]["lastLogout"]
    lastLogout = datetime.fromtimestamp(lastLogout/1000)
    uuid = data["player"]["uuid"]
    try:
        mostRecentGameType = data["player"]["mostRecentGameType"]
    except:
        mostRecentGameType = "None"
    karma = data["player"]["karma"]
    online = True if lastLogin > lastLogout else False

    print(colored("Info:",'green'))

    try:
        print(colored(" > ",'cyan')+colored("is Online:    ","blue") + colored(str(online),'magenta'))
        print(colored(" > ",'cyan')+colored("UUID:         ","blue") + colored(str(uuid),'magenta'))
        print(colored(" > ",'cyan')+colored("First Login:  ","blue") + colored(str(firstLogin),'magenta'))
        print(colored(" > ",'cyan')+colored("Last Login:   ","blue") + colored(str(lastLogin),'magenta'))
        print(colored(" > ",'cyan')+colored("Last Logout:  ","blue") + colored(str(lastLogout),'magenta'))
        print(colored(" > ",'yellow')+colored("-----------",'yellow'))
        print(colored(" > ",'cyan')+colored("Recent Game:  ","blue") + colored(str(mostRecentGameType),'magenta'))
        print(colored(" > ",'cyan')+colored("Karma:        ","blue") + colored(str(karma),'magenta'))
    except:
        pass
if "B" in answers["Info"]:
    #BEDWARS
    try:
        BedwarsKills =  data["player"]["stats"]["Bedwars"]["kills_bedwars"]
    except KeyError:
        BedwarsKills = 0
    try:
        BedwarsDeaths = data["player"]["stats"]["Bedwars"]["deaths_bedwars"]
    except KeyError:
        BedwarsDeaths = 0
    try:
        BedwarsWins =   data["player"]["stats"]["Bedwars"]["wins_bedwars"]
    except KeyError:
        BedwarsWins = 0
    try:
        BedwarsLosses = data["player"]["stats"]["Bedwars"]["losses_bedwars"]
    except KeyError:
        BedwarsLosses = 0

    print(colored("Bedwars:",'green'))
    try:
        print(colored(" > ",'cyan')+colored("Kills:  ","blue") + colored(str(BedwarsKills),'magenta'))
        print(colored(" > ",'cyan')+colored("Deaths: ","blue") + colored(str(BedwarsDeaths),'magenta'))
        print(colored(" > ",'cyan')+colored("K/D:    ","blue") + colored(str(round(BedwarsKills/BedwarsDeaths,3)),'magenta'))
    except:
        pass
    try:
        print(colored(" > ",'yellow')+colored("-----------",'yellow'))
        print(colored(" > ",'cyan')+colored("Wins:   ","blue") + colored(str(BedwarsWins),'magenta'))
        print(colored(" > ",'cyan')+colored("Losses: ","blue") + colored(str(BedwarsLosses),'magenta'))
        print(colored(" > ",'cyan')+colored("W/L:    ","blue") + colored(str(round(BedwarsWins/BedwarsLosses,3)),'magenta'))
    except:
        pass