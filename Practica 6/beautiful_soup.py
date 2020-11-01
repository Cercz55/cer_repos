#Webscrapping para obtener informacion de BeautifulSoup y lo guarda en un archivo

import requests
from bs4 import BeautifulSoup


def req(url):
    a = requests.get(url)
    return BeautifulSoup(a.content, 'html.parser')


ask = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
sopa = req(ask)

content = sopa.find('div', attrs={'class':'section'}).getText()
with open('archivo.txt', 'w') as file:
    file.write(content)
