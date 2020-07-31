import os, time
from pynput.mouse import Controller
############ VARS ############
text = 'test'
##############################
mouse = Controller()
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
class nosecription:
    def getSeed(num):
        past = (0, 0)
        seed = []
        seedtime = []
        finalseed = 1
        done = False
        while not done:
            if past != mouse.position:
                seed.append(mouse.position[0]*mouse.position[1])
                seedtime.append(round(time.time(),0))
                past = mouse.position
            else:
                print(colored("\rMove your mouse around More! (",'red')+colored(str(len(seed)+1),'magenta')+colored("/",'red')+colored(str(num),'magenta')+colored(")",'red'),end='')
            if len(seed) == num:
                print(colored("\nDone!",'green'))
                done = True
        for i in range(len(seed)):
            finalseed = round(finalseed + (seed[i] * seedtime[i]/50),0)
        print(finalseed)
    def toBinary(st):
        return ''.join(format(ord(x), 'b') for x in st)
    def BinaryToDecimal(binary):  
        binary1 = binary  
        decimal, i, n = 0, 0, 0
        while(binary != 0):  
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)  
            binary = binary//10
            i += 1
        return (decimal)
    def BinaryToString(bin_data):
        str_data =' '
        for i in range(0, len(bin_data), 7): 
            temp_data = int(bin_data[i:i + 7]) 
            decimal_data = nosecription.BinaryToDecimal(temp_data) 
            str_data = str_data + chr(decimal_data)  
        return str_data
    def mixymixy1(binIn,key):
        done = False
        working = []
        workingdone = ''
        newkey = key
        while len(str(newkey)) < len(str(binIn)):
            newkey = str(newkey) + str(key) 
        newkey = newkey[:len(str(binIn))]
        workingstring = int(binIn) + int(newkey)
        while not done:
            for i in range(len(str(workingstring))):
                if i >= 5:
                    working.append(1)
                else:
                    working.append(0)
            done = True
        for i in working:
            workingdone = str(workingdone) + str(i)
        return workingdone

            

#1110100110010111100111110100

#print(nosecription.toBinary(text))
#print(nosecription.BinaryToString(nosecription.toBinary(text)))

nosecription.getSeed(256)

#print(nosecription.mixymixy1(1110100110010111100111110100,999))