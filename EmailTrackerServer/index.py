############ VARS ############
configFile = "data/config/config.confnose"
serverVersion = "0.1"
DEBUG = True
toImport = {"base64": "", "json": "", "urllib.parse": "urlparse", "time": "",
            "http.server": "BaseHTTPRequestHandler, HTTPServer", "datetime": "datetime", "re":""}
########### SETUP ###########
for i in toImport:
    defult = False if toImport[i] != "" else True
    exec(str("from " if defult == False else "import ") + str(i) +
         str(" import " + toImport[i] if defult == False else ""))


def colored(text, color):
    ColorCodes = {"black": "30", "red": "31", "yellow": "33", "green": "32", "blue": "34",
                  "cyan": "36", "magenta": "35", "white": "37", "gray": "90", "reset": "0"}
    return "\033[" + ColorCodes[str(color).lower()] + "m" + str(text) + "\033[0m"
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
            working = i.split('=')
            try:
                working[0] = working[0].replace(' ','')
                working[1] = re.search(r'"([A-Za-z0-9_\./\\-]*)"', working[1]).group().replace('"','')
            except:
                pass
            if len(working[0]) >= 3 and working[0][0] != '#':
                final[working[0]] = working[1]
        DebugPrint('Config','Config File Parsed Successfully', 'green')
        config.configFileData = final
        

    def get(Thing):
        return config.configFileData[Thing]

class MyServer(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
       return

    def responce(self, data, content, code):
        self.send_response(code)
        self.send_header("Content-type", content)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        urlps = urlparse(self.path).path.split("/")
        dateTimeNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if urlps[1] == "image":
            DebugPrint('Request','\033[34m%s \033[34m%s %s' % (self.client_address[0],self.command,self.path),'magenta')
            try:
                try:
                    self.responce(open(config.get('ImgDir')+urlps[2], 'rb').read(), "image/png", 200)
                    databaseWrite(config.get('database'), createJsonResponce([['ip',self.client_address[0]], ['cmd', self.command], ['path',self.path], ['userAgent',str(self.headers).split('\n')[1].split('User-Agent: ')[1]]]))
                except:
                    self.responce(open(config.get('defultImg'), 'rb').read(), "image/png", 200)
                    databaseWrite(config.get('database'), createJsonResponce([['ip',self.client_address[0]], ['cmd', self.command], ['path',self.path], ['userAgent',str(self.headers).split('\n')[1].split('User-Agent: ')[1]]]))
            except:
                self.responce(bytes(createJsonResponce([['serverVersion', serverVersion], ['auth', 'invalidRequest']]), "utf-8"), 400)
                databaseWrite(config.get('database'), createJsonResponce([['ip',None], ['cmd', None], ['path',None]]))


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
    try:
        working = open(config.get('database'), "r").read()
        if working == "":
            open(config.get('database'), "w").write("[]")
    except:
        open(config.get('database'), "x")
        startupChecks()


def startServer(hostName, serverPort):
    webServer = HTTPServer((hostName, serverPort), MyServer)
    try:
        DebugPrint('Server','Server Started at \033[34mhttp://%s:%s' % (hostName, serverPort),'green')
        webServer.serve_forever()
    except:
        pass
    webServer.server_close()
    DebugPrint('Server','Server Closed','red')


####### MAIN FUNCTION #######
def main():
    config.read(configFile)
    startupChecks()
    startServer(config.get('hostName'), int(config.get('serverPort')))


if __name__ == "__main__":
    main()