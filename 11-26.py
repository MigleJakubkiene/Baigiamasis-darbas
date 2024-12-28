data = open("duomenys.txt" , "r")

#Antra sąlyga:
#Išfiltruokite vartotojus kurie neturi gimimo metų.

#for line in data.readlines()[1:] :
    #l = line.split(";")

    #if l[3] :
        #print(line, end = "")

#Šešta sąlyga:
#Išfiltruokite vartotojus kurie nėra įvedę pavardės.

#for line in data.readlines()[1:] :
    #l = line.split(";")

    #if l[1] :
        #print(line, end = "")

#Penkta sąlyga:
#Išfiltruokite vartotojus kurių slaptažodžiai yra trumpesni nei 5 simboliai.

#for line in data.readlines()[1:] :
    #l = line.split(";")

    #if len(l[4]) >= 5 :
        #print(line, end = "")

#Pirma sąlyga: 
#Išfiltruokite ir grąžinkite vartotojus kurių slaptažodžiuose nėra skaičių.

#for line in data.readlines()[1:] :
    #l = line.split(";")
    
    #if l[4].replace("\n", "").isalpha():
        #print(line, end = "")

#Trečia sąlyga: 
#Išveskite visų vartotojų amžiaus vidurkį.

#amziaus_suma = 0
#asmenys = 0
#for line in data.readlines()[1:]:
    #l = line.split(";")
    
    #if l[3] :
        #amziaus_suma += 2024 - int(l[3])
        #asmenys += 1
              
#print(amziaus_suma/asmenys)

#Ketvirta sąlyga:
#Išfiltruokite vartotojus su neteisingais el. pašto adresais.

#for line in data.readlines()[1:] :
    #l = line.split(";")

   #if "@" in l[2].replace("\n", ""):
        #print(line, end = "")
  