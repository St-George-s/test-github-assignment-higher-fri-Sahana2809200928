import csv

def read_file():
    names = []
    hobbies = []
    pokemon= []
    fallout_favourite=[]
    age=[]
    occupation=[]
    with open('data flow/Fun_Users.csv', 'r') as file: 
        reader = csv.reader(file)
        next(reader) 
        for row in reader: 
            print(row) 
            names.append(row[0])
            hobbies.append(row[1])
            pokemon.append(row[2])
            fallout_favourite.append(row[3])
            age.append(row[4])
            occupation.append(row[5])
    return names, hobbies, pokemon, fallout_favourite, age, occupation

def CountPokemon(pokemon):
    pokemon_counter= 0
    choice= input("enter pokemon")
    for x in range(len(pokemon)):
        if pokemon[x] == choice:
            pokemon_counter = pokemon_counter + 1
    return pokemon_counter

def findOld(age):
    highest = age[0]
    for x in range(1, len(age)):
        if age[x] > highest: 
            highest = age[x]
    return highest

def findYoung(age):
    lowest = age[0]
    for x in range(1, len(age)):
        if age[x] < lowest: 
            lowest = age[x]
    return lowest


  
names, hobbies, pokemon, fallout_favourite, age, occupation = read_file()
# globalCounter=CountPokemon(pokemon)
# print(globalCounter)

# oldest = findOld(age)
# print(oldest)

youngest= findYoung(age)
print(youngest)