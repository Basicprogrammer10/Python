from datetime import date
from configparser import ConfigParser
from threading import Thread
import os,glob,easygui

def setupfile():
    config_object = ConfigParser()

    file = open("backupconfig.ini","w+")
    file.close()

    config_object["Setup"] = {
        "compressondirectoryin": "C:\\",
        "compressondirectoryout": "C:\\",
        "compressonlevel": "5",
        "compressonformat": ".rar"
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

def configsave():
    with open('backupconfig.ini', 'w') as conf:
            config_object.write(conf)
            conf.close()

config_object = ConfigParser()
config_object.read("backupconfig.ini")

compressondirectoryin = config_object["Setup"]["compressondirectoryin"]
compressondirectoryout = config_object["Setup"]["compressondirectoryout"]
compressonlevel = config_object["Setup"]["compressonlevel"]
compressonformat = config_object["Setup"]["compressonformat"]

def compress(output,folder_path,format,level):
    '''Does The Compression'''
    today = str(date.today())
    os.system('mkdir "' + output + today + '"')
    worlds = open(output + today + "\\Backup.txt","w+")
    worlds.write('Backup Created With Connors Backer Upper™' + '\n' + 'Backup Creation Date: ' + today + '\n' + '\n')
    for filename in glob.glob(os.path.join(folder_path, '**')):
        name = filename.replace(folder_path, "")
        nname = name.replace(" ", "-")
        os.system('rar a -m' + str(level) + ' -r ' + output + str(date.today()) + "\\" + nname + format + ' "' + filename + '"')
        worlds.write(nname + '\n')
    worlds.close()

def about():
    '''Info About Me!'''
    easygui.msgbox("This Backup Utility was made by Connor Slade!\nEmail: connor@connorcode.com\nSorry for the Win95 UI", "About")

def error(message):
    '''Error Message lol'''
    easygui.msgbox(message, "Error")

def compress1():
    easygui.msgbox("Backup Started\nThis may take some time!\n\nWhen process finishes you will be alerted.")
    pass

def compress2():
    compress(compressondirectoryout,compressondirectoryin, compressonformat, compressonlevel)
    easygui.msgbox("Process Completed!")
    pass

while True:
    choices = ["Backup", "Setup", "About", "Quit"]
    opt = easygui.buttonbox("Chose an option", choices=choices)
    if opt == "Quit":
        quit()
    elif opt == "Backup":
        choices = ["Yes", "No"]
        title = "Is this correct?\n\n"+"In Directory: "+compressondirectoryin+"\nOut Directory: "+compressondirectoryout+"\nCompression Level: "+str(compressonlevel)+"\nCompression Format: "+compressonformat
        setup = easygui.buttonbox(title, choices=choices)
        if setup == "No":
            pass
        elif setup == "Yes":
            try:
                #print('rar a -m' + str(compressonlevel) + ' -r ' + compressondirectoryout + str(date.today()) + "\\ " + compressondirectoryin + compressonformat + ' "' + 'FileName' + '"')
                Thread(target=compress1).start()
                Thread(target=compress2).start()
            except:
                easygui.msgbox("An Error Occurred")
            pass
        else:
            quit()
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
                config_object["Setup"]["compressondirectoryin"] = compressondirectoryin
                configsave()
                easygui.msgbox("Input Directory has been set to " + compressondirectoryin)
                pass
            elif setup == "Output Directory":
                compressondirectoryout = easygui.diropenbox("Choose Output Directory", "Output Directory", compressondirectoryout) + "\\"
                config_object["Setup"]["compressondirectoryout"] = compressondirectoryout
                configsave()
                easygui.msgbox("Output Directory has been set to " + compressondirectoryout)
                pass
            else:
                quit()
            pass
        elif setup == "Compression Format":
            choices = ["Rar", "Zip", "Done"]
            setup = easygui.buttonbox("Chose an option", choices=choices)
            if setup == "Rar":
                easygui.msgbox("Compression Format has been set to .Rar")
                compressonformat = ".rar"
                config_object["Setup"]["compressonformat"] = compressonformat
                configsave()
                pass
            elif setup == "Zip":
                easygui.msgbox("Compression Format has been set to .Zip")
                compressonformat = ".zip"
                config_object["Setup"]["compressonformat"] = compressonformat
                configsave()
                pass
            else:
                quit()
        elif setup == "Compression Level":
            choices = ["Store", "Fastest", "Fast", "Normal", "Good", "Best", "Done"]
            setup = easygui.buttonbox("Chose an option", choices=choices)
            if setup == "Done":
                pass
            elif setup == "Store":
                easygui.msgbox("Compression Level has been set to Store")
                compressonlevel = 0
                config_object["Setup"]["compressonlevel"] = str(compressonlevel)
                configsave()
                pass
            elif setup == "Fastest":
                easygui.msgbox("Compression Level has been set to Fastest")
                compressonlevel = 1
                config_object["Setup"]["compressonlevel"] = str(compressonlevel)
                configsave()
                pass
            elif setup == "Fast":
                easygui.msgbox("Compression Level has been set to Fast")
                compressonlevel = 2
                config_object["Setup"]["compressonlevel"] = str(compressonlevel)
                configsave()
                pass
            elif setup == "Normal":
                easygui.msgbox("Compression Level has been set to Normal")
                compressonlevel = 3
                config_object["Setup"]["compressonlevel"] = str(compressonlevel)
                configsave()
                pass
            elif setup == "Good":
                easygui.msgbox("Compression Level has been set to Good")
                compressonlevel = 4
                config_object["Setup"]["compressonlevel"] = str(compressonlevel)
                configsave()
                pass
            elif setup == "Best":
                easygui.msgbox("Compression Level has been set to Best")
                compressonlevel = 5
                config_object["Setup"]["compressonlevel"] = str(compressonlevel)
                configsave()
                pass
            else:
                quit()
            pass
        else:
            quit()
    elif opt == "About":
        about()
    else:
        quit()