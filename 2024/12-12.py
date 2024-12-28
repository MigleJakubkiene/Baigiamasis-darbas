import requests

kokteilis = input("Įveskite kokteilio pavadinimą ")

url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={kokteilis}"

response = requests.get(url)

data=response.json()

for drink in data["drinks"]:
    print(f"Pavadinimas: {drink["strDrink"]}, Tipas: {drink["strAlcoholic"]}")

