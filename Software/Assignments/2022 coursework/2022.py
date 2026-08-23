import csv

def readFileIntoRecords():
    sightings = []
    class Sighting:
        def __init__(self, town, mammal, date, age):
            self.town = town
            self.mammal = mammal
            self.date = date
            self.age = int(age)
    with open('Software/Assignments/2022 coursework/mammals (1).txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newSighting = Sighting(row[0], row[1], row[2], row[3])
            sightings.append(newSighting)
    return sightings

def DisplayAgeOfOldestWalker(sightings):
    oldestAge = 0
    for index in range(len(sightings)):
        if sightings[index].age > oldestAge:
            oldestAge = sightings[index].age
    print(oldestAge)

def firstLetterUpperCase(string):
    firstChar = ord(string[0])
    if firstChar >=97  and firstChar <= 122:
        firstChar = firstChar -32
        string = chr(firstChar) + string[1:]
    return string


def displaySightings(sightings):
    town = input("enter town")
    town = firstLetterUpperCase(town)
    mammal = input("enter mammal")
    mammal = firstLetterUpperCase(mammal)
    print("the dates of the sightings were:")
    for index in sightings:
        if index.town == town and index.mammal == mammal:
            print(index.date)


def displayNumberOfSightings(sightings):
    dayToCount = sightings[0].date
    count = 1
    print("number of sightings in rach day were:")
    for index in range(1, len(sightings)):
        if sightings[index].date == dayToCount:
            count = count + 1
        else:
            print(str(dayToCount) +" "+ str(count))
            dayToCount = sightings[index].date
            count = 1





#main
sightings = readFileIntoRecords()

DisplayAgeOfOldestWalker(sightings)

displaySightings(sightings)

displayNumberOfSightings(sightings)

