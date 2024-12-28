
zvakes=int(input("Įveskite žvakių kiekį :"))

if zvakes > 2000:
    print("Įsigytas žvakių skaičius -", (zvakes), "Žvakių kaina -", (zvakes)*0.96,"Eur")
elif zvakes > 1000:
    print("Įsigytas žvakių skaičius -", (zvakes),"Žvakių kaina -", (zvakes)*0.97,"Eur")
else:
    print("Įsigytas žvakių skaičius -", (zvakes),"Žvakių kaina -", (zvakes),"Eur")


   
pirmas=int(input("Įveskite pirmą skaičių :"))
antras=int(input("Įveskite antrą skaičių :"))
trečias=int(input("Įveskite trečią skaičių :"))

suma=0
kiekis=0
print(f"vidurkis yra {int(pirmas + antras + trečias)/3}")

if pirmas>=10 and pirmas<=90:
     suma += pirmas
     kiekis += 1

if antras>=10 and antras<=90:
     suma += antras
     kiekis += 1


if trečias>=10 and trečias<=90:
     suma += trečias
     kiekis += 1

if kiekis > 0 and suma > 0:
    print (f"Skaičių vidurkis atmetus reikšmes kurios yra mažesnės nei 10 ir didesnės nei 90 {suma/kiekis}")
else :
    print ("Netinkamos reikšmės")






