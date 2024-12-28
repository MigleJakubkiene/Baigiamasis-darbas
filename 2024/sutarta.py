import requests
from bs4 import BeautifulSoup
from time import sleep
import mysql.connector


#base_url = "https://sutarta.lt/"

url = "https://sutarta.lt/skelbimai/garso-vaizdo-foto-technika/vaizdo-video-technika"
data = requests.get(url)

if data.status_code != 200 :
    print("Nepavyko gauti duomenų")
else :
    # Paimame iš atsakymo gautą html kodą
    data = data.text

    # print(data)

    # # Konvertuojame HTML kodą į objektą
    html = BeautifulSoup(data, "html.parser")

    # select_one() metodas suranda vieną patį pirmą elementą pagal css selektorių
    # print(html.select_one(".uk-panel-title a span").text)

    # select() metodas grąžina visus elementus pagal pateiktą selektorių
    # for title in html.select(".uk-panel-title a span") :
    #     print(title.text)

    for box in html.select(".list li") :
        time = box.select_one("div.list-date")
        time = time.text.strip() if time else ""
        print(f"Laikas: {time}")
        photo = box.select_one("img")
        photo = photo.attrs['src'] if photo else ""
        print(f"Nuotrauka: {photo}")
        title = box.select_one("div.desc-title")
        title = title.text if title else ""
        print(f"Pavadinimas: {title}")
        category = box.select_one(".section a")
        category = category.text if category else ""
        print(f"Kategorija: {category}")
        city = box.select_one("div.cat-geo clean-links.section section-category.section")
        city = city.text if city else ""
        print(f"Miestas: {city}")

