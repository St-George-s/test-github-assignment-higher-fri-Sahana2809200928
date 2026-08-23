import csv
import math

class Member:
    def __init__(self, forename, surname, distance):
            self. forename= forename
            self.surname = surname
            self.distance = distance
def readMemberData():
    members = []
    with open("Software/Assignments/2019/members.txt", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newMember = Member(row[0], row[1], float(row[2]))
            members.append(newMember)
    return members

    
def findFurthestDistance(members):
    furthest = members[0].distance
    for x in range(len(members)):
        if members[x].distance > furthest:
            furthest = members[x].distance
    return furthest

def displayFurthestDistance(furthest):
    print(furthest)

def writeWinnerToFile(members, furthest):
    with open('results.txt', 'w') as file:
        file.write("The prize winning members are: " + "\n")
        for x in range(len(members)):
            if members[x].distance >= furthest*0.7:
                file.write(members[x].forename + " " + members[x].surname + "\n")
        file.write("ht enubmer of whoel mathtaosn walked by each emmebr is:" + "\n")
        for x in range(len(members)):
            numberMarathons = members[x]. distance//26.22
            file.write(members[x].forename +"," + members[x].surname + "," + str(math.trunc(numberMarathons)) + '\n')



#main
members = readMemberData()
furthest = findFurthestDistance(members)
displayFurthestDistance(furthest)
writeWinnerToFile(members, furthest)


