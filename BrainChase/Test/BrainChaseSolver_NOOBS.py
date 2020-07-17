import argparse
import sys
import re
import math
import configparser
import os
import urllib.request
from pathlib import Path
from random import randint, shuffle
config = configparser.ConfigParser()
ap = argparse.ArgumentParser()
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

try:
    print(colored("Checking For Updates", 'yellow'))
    update_data = urllib.request.urlopen("https://raw.githubusercontent.com/Basicprogrammer10/Python/master/BrainChase/BrainChase.version")
    config.read_string(update_data.read().decode())
    new_version = config.get('version_info', 'new_version')
    new_version_date = config.get('version_info', 'update_date')
    if float(ver) == float(new_version):
        print(colored("BrainChaseSolver™ ", "blue") + colored("is up to date!", 'green'))
        print(colored("===================================", 'magenta'))
        print(colored("Current Version: ", 'blue') + colored(ver,'cyan') + colored("  (" + ver_date[0:2] + '/' + ver_date[2:4] + '/' + ver_date[4:8] + ")",'magenta'))
        print(colored("Newest Version:  ", 'blue') + colored(new_version,'cyan') + colored("  (" + new_version_date[0:2] + '/' + new_version_date[2:4] + '/' + new_version_date[4:8] + ")",'magenta'))
    elif float(ver) > float(new_version):
        print(colored("You are on a Beta Release of ", 'green') + colored("BrainChaseSolver™ ", "blue"))
        print(colored("===================================", 'magenta'))
        print(colored("Current Version: ", 'blue') + colored(ver,'cyan') + colored("  (" + ver_date[0:2] + '/' + ver_date[2:4] + '/' + ver_date[4:8] + ")",'magenta'))
        print(colored("Newest Version:  ", 'blue') + colored(new_version,'cyan') + colored("  (" + new_version_date[0:2] + '/' + new_version_date[2:4] + '/' + new_version_date[4:8] + ")",'magenta'))
    elif float(ver) < float(new_version):
        print(colored("BrainChaseSolver™ ", "blue") + colored("is out of date...", 'red'))
        print(colored("===================================", 'magenta'))
        print(colored("Current Version: ", 'blue') + colored(ver,'cyan') + colored("  (" + ver_date[0:2] + '/' + ver_date[2:4] + '/' + ver_date[4:8] + ")",'magenta'))
        print(colored("Newest Version:  ", 'blue') + colored(new_version,'cyan') + colored("  (" + new_version_date[0:2] + '/' + new_version_date[2:4] + '/' + new_version_date[4:8] + ")",'magenta'))
        update_input = input(colored("Would You Like To Update? (Y/N) ", 'magenta'))
        if update_input.lower() == 'y':
            print(colored("BrainChaseSolver™ in Updating... ", "yellow"))
            update_code = urllib.request.urlopen("https://raw.githubusercontent.com/Basicprogrammer10/Python/master/BrainChase/Index.py")
            update_code_string = update_code.read().decode()
            update_output = open('BrainChaseSolver_V' + new_version.replace('.','-') + '.py','w', encoding="utf-8")
            update_output.write("filepath = '" + str(Path(__file__).absolute()) + "'\n" + update_code_string)
            print(colored("Done!", "green"))
            print(colored('Run ', 'blue')+ colored('"BrainChaseSolver_V' + new_version.replace('.','-') + '.py"','cyan') + colored('to use V' + new_version, 'blue'))
            quit()
except urllib.error.URLError:
    print(colored("Can't connect to ConnorCode Servers...", 'red'))