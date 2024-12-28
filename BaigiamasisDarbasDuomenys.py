import requests
from bs4 import BeautifulSoup
import mysql.connector
import csv

#url = "https://www.aruodas.lt/butai/vilniuje/"

#url = "https://www.skelbiu.lt/skelbimai/transportas/kita/"

#print(data.status_code)

# prisijungiant prie Aruodo statuso kodas - 403, galima būtų bandyti dirbti su selenium, tačiau nesirenku šio varianto
# prisijungiant prie Skelbimai.lt statuso kodas - 403, galima būtų bandyti dirbti su selenium, tačiau nesirenku šio varianto

base_url = "https://elenta.lt/"
next_url = "/skelbimai/nt/namai"

def get_data(base, next) :
    response = []

    data = requests.get(base + next)

    html = BeautifulSoup(data.text, "html.parser")

    #response.append(html.select_one('title').text)
    for box in html.select(".summary") :
        Pavadinimas = box.select_one("h3.ad-hyperlink")
        Pavadinimas = Pavadinimas.text if Pavadinimas else ""
        Adresas = box.select_one("span.location-box")
        Adresas = Adresas.text if Adresas else ""
        Kaina = box.select_one("span.price-box")
        Kaina = Kaina.text if Kaina else ""
        
        response.append({
            "Pavadinimas" : Pavadinimas,
            "Adresas" : Adresas,
            "Kaina" : Kaina
        })

    next = html.select_one('[rel="next"]')

    if next :
        next = html.select_one('[rel="next"]').attrs['href']
        response += get_data(base, next)

    return response

f = open("visi_duomenys.csv", "w", encoding="utf8")

data = get_data(base_url, next_url)

for listing in data :
    #print(";".join(listing.values()))
    f.write(";".join(listing.values())+"\n")






