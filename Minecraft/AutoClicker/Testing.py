############ VARS ############
### SERVER ###
hostName = "localhost"
serverPort = 8080
#### PAGE ####
HTML = 'index.html'
PageFormat = {'title':'NOSE'}
#### CODE ####
initialise = {'data':"''",'index':'0'}
toImport  =  {'http.server':'BaseHTTPRequestHandler, HTTPServer','time':'','os':''}
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
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global cps, eatclick
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == '/':
            data = str(open(HTML,'r',encoding='utf-8').read())
            self.wfile.write(bytes(data, "utf-8"))
        elif "CPS" in self.path:
            cps = str(self.path).replace('/CPS/','')
            print("CPS: " + cps)#FIXME:
        elif "EATCLICK" in self.path:
            eatclick = str(self.path).replace('/EATCLICK/','')
            if int(eatclick) == 0:
                eatclick = False
            print("EATCLICK: " + str(eatclick))#FIXME:

####### MAIN FUNCTION #######
def main():
    os.chdir('.')
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(colored("Server started http://%s:%s" % (hostName, serverPort),'green'))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print(colored("Server stopped.",'red'))

if __name__ == "__main__":
    main()