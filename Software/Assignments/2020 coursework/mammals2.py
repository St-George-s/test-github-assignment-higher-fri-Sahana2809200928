import csv

class sightings():
    def __init__(self, town,mammal,date,age):
        self.town = town
        self.mammal = mammal
        self.date= date
        self.age = age

#PART 1
def readFile():
    Sightings = []
    with open('Software/Assignments/2020 coursework/mammals (1).txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newSighting = sightings(row[0], row[1], row[2], row[3])
            Sightings.append(newSighting)
        return Sightings

#PART 2
def oldestWalker():
    oldestWalker = 0
    for index in range(len(Sightings)):
        if (int(Sightings[index].age)> oldestWalker):
            oldestWalker =int(Sightings[index].age)
    print(oldestWalker)

def firstLetter_upperCase(word):
    firstChar = ord(word[0])
    if firstChar >97 and firstChar < 122:
        firstChar = ord(int(firstChar-32))

    newWord =  firstChar + word[1:]
    return newWord




# #PART 3
# def mammalSightingsNearTown():
#     Town = input("enter name of town")
#     Town_Capitalized = firstLetter_upperCase(Town)

#     mammal = input("enter the mammal name")
#     mammal_Capitalized = firstLetter_upperCase(mammal)
    
#     print("The dates of sightings were:")
#     for index in range(len(Sightings)):
#         if Sightings[index].mammal ==  mammal_Capitalized and Sightings[index].town== Town_Capitalized:
#             print(Sightings[index].date)


def count_sightings_forEveryDate():
    dayToCount = Sightings[0].date
    count = 1
    for index in range(1, len(Sightings)):
        if Sightings[index].date == dayToCount:
            count += 1
        else:
            print(dayToCount, count)
            dayToCount = Sightings[index].date
            count = 1


        

    


#main
Sightings = readFile()
oldestWalker()
# mammalSightingsNearTown()
#Culross,Squirrel
count_sightings_forEveryDate()