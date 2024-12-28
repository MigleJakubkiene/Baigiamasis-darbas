data = open("vardai.txt", "r")

eilutes = data.readlines()

# Suskaičiuokite visų žmonių amžiaus vidurkį
amziaus_suma = 0

for eilute in eilutes[1:] :
    zmogus = eilute.replace("\n", "").split(";")

    amziaus_suma += int(zmogus[2]) if zmogus[2] else 0

print(amziaus_suma / len(eilutes[1:]))

