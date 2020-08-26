############ VARS ############
### SERVER ###
version = 'BETA 0.15'
hostName = "localhost"
serverPort = 8080
#### CODE ####
initialise = {'data':"''",'index':'0','cps':'10','running':'False','a':'0','eatclick':'0','skey':'"j"'}
toImport  =  {'http.server':'BaseHTTPRequestHandler, HTTPServer','time':'','os':'','urllib.parse':'urlparse','sys':'','threading':'','keyboard':'','mouse':''}
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
def Clicker():
    global running,a,eatclick
    while thred:
        limit = int(eatclick)
        if running:
            time.sleep(1/int(cps))
            mouse.click('left')
            a = int(a) + 1
            if keyboard.is_pressed('k'):
                running = False
            if a == limit:
                a = 0
                mouse.hold('right')
                time.sleep(5)
                mouse.release('right')
        else:
            if keyboard.is_pressed(skey):
                running = True
        
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global cps, eatclick, mode, running
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        urlp = urlparse(self.path)
        if urlp[2] == '/':
            data = str(open('index.html','r',encoding='utf-8').read())
            self.wfile.write(bytes(data, "utf-8"))
        elif urlp[2] == '/start/':
            running = True
        elif urlp[2] == '/stop/':
            running = False
        elif 'MODE=' in urlp[4]:
            workng = urlp[4].split('MODE=')
            mode = int(workng[1])
        elif '/CPS/' in urlp[2]:
            cps = urlp[2].split('/CPS/')[1]
        elif '/EATCLICK/' in urlp[2]:
            eatclick = urlp[2].split('/EATCLICK/')[1]
####### MAIN FUNCTION #######
def main():
    global thred
    print(colored('Minecraft Autoclicker Server ','blue')+colored(version,'magenta'))
    os.chdir('.')
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(colored("Server started http://%s:%s" % (hostName, serverPort),'green'))
    thred = True
    x = threading.Thread(target=Clicker, args=())
    x.start()
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print(colored("Server stopped.",'red'))
    thred = False

if __name__ == "__main__":
    main()