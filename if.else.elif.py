#Pirma užduotis 

amžius=int(input("Įveskite savo amžių: "))

if amžius >= 18:
    print("Jūs galite balsuoti")

#Antra užduotis

pažimys1=int(input("Įveskite pažymį: "))
pažimys2=int(input("Įveskite pažymį: "))
pažimys3=int(input("Įveskite pažymį: "))

if ((pažimys1 + pažimys2 + pažimys3)/3)>=5:
    print ("Vidurkis teigiamas")
else:
    print ("Vidurkis neigiamas")

#Trečia užduotis
import math
skaičius=int(input("Įveskite skaičių "))

if (skaičius % 2) == 0:
    print(skaičius)
    print(skaičius**2)
    print(skaičius/2)


#Ketvirta užduotis
skaičius1=int(input("Įveskite pirmą skaičių: "))
skaičius2=int(input("Įveskite antrą skaičių: "))

if skaičius1 == skaičius2:
    print("skaičiai lygūs")
elif skaičius1 > skaičius2:
    print("pirmas skaičius didesnis už antrą")
else :
    print("antras skaičius didesnis už pirmą")

#Penkta užduotis
skaičius=9

if skaičius >= 10 and skaičius <=20:
   print ((skaičius),"yra tarp 10 ir 20")

#Šešta užduotis
skaičius=100

if (skaičius % 2) == 0:
    print("Skaičius yra lyginis")

#Septinta užduotis

skaičius=int(input("Įveskite skaičių "))

if skaičius % 5 == 0 and skaičius % 3 == 0: 
    print("FizzBuzz")  
elif skaičius % 3 == 0:
    print("Fizz")
elif skaičius % 5 == 0: 
    print("Buzz")  
else :
    print (skaičius)

#Aštunta užduotis

import string
   
tekstas=''

if tekstas == "":
    print("tekstas tuščias")


if tekstas.isalpha():
    print("vien raidės")
elif tekstas.isnumeric():
    print("vien skaičiai")
elif tekstas.isalnum():
    print("Įvestas tekstas")
else:
    print("yra simbolių")


txt='Kj ah'

if txt.isupper():
    print("didžiosios raidės")
elif txt.islower():
    print("mažosios raidės")
else:
    print("didžiosios ir mažosios raidės")


# Devinta užduotis

įveskitastekstas = input("Įveskite tekstą :")
tekslas= "Vilnius yra UNESCO paveldas nuo 1996 metų."
if įveskitastekstas.lower() in tekslas.lower() :
    print("radome")
