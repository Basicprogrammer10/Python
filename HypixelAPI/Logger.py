import requests, json, os, time, threading
from datetime import datetime, date
############ VARS ############
port = 8888
folder = 'data'
names = ['Delta68']
key = '671c96d4-c517-4dfb-a5ce-edbe0e7c0003'
t = 5 #Wait Tile
ver = 1.3
##############################
def startserver(port,folder):
    os.system("cd "+folder+" && python3 -m http.server "+str(port))
t1 = threading.Thread(target=startserver, name='t1', args=(port,folder)) 
t1.start() 
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
print(colored("Running Version: ",'blue')+colored(str(ver),'magenta'))
while True:
    for name in names:
        data = ''
        print(colored("Getting Player Data...",'green'))
        try:
            response = requests.get("https://api.hypixel.net/player?key="+str(key)+"&name=" + str(name.lower()))
        except:
            print(colored("Error...",'red'))
            quit()
        data = json.loads(response.text)
        print(colored("Success!!",'green'))
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
        try:
                GamesPlayed = data["player"]["stats"]["Bedwars"]["games_played_bedwars"]
        except KeyError:
                GamesPlayed = 0
        try:
            lastLogin = data["player"]["lastLogin"]
            lastLogin = datetime.fromtimestamp(lastLogin/1000)
            lastLogout = data["player"]["lastLogout"]
            lastLogout = datetime.fromtimestamp(lastLogout/1000)
            online = 1 if lastLogin > lastLogout else 0
        except:
            online = False
        try:
            open('data/'+name.lower()+'.csv','r')
        except:
            open('data/'+name.lower()+'.csv','a').write("Time,Kills,Deaths,Wins,Losses,GamesPlayed,isOnline\n")
        open('data/'+name.lower()+'.csv','a').write(str(datetime.now().strftime('%Y-%m-%d %H:%M'))+","+str(BedwarsKills)+","+str(BedwarsDeaths)+","+str(BedwarsWins)+","+str(BedwarsLosses)+","+str(GamesPlayed)+","+str(online)+"\n")
    time.sleep(t*60)
