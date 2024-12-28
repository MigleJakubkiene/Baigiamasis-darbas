data = open("U2.txt" , "r")

for line in data.readlines()[2:3] :
    l = line.split(" ")

    int_result = int(''.join(map(str,l)))

    print(int_result)



    
    
