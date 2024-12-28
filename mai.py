import mysql.connector

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="naujas")

cur = cnx.cursor()

#cur.execute("SELECT * FROM country_data")

#data = cur.fetchall()
#cur.fetchone()
#print(data)
letter = input("Įveskite sraidę l ")
cur.execute(f"SELECT country_name FROM country_data WHERE country_name LIKE '%{letter}%'")
data = cur.fetchall()

print(data)


