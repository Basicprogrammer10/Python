# For python 3.8
import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import gmtime, strftime, sleep
from tkinter import *
d = False
#min = 5
min = randint(1, 15)
hor = 8
sec = 0
wait = 2
root = Tk()
mainframe = Frame(root)
mainframe.grid(column=1000, row=1000, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
 
best = StringVar()
best.set('start')
x1 = 12
Label(mainframe,textvariable=best,font=("Helvetica",x1)).grid(column=1,row=1)
def login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://students.genesisedu.com/bernardsboe/")
    assert "Students" in driver.title
    username = driver.find_element_by_name('j_username')
    password = driver.find_element_by_name('j_password')
    username.clear()
    password.clear()
    # replace "<Email>" with your email (SamSmith@bernardsboe.com)
    username.send_keys("<Email>")
    password.send_keys("<Password>")  # replace <Password> with password
    password.send_keys(Keys.RETURN)
    button = driver.find_element_by_id('__button1__')
    button.click()
    element = driver.find_element_by_id('attendanceType')
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        if option.get_attribute("value") == "Present":
            option.click()
    save = driver.find_element_by_class_name('saveButton')
    save.click()
    time.sleep(3)
    driver.close()
while True:
    # change - 4 to your timezone (-4 is Eastern Time)
    h = int(strftime("%H", gmtime())) - 4
    m = int(strftime("%M", gmtime()))
    ct = m + (h * 60)
    ft = min + (hor * 60)
    tp = ft - ct
    print(chr(27) + "[2J")
    if tp < 0:
        pt = tp + 24 * 60
        ph = pt / 60
        pm = pt % 60
        j = str(int(ph)) + ":" + str(pm)
    else:
        pt = tp
        ph = pt / 60
        pm = pt % 60
        j = str(int(ph)) + ":" + str(pm)
    time.sleep(wait)
    if j == "0:0":
        best.set("Now!")
    else:
        best.set(str(j))
    mainframe.update()
    if int(h) == hor:
        if int(m) == min:
            if d == False:
                login()
                time.sleep(65)
root.mainloop() 