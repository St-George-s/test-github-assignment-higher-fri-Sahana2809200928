import csv

class Sighting():
    def __init__(self, town, mammal, date, age):
        self.town = town
        self.mammal = mammal
        self.date = date
        self.age = age

def readFile():
    Sightings = []
    with open ('Software/Assignments/2020 coursework/mammals (1).txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newSighting = Sighting(row[0], row[1], row[2], int(row[3]))
            Sightings.append(newSighting)
    return Sightings

def OldestWalker(Sightings):
    oldestWalker = 0
    for index in range(len(Sightings)):
        if Sightings[index].age > oldestWalker:
            oldestWalker = Sightings[index].age
    print(oldestWalker)

def firstLetter_uppercase(word):
    firstchar = ord(word[0])
    if firstchar <= 122 and firstchar >=97:
        firstchar = firstchar - 32
        word= chr(firstchar) + word[1:]
    return word


def mammalSightings(Sightings):
    Town =input("enter Town")
    Town = firstLetter_uppercase(Town) 

    Mammal = input("enter mammal")
    Mammal = firstLetter_uppercase(Mammal)

    print("the date(s) of the sightings were:")

    for index in range(len(Sightings)):
        if Sightings[index].mammal == Mammal and Sightings[index].town == Town:
            print(Sightings[index].date)

    
def number_sightings(Sightings):
    dayToCount = Sightings[0].date
    count = 1
    for index in range(1, len(Sightings)):
        if Sightings[index].date == dayToCount:
            count = count + 1
        else:
            print(dayToCount, count)
            dayToCount = Sightings[index].date
            count = 1
    print(dayToCount, count)

           
        
#main

Sightings = readFile()

OldestWalker(Sightings)

mammalSightings(Sightings)

number_sightings(Sightings)