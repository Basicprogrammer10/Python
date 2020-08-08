import re,sys
functions = {"debug":1,"uout":1,"exit":0,"uin":1,"setvar":2,"nose":0,"add":2,"subtract":2}
program_vars = {}
c = 0
doDebug=True #DEBUG Set to False
exec_to_print = ''
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
    file = sys.argv[1]
except:
    file = None
    #file = '/Users/connorslade/Nextcloud/Programming/Python/NoseScript/helloworld.ns'#DEBUG
#TODO: Add Debug Print
def debug_print(text,color):
    if doDebug:
        print(colored(text,color))
def debug(command):
    global doDebug
    if command == '1':
        doDebug = True
        print(colored("Debug Enabled",'magenta'))
    else:
        exec(command)
def nose():
    global exec_to_print
    exec_to_print = colored("^..^      /\n/_/\_____/\n   /\   /\\\n  /  \ /  \\", 'yellow')
    print(colored("^..^      /\n/_/\_____/\n   /\   /\\\n  /  \ /  \\", 'yellow'))
    debug_print("Nosed You!",'magenta')


def uout(text):
    '''uout;text/command | used to print to termanal'''
    global c
    global exec_to_print
    command = user[0 + c].lower()
    exec_to_print = None
    if text in functions:
        formated_args = ''
        for i in range(functions[command]):
            c = c + 1
            formated_args = formated_args + """user[""" + str(c) +"""],"""
        exec("""exec_to_print=""" + command + """(""" + formated_args + """)""")
        if exec_to_print != None:
            print(exec_to_print)
    elif text in program_vars:
        print(program_vars[text],end=' ')
    else:
        print(text,end=' ')
    debug_print("\nPrinted '" + str(text) + "'",'magenta')

def uin(text):
    global exec_to_print
    nose = input(text)
    try:
        exec_to_print = int(nose)
    except ValueError:
        exec_to_print = nose
    debug_print("Returned '" + str(exec_to_print) + "'", 'magenta')
    return nose

def setvar(varname,value):
    global exec_to_print
    global c
    print("c: " + str(c))#DEBUG
    command = user[0 + c].lower()
    exec_to_print = None
    if value in functions:
        formated_args = ''
        for i in range(functions[command]):
            c = c + 1
            formated_args = formated_args + """user[""" + str(c) +"""],"""
        print("c: " + str(c))#DEBUG
        print("command: " + str(command))#DEBUG
        exec("""exec_to_print=""" + command + """(""" + formated_args + """)""")
        if exec_to_print != None:
            program_vars[varname] = exec_to_print
    else:
        program_vars[varname] = value
        debug_print("Set " + varname + " to " + value,'magenta')


def intager(text):
    return int(text)


def exit():
    debug_print("Exiting...",'magenta')
    quit()


def add(num1,num2):
    global exec_to_print
    global c
    c = c - 1#DEBUG
    print("c: " + str(c))#DEBUG
    command = user[0 + c].lower()
    print("command: " + str(command))#DEBUG
    exec_to_print = None
    if num1 in functions or num2 in functions:
        if num1 in functions:
            formated_args = ''
            for i in range(functions[command]):
                c = c + 1
                formated_args = formated_args + """user[""" + str(c) +"""],"""
            print("c: " + str(c))#DEBUG
            print("command: " + str(command))#DEBUG
            exec("""exec_to_print=""" + command + """(""" + formated_args + """)""")
            if exec_to_print != None:
                num1 = exec_to_print
                print("NUM1: " + str(num1))#DEBUG
        if num2 in functions:
            formated_args = ''
            for i in range(functions[command]):
                c = c + 1
                formated_args = formated_args + """user[""" + str(c) +"""],"""
            print("c: " + str(c))#DEBUG
            print("command: " + str(command))#DEBUG
            exec("""exec_to_print=""" + command + """(""" + formated_args + """)""")
            if exec_to_print != None:
                num2 = exec_to_print
                print("NUM2: " + str(num2))#DEBUG
        try:
            exec_to_print=int(num1)+int(num2)
            debug_print("Added " + str(num1) + " and " + str(num2) + " to get " + str(exec_to_print),'magenta')
            return int(num1) + int(num2)
        except ValueError:
            exec_to_print=num1+num2
            debug_print("Added " + str(num1) + " and " + str(num2) + " to get " + str(exec_to_print),'magenta')
            return num1 + num2
    if num1 not in functions and num2 not in functions:
        if num1 in program_vars:
            num1 = program_vars[num1]
        if num2 in program_vars:
            num2 = program_vars[num2]
        try:
            exec_to_print=int(num1)+int(num2)
            debug_print("Added " + str(num1) + " and " + str(num2) + " to get " + str(exec_to_print),'magenta')
            return int(num1) + int(num2)
        except ValueError:
            exec_to_print=num1+num2
            debug_print("Added " + str(num1) + " and " + str(num2) + " to get " + str(exec_to_print),'magenta')
            return num1 + num2


def subtract(num1,num2):
    global exec_to_print
    if num1 in program_vars:
        num1 = program_vars[num1]
    if num2 in program_vars:
        num2 = program_vars[num2]
    try:
        exec_to_print=int(num1)-int(num2)
        debug_print('Subtracted ' + str(num2) + ' from ' + str(num1) + ' to get ' + str(exec_to_print),'magenta')
        return int(num1) - int(num2)
    except ValueError:
        exec_to_print=num1.replace(num2,'')
        debug_print('Subtracted ' + str(num2) + ' from ' + str(num1) + ' to get ' + str(exec_to_print),'magenta')
        return num1.replace(num2,'')

if file != None:
    try:
        nose_file = open(file,'r')
    except:
        print(colored("File Not Foud: ", 'red') + colored(file,'magenta'))
        exit()
    commands = nose_file.readlines()
    a = 0
    for i in commands:
        c = 0
        userin = str(commands[a]).replace('\n','')
        PATTERN = re.compile(r'''((?:[^;"']|"[^"]*"|'[^']*')+)''')
        user = PATTERN.split(userin)[1::2]
        #print("user: "+str(user))#DEBUG
        #print("program_vars: "+str(program_vars))#DEBUG
        command = user[0].lower()
        formated_args = ''
        try:
            arg1 = user[1]
        except:
            arg1 = None
        if command in functions:
            #try:
                for i in range(functions[command]):
                    c = c + 1
                    formated_args = formated_args + """user[""" + str(c) +"""],"""
                #print(command + """(""" + formated_args + """)""")#DEBUG
                exec(command + """(""" + formated_args + """)""")
            #except NameError:
                #print(colored("Unknown Command", 'red'))
        else:
            print(colored("Unknown Command", 'red'))
        a = a + 1
else:
    while True:
        c = 0
        userin = input(colored("\n>>> ", 'green'))
        PATTERN = re.compile(r'''((?:[^;"']|"[^"]*"|'[^']*')+)''')
        user = PATTERN.split(userin)[1::2]
        command = user[0].lower()
        formated_args = ''
        try:
            arg1 = user[1]
        except:
            arg1 = None
        if command in functions:
            #try:
                for i in range(functions[command]):
                    c = c + 1
                    formated_args = formated_args + """user[""" + str(c) +"""],"""
                #print(command + """(""" + formated_args + """)""")#DEBUG
                exec(command + """(""" + formated_args + """)""")
            #except NameError:
                #print(colored("Unknown Command", 'red'))
        else:
            print(colored("Unknown Command", 'red'))