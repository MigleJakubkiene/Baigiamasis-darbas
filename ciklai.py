miestai = ['Vilnius', 'Kaunas', 'Alytus', 'Rokiškis', 'Ūla', 'Mažeikiai', 'Akmena']
              
for miestas in miestai:
      if len(miestas) > 6:
            print (miestas)


simbolis= input("Įveskite simbolį ")
skaičius= int(input("Įveskite skaičių "))

eilute=simbolis * skaičius

for eilute in range(skaičius):
    print (simbolis*skaičius)


simbolis= input("Įveskite simbolį ")
skaičius= int(input("Įveskite skaičių "))



for indeksas in range(skaičius):
        print (simbolis*(indeksas +1))






