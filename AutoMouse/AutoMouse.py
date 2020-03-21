import pyautogui
import os, sys, time
from configparser import *
configParser = ConfigParser()   
configParser.read_file(open(os.path.join(sys.path[0], "config.ini"), "r"))
pyautogui.alert('To stop program move mouse curser to the top left of the screen.')
time.sleep(0.25)
pyautogui.moveTo(int(configParser.get('SETUP', 'start-x')), int(configParser.get('SETUP', 'start-y')))
if int(configParser.get('SETUP', 'drag')) == 0:
    while True:
        pyautogui.moveRel(int(configParser.get('SETUP', 'move-x')), int(configParser.get('SETUP', 'move-y')))
        time.sleep(int(configParser.get('SETUP', 'delay'))/1000)
        pyautogui.moveRel(int(configParser.get('SETUP', 'moveback-x')), int(configParser.get('SETUP', 'moveback-y')))
        time.sleep(int(configParser.get('SETUP', 'delay'))/1000)
else:
    while True:
        pyautogui.moveRel(int(configParser.get('SETUP', 'move-x')), int(configParser.get('SETUP', 'move-y')), int(configParser.get('SETUP', 'drag-duration'))/1000)
        time.sleep(int(configParser.get('SETUP', 'delay'))/1000)
        pyautogui.moveRel(int(configParser.get('SETUP', 'moveback-x')), int(configParser.get('SETUP', 'moveback-y')), int(configParser.get('SETUP', 'drag-duration'))/1000)
        time.sleep(int(configParser.get('SETUP', 'delay'))/1000)


