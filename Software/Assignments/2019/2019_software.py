
import csv
class Member:
        def __init__(self, forename, surname, distance):
            self.forename = forename
            self.surname = surname
            self.distance = distance

def readFile():
    Members = []
    with open ('Software/Assignments/Member_walks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newMember = Member(row[0], row[1], row[2])
            Members.append(newMember)
    return Members

def Furthest_distance():
     Furtherst_distance = Members[0].distance
     for index in range(len(Members)):
        if Members[index].distance > Furtherst_distance:
            Furtherst_distance = Members[index].distance
     print(Furtherst_distance)


#MAIN
Members = readFile()
Furthest_distance()



          


