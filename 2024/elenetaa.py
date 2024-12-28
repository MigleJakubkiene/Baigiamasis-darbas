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

base_url = "https://elenta.lt"

next_url = "https://elenta.lt/skelbimai/nt/butai"

def get_data(base, next) :  
    #response = []

    data = requests.get(base + next)

    html = BeautifulSoup(data.text, "html.parser")

  
    data = html.select('.units-list li')
    
    for listing in data :
        title = listing.select_one('a.ad-hyperlink')
        title = title.text if title else ""

        image = listing.select_one('img')
        image = image.attrs['src'] if image else ""

        price = listing.select_one('.price-box')
                price = price.text if price else "0"

        address = listing.select_one(".location-box")
        address = address.attrs["title"].replace("adresas", "").replace("vieta", "").strip() if address else "Nenurodyta"


        description = listing.select_one("p")
        description = description.text if description else ""