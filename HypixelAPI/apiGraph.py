import pandas as pd
import numpy as np
import urllib.request
############ VARS ############
url = 'http://mc.connorcode.com:8888/'
names = ['Delta68']
ver = 0.1
##############################
for name in names:
    print(name)
    #page = urllib.request.urlopen(url+name.lower()+'.csv')
    s1 = pd.Series([1.1,1.5,3.4,3.8,5.3,6.1,6.7,8]) 
    s1.plot()
    while True:
        pass