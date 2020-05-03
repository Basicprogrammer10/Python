from datetime import date
from configparser import ConfigParser
import os,glob,easygui

def setupfile():
    config_object = ConfigParser()

    file = open("backupconfig.ini","w+")
    file.close()

    config_object["Setup"] = {
        "admin": "Chankey Pathak",
        "loginid": "chankeypathak",
        "password": "tutswiki"
    }

    with open('backupconfig.ini', 'w') as conf:
        config_object.write(conf)
        conf.close()
    pass

try:
    config_object = ConfigParser()

    config_object.read("backupconfig.ini")
    config_object["Setup"]
except:
    choices = ["Yes", "No"]
    setup = easygui.buttonbox("Config file not found.\nWould you like to Create One?", choices=choices)
    if setup == "Yes":
        setupfile()
        pass
    elif setup == "No":
        easygui.msgbox("This program can not work without the config file.")
        quit()
    else:
        quit()
    
compressondirectoryin = "C:"
compressondirectoryout= "C:"

def compress():
    '''Does The Compression'''
    folder_path = "C:/Users/turtl/AppData/Roaming/.minecraft/saves/"
    output = 'N:/Minecraft/WorldBackups/Minecraft/'
    today = str(date.today())
    os.system('mkdir "' + output + today + '"')
    worlds = open(output + today + "\\Backup.txt","w+")
    worlds.write('Backup Created With Connors Minecraft Backer Upper™' + '\n' + 'Backup Creation today: ' + today + '\n' + '\n')
    for filename in glob.glob(os.path.join(folder_path, '**')):
        name = filename.replace("C:/Users/turtl/AppData/Roaming/.minecraft/saves\\", "")
        nname = name.replace(" ", "-")
        os.system('rar a -m5 -r ' + output + today + "\\" + nname + '.rar "' + filename + '"')
        worlds.write(nname + '\n')
    worlds.close()

def about():
    '''Info About Me!'''
    easygui.msgbox("This Backup Utility was made by Connor Slade!\nEmail: connor@connorcode.com\nSorry for the Win95 UI", "About")

def error(message):
    '''Error Message lol'''
    easygui.msgbox(message, "Error")

while True:
    choices = ["Backup", "Setup", "About", "Quit"]
    opt = easygui.buttonbox("Chose an option", choices=choices)
    if opt == "Quit":
        quit()
    elif opt == "Backup":
        pass
    elif opt == "Setup":
        choices = ["In and Out", "Compression Format", "Compression Level", "Done"]
        setup = easygui.buttonbox("Chose an option", choices=choices)
        if setup == "Done":
            pass
        elif setup == "In and Out":
            choices = ["Input Directory", "Output Directory", "Done"]
            setup = easygui.buttonbox("Chose an option", choices=choices)
            if setup == "Done":
                pass
            elif setup == "Input Directory":
                compressondirectoryin = easygui.diropenbox("Choose Input Directory", "Input Directory", compressondirectoryin) + "\\"
                easygui.msgbox("Input Directory has been set to " + compressondirectoryin)
                pass
            elif setup == "Output Directory":
                compressondirectoryout = easygui.diropenbox("Choose Output Directory", "Output Directory", compressondirectoryout) + "\\"
                easygui.msgbox("Output Directory has been set to " + compressondirectoryout)
                pass
            else:
                pass
            pass
        elif setup == "Compression Format":
            choices = ["Rar", "Zip", "Done"]
            setup = easygui.buttonbox("Chose an option", choices=choices)
            if setup == "Rar":
                easygui.msgbox("Compression Format has been set to .Rar")
                compressonformat = ".rar"
                pass
            elif setup == "Zip":
                easygui.msgbox("Compression Format has been set to .Zip")
                compressonformat = ".zip"
                pass
            else:
                pass
        elif setup == "Compression Level":
            choices = ["Store", "Fastest", "Fast", "Normal", "Good", "Best", "Done"]
            setup = easygui.buttonbox("Chose an option", choices=choices)
            if setup == "Done":
                pass
            elif setup == "Store":
                easygui.msgbox("Compression Level has been set to Store")
                compressonlevel = 0
                pass
            elif setup == "Fastest":
                easygui.msgbox("Compression Level has been set to Fastest")
                compressonlevel = 1
                pass
            elif setup == "Fast":
                easygui.msgbox("Compression Level has been set to Fast")
                compressonlevel = 2
                pass
            elif setup == "Normal":
                easygui.msgbox("Compression Level has been set to Normal")
                compressonlevel = 3
                pass
            elif setup == "Good":
                easygui.msgbox("Compression Level has been set to Good")
                compressonlevel = 4
                pass
            elif setup == "Best":
                easygui.msgbox("Compression Level has been set to Best")
                compressonlevel = 5
                pass
            else:
                pass
            pass
        else:
            pass
    elif opt == "About":
        about()
    else:
        quit()