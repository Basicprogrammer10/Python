from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json, time
############ VARS ############
configFile = 'config/config.confnose'
DEBUG = True

toImport  =  {}
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

class config():
    def read(file):
        DebugPrint('Config','Parseing Config File', 'cyan')
        data = open(file, 'r').read().split('\n')
        final = {}
        for i in data:
            working = i.split('=', 1)
            try:
                if '#' not in working[0] and len(working[0]) > 1:
                    working[0] = working[0].replace(' ','').replace('   ','')
                    working[1] = working[1].split("'")[1]
                #working[1] = re.search(r'"([A-Za-z0-9_\./\\-]*)"', working[1]).group().replace('"','')
            except:
                DebugPrint('Config', 'Error Parsing Config', 'red')
                exit(1)
            if len(working[0]) >= 3 and working[0][0] != '#':
                final[working[0]] = working[1]
        DebugPrint('Config','Config File Parsed Successfully', 'green')
        config.configFileData = final
        
    def get(Thing):
        try:
            return config.configFileData[Thing]
        except KeyError:
            DebugPrint('Config', '\033[34m' + Thing + ' \033[31mwas not Defined...', 'red')
            quit(1)

def getSite():
    DebugPrint('Webdriver', 'Starting Webdriver','cyan')
    try:
        driver = webdriver.Firefox(executable_path=config.get('driverPath'))
        DebugPrint('Webdriver', 'Getting \033[34m' + config.get('website'),'cyan')
        driver.get(config.get('website'))
        DebugPrint('Webdriver', 'Success!', 'GREEN')
    except:
        DebugPrint('Webdriver', 'Error Starting Webdriver', 'RED')
    DebugPrint('Webdriver', 'Logging in', 'cyan')
    try:
        un = driver.find_element_by_id(config.get('username_id'))
        pw = driver.find_element_by_id(config.get('password_id'))
        pw.send_keys(config.get("login"))
        un.send_keys(config.get('username'))
        un.send_keys(Keys.RETURN)
        DebugPrint('Webdriver', 'Success! Logged in as: ' + config.get('username').split('@')[0].lower(),'green')
    except:
        DebugPrint('Webdriver', 'Error Logging In', 'red')
    DebugPrint('Webdriver', 'Waiting for Page Load', 'cyan')
    try:
        for i in range(int(config.get('tryAmmount'))):
            if config.get('tabTitle') in driver.execute_script('return document.title;'):
                DebugPrint('Webdriver', 'Changeing Tab', 'cyan')
                driver.execute_script(config.get('changeTabJS').format(login=config.get('login'),tab3=''))
                driver.execute_script(config.get('changeTabJS').format(login=config.get('login'),tab3=config.get('changeTab')))
                break
            time.sleep(int(config.get('restartTime')))
    except IndexError:
        DebugPrint('Webdriver', 'Error Changing Tab', 'red')
    DebugPrint('Webdriver', 'Getting Class Codes', 'cyan')
    try:
        for i in range(int(config.get('tryAmmount'))):
            try:
                working = []
                classCodes = driver.execute_script(config.get('getClassCode'))
                for i in classCodes:
                    if i != None:
                        working.append(i)
                break
            except:
                pass
            time.sleep(int(config.get('restartTime')))
        finalData = {}
        for i in working:
            try:
                driver.execute_script(config.get('displayMP'))
                select = Select(driver.find_element_by_id(config.get('MPselectID')))
                select.select_by_value(config.get('markingPeroid'))
                driver.find_elements_by_xpath(config.get('MPsubmit'))[0].click()
                time.sleep(int(config.get('shortRestart')))
            except: pass
            driver.execute_script(config.get('changeClass').format(code=i))
            gradeData = driver.execute_script('return ' + config.get('getElements').format(tag=config.get('gradeTag'),index=config.get('gradeIndex'))).replace(' ','').replace('\n','')
            gradeSplits = dict(subString.split("=") for subString in config.get('gradeSplits').split(";"))
            #### print('OG: '+gradeData)
            for i in gradeSplits:
                gradeData = gradeData.split(i)[int(gradeSplits[i])]
            className = driver.execute_script(config.get('getSelectedN'))
            DebugPrint('Webdriver', 'Getting data for \033[34m' + className,'magenta')
            try:
                finalData[className] = int(gradeData)
            except: pass
            #### print(className + ': ' + gradeData)
            time.sleep(int(config.get('restartTime')))
    except:
        DebugPrint('Webdriver', 'Error getting Class Codes', 'red')
    driver.quit()
    return finalData

def createJsonResponce(jsonData):
    data = {}
    for i in jsonData:
        data[i[0]] = i[1]
    return json.dumps(data)


def databaseWrite(file, data):
    working = open(file, "r+", encoding="utf-8").read()
    comma = "," if working != "[]" else ""
    open(file, "w", encoding="utf-8").write(working[:-1] + comma + "\n" + data + "]")


def startupChecks():
    global startTime
    startTime = int(round(time.time() * 1000))
    try:
        working = open(config.get('database'), "r").read()
        if working == "":
            open(config.get('database'), "w").write("[]")
    except:
        open(config.get('database'), "x")
        startupChecks()
####### MAIN FUNCTION #######
def main():
    config.read(configFile)
    startupChecks()
    print(getSite())
    DebugPrint('Process', 'Compleated in \033[34m' + str(int(round(time.time() * 1000)) - startTime) + ' ms', 'green')

if __name__ == "__main__":
    main()
