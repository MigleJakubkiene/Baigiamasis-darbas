import requests
from bs4 import BeautifulSoup

# Adreso priskyrimas
url = "https://www.1551.lt/automobiliu-atsargines-dalys-reikmenys/"

# Pateikiame užklausą
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

    for box in html.select("ad-list-area") :
        title=(box.select_one(".uk-panel-title").text)
        description=(box.select_one(".uk-margin").text)
        address=(box.select_one(".uk-margin-right").text)
        phone=(box.select_one(".uk-button-primary").text)

   
    import mysql.connector

cnx = None

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="1551")
except :
    print("Prisijungimo klaida")

cur = cnx.cursor()

#title = (box.select_one(".uk-panel-title").text)
#address = (box.select_one(".uk-margin-right").text)
#phone = (box.select_one(".uk-button-primary").text)

cur.execute(f"INSERT INTO `1551` (title, description, address, phone) VALUES ('{title}', '{description}', '{address}', '{phone}')")
cnx.commit()