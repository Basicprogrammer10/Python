from datetime import date
import os,glob
folder_path = "C:/Users/turtl/AppData/Roaming/.minecraft/saves/"
output = 'N:/Minecraft/WorldBackups/Minecraft/'
today = str(date.today())
os.system('mkdir "' + output + today + '"')
worlds = open(output + today + "\\Worlds.txt","w+")
worlds.write('Backup Created With Connors Minecraft Backer Upper™' + '\n' + 'Backup Creation today: ' + today + '\n' + '\n')
for filename in glob.glob(os.path.join(folder_path, '**')):
    name = filename.replace("C:/Users/turtl/AppData/Roaming/.minecraft/saves\\", "")
    nname = name.replace(" ", "-")
    os.system('rar a -m5 -r ' + output + today + "\\" + nname + '.rar "' + filename + '"')
    worlds.write(nname + '\n')
worlds.close()
os.system('exit')