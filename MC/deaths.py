import json
import os,glob
folder_path = 'N:\Minecraft\SalC1\Other\jsonTEST\\'
#folder_path = 'N:\Minecraft\SalC1\jsonTEST'
total = 0
players = 0
death = [];
bdeath = []
for filename in glob.glob(os.path.join(folder_path, '*.json*')):
    with open(filename, 'r') as data:
        obj = json.loads(data.read())
        try:
            total = total + obj['stat.deaths']
            players = players + 1
            bdeath.append(obj['stat.deaths'])
            death.append(data)
            death.append(obj['stat.deaths'])
        except:
            players = players + 1
            bdeath.append(0)
            death.append(data)
            death.append(0)
file = open('MC\MCdeath.txt', 'w')
file.write(str(death) + "\n")
file.write("---------------\n")
file.write("Total server deaths: " + str(total) + "\n")
file.write("Average: " + str(total/players) + "\n")
file.write("Max: " + str(max(bdeath)) + "\n")
file.write("Min: " + str(min(bdeath)) + "\n")
file.close()
print("Total server deaths: " + str(total))
print("Average: " + str(total/players))
print("Max: " + str(max(bdeath)) + "\n")
print("Min: " + str(min(bdeath)) + "\n")