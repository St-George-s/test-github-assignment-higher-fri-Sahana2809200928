
"""
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
     for index in range(1,len(Members)):
        if Members[index].distance > Furtherst_distance:
            Furtherst_distance = Members[index].distance
     print(Furtherst_distance)

name= 'sahana'
array = [0] * 8

array[7]='Sahana'
            
print(array)
       
print([False] * 4)
#MAIN
Members = readFile()
Furthest_distance()


import random
number= random.randint(0,4)
print(number)

Qoutient, remainder = divmod(150,60)
print(Qoutient, remainder)
data= ("sAHANA, oSCAR, HELLO, HI")
with open("Hi.csv", 'w') as file:
     with file:
          writer = csv.writer(file)
          writer.writerrows(data)

"""


class Recipe:
    ingridient:str = ""
    number: int = 0

allRecipes = [Recipe() for x in range(20)]
allRecipes[2].ingridient = "Strawberry"
print(allRecipes[2].ingridient)

import random
number = random.randint(0,2)
print(number)


class Player:
    name: str= ""
    age : int = 0

Players = [Player() for x in range(20)]
Players = []
for x in range(20):
    Players.append(Player())

