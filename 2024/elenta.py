import requests
from bs4 import BeautifulSoup
from time import sleep
import mysql.connector

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="elenta")
except :
    print("Prisijungimo klaida")

cur = cnx.cursor()

    # Adreso priskyrimas
url = "https://elenta.lt/skelbimai/nt/butai"

    # Pateikiame užklausą
data = requests.get(url)
data = data.text

#print(data)
     
html = BeautifulSoup(data, "html.parser")

for box in html.select(".units-list li") :
    #PhotoId=(box.select_one(".img src").text)
    title=(box.select_one("a.ad-hyperlink").text)
    #price=(box.select_one("span").text)
    address=(box.select_one("span").text)
    #phone=(box.select_one(".uk-button-primary").text)

#print(title)
print(title)
print(address)

   