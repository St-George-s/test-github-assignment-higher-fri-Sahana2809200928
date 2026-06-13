import csv
import math 

def readFromfileIntoRecords():
    members = []
    class Member:
        def __init__(self, forename, surname, distance):
            self.forename = forename
            self.surname = surname
            self.distance = distance #PUT OUTSIDE INSTEAD OF INSEAD THE FUNCTION
    with open('Software/Assignments/2019/members.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newMember = Member(row[0], row[1], float(row[2]))
            members.append(newMember)
    return members


def findFuthestDistance(members):
    furthest = members[0].distance
    for index in range(1, len(members)):
        if members[index].distance > furthest:
            furthest = members[index].distance
    return furthest

def displayFurthestDistance(furthest):
    print("the furthest distance walked was " + str(furthest))
    
def writeToFileWinningMembers(furthest, members):
    with open('results.txt', 'w') as file:
        for index in range(len(members)):
            if members[index].distance > float(0.7) * float(furthest):
                file.write(members[index].forename + ", " + members[index].surname + '\n')
        file.write("the number of whole marathons walked by each member is: ")
        for index in range(len(members)):
            wholeMarathons = math.trunc(members[index].distance/26.22) 
            file.write(members[index].forename + ", "+ members[index].surname + ", "  + str(wholeMarathons) + "\n")



#main
members = readFromfileIntoRecords()
furthest = findFuthestDistance(members)
displayFurthestDistance(furthest)
writeToFileWinningMembers(furthest, members)

