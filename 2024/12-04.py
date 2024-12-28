#Pasirinktoje duomenų bazėje sukurkite lentelę dainos, kuri turi šiuos stulpelius:
#id (INT)
#pavadinimas (VARCHAR 255)
#atlikejas (VARCHAR 255)
#zanras (VARCHAR 255)

#Parašykite programą kuri:
#Lieptų vartotojui pasirinkti programos rėžimą. Įvesta raidė "p" reiškia naujos dainos pridėjimą. Visais kitais įvestais atvejais grąžinamas visų dainų sąrašas.
#Jeigu pasirinktas dainos pridėjimas, leiskite vartotojui įvesti duomenis: pavadinima, atlikeją ir žanrą kuriuos išsaugokite duomenų bazėje.

import mysql.connector

cnx = None

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="dainos")
except :
    # print(e)
    print("Prisijungimo klaida")


# Kursoriaus sukūrimas
cur = cnx.cursor()

letter = input("Įveskite raidę p jei norite pridėti naują dainą ")

raide = 'p'


if letter == raide :
    pavadinimas = input("Įveskite pavadinimą: ")
    atlikejas = input("Įveskite atlikėją: ")
    zanras = input("Įveskite žanrą: ")

    cur.execute(f"INSERT INTO dainos (pavadinimas, atlikejas, zanras) VALUES ('{pavadinimas}', '{atlikejas}', '{zanras}')")
    cnx.commit()
else :
    cur.execute("SELECT pavadinimas, atlikejas, zanras FROM dainos")

data = cur.fetchall()

for filmas in data:
    print(filmas)



