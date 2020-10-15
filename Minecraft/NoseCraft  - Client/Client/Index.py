import socket, sys
from datetime import datetime
ip = '127.0.0.1'
port = 25565
DEBUG = True
############ VARS ############
initialise = {}
toImport  =  {}
########### SETUP ###########
for i in toImport:
    defult = False if toImport[i] != '' else True
    exec(str('from ' if defult == False else 'import ')+str(i)+str(' import ' + toImport[i] if defult == False else ''))
def colored(text, color):
    ColorCodes = {'black':'30','red':'31','yellow':'33','green':'32','blue':'34','cyan':'36','magenta':'35','white':'37','gray':'90','reset':'0'}
    return '\033[' + ColorCodes[str(color).lower()] + 'm' + str(text) + "\033[0m"
for i in initialise:
    exec(i + '=' + initialise[i])
######### FUNCTIONS #########
def DebugPrint(Catagory,Text,Color):
    if DEBUG == True:
        print(colored('['+datetime.now().strftime("%H:%M:%S")+'] ','yellow')+colored('['+Catagory+'] ','magenta')+colored(Text,Color))
def sendData(data,ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    s.sendto(data, (ip, port))
    DebugPrint('SendData','Client Sent: \033[34m'+str(data), 'green')
    s.close()
def sendReceveData(data,ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    s.sendto(data, (ip, port))
    DebugPrint('SendData','Client Sent: \033[34m'+str(data), 'green')
    rdata, address = s.recvfrom(4096)
    DebugPrint('SendData','Client Received: \033[34m'+str(rdata), 'green')
    s.close()

####### MAIN FUNCTION #######
def main():
    #sendData(bytes.fromhex('01'),ip,port)
    sendData(bytearray([0x01,0x01]),ip,port)
    #sendData(bytes.fromhex('00'),ip,port)
    #sendData(bytes.fromhex('FE'),ip,port)
    
if __name__ == "__main__":
    main()