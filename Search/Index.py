import requests
from parsel import Selector
links = ['https://en.wikipedia.org/']
titles = {}
a = 0
no = 0
for i in range(10):
    response = requests.get(links[a])
    selector = Selector(response.text)
    href_links = selector.xpath('//a/@href').getall()
    for i in href_links:
        if i[:1] == '/':
            addlink = str(links[a])+str(i)
            links.append(str(links[a])+str(i))
            no = 0
        elif i[:1] == "#":
            no = 1
        else:
            addlink = str(i)
            links.append(i)
            no = 0
        if no == 0:
            response = requests.get(links[len(links)-1])
            selector = Selector(response.text)
            title = selector.xpath('//title').getall()
            title = str(str(title).replace("<title>","")).replace("</title>","")
            titles[title] = addlink
        a = a + 1
file = open("Search.csv",'a',encoding="utf-8")
for i in titles:
    file.write(str(str(i).replace("['","")).replace("']","")+","+titles[i]+"\n")