#Paleista programa atspausdina visus įrašus esančius lentelėje.
#Tuomet vartotojo paprašome įvesti norima veiksmą: 
#N - Naujas įrašas
#E - Įrašo redagavimas
#D - Įrašo ištrynimas
#Jeigu pasirenkama E arba D raide, tuomet paprašoma įvesti norimo įrašo ID. 
#Jeigu vykdomas redagavimo veiksmas, tuomet paprašoma įvesti stulpelius kuriuos norima redaguoti ir vėliau stulpelių reikšmes.
#Jeigu norima tik ištrinti įrašą, užtenka tik įr1ašo ID.

import mysql.connector

cnx = None

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="kalėdų dovanos")
except :
    # print(e)
    print("Prisijungimo klaida")


# Kursoriaus sukūrimas
cur = cnx.cursor()

cur.execute("SELECT * FROM pirkiniai")
data = cur.fetchall()
print(data)

letter = input("Įveskite raidę N jei norite įvesti naują įraša, E - įrašą redaguoti, D - įrašą ištrinti ")

if letter == 'N':
    vardas = input("Įveskite vadrą: ")
    dovana = input("Įveskite dovaną: ")
    parduotuve = input("Įveskite parduotuvę: ")
    cur.execute(f"INSERT INTO pirkiniai (vardas, dovana, parduotuve) VALUES ('{vardas}', '{dovana}', '{parduotuve}')")
    cnx.commit()

if letter == 'E':
    id = input("Įveskite id kurį norite redaguoti ")
    stulpelis = input("Įveskite stulpelio pavadinimą kurį norite radaguoti ")
    reikšmė = input("Įveskite koreguotiną reikšmę ")
    cur.execute(f"UPDATE pirkiniai SET {stulpelis} = '{reikšmė}' WHERE id = '{id}'")
    cnx.commit()

if letter == 'D':
    #trinti = input("Įveskite id kurį norite ištrinti ")
    #cur.execute(f"DELETE FROM pirkiniai WHERE id = '{trinti}'")
    cur.execute(f"DELETE FROM pirkiniai WHERE parduotuve = 'Reserved'")
    cnx.commit()





