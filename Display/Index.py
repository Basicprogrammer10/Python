############ VARS ############
### SERVER ###
hostName = "localhost"
serverPort = 8080
#### PAGE ####
JsonData = ['{"ID":"TEST-ID","DATA":"NOSE"}','{"ID":"TEST-ID2","DATA":"NOSE2"}','{"ID":"TEST-ID03","DATA":"NOSE03"}','{"ID":"TEST-ID004","DATA":"NOSE004"}']
HTML = 'index.html'
#### CODE ####
initialise = {'data':"''",'getindex':'0'}
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
        global getindex
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == '/':
            data = str(open(HTML,'r',encoding='utf-8').read())
            self.wfile.write(bytes(data, "utf-8"))
        elif "DOMGET" in self.path:
            try:
                self.wfile.write(bytes(JsonData[getindex], 'utf-8'))
                getindex = getindex + 1
            except IndexError:
                getindex = 0
                self.wfile.write(bytes(JsonData[getindex], 'utf-8'))
                getindex = getindex + 1

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