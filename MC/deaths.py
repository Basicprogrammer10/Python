import json
import os,glob
folder_path = 'N:\Minecraft\SalC1\world\stats'
total = 0
players = 0
death = [];
for filename in glob.glob(os.path.join(folder_path, '*.json*')):
    with open(filename, 'r') as data:
        obj = json.loads(data.read())
        try:
            total = total + obj['stat.deaths']
            players = players + 1
            death.append(obj['stat.deaths'])
        except:
            players = players + 1
            death.append(0)
file = open('MC\MCdeath.txt', 'w')
file.write(str(death) + "\n")
file.write("---------------\n")
file.write("Total server deaths: " + str(total) + "\n")
file.write("Average: " + str(total/players) + "\n")
file.close()
print(death)
print("Total server deaths: " + str(total))
print("Average: " + str(total/players))