############ VARS ############
##############################
try:
    for i in toImport:
        if toImport[i] == '':
            exec('import '+i)
        else:
            exec('from '+i+' import '+toImport[i])
    for i in initialise:
        if initialise[i] == 's':
            exec(str(i)+'=""')
        elif initialise[i] == 'i':
            exec(str(i)+'=0')
        elif initialise[i] == 'b':
            exec(str(i)+'=None')
        else:
            pass
except:
    pass