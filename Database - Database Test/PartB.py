import csv

def getData():
    with open('Database - Database Test/athletes.csv', 'r') as file:
        entryID = []   #declare arrays
        location = []
        forename= []
        surname=[]
        jumps=[]
        reader = csv.reader(file)
        for row in reader:
            entryID.append(row[0])
            location.append(row[1])
            forename.append(row[2])
            surname.append(row[3])
            jumps.append(int(row[4]))
    return entryID, location, forename, surname, jumps

# write to file the entry Id THEN GENRARETED BIB VALUE
def generate_bibValues(entryID, location, forename, surname):
    with open ('BibValues.csv', 'w' ) as file:
        for x in range(30):
             bibValue = (forename[x][0]) + surname[x] + str(ord(location[x][0])) #find position in array and take first letter from 
             file.write(entryID[x] + " " + bibValue + '\n')

# highest jumps
def findHighestNumber(jumps):
    maxJumps = jumps[0] #
    for x in range(1, len(jumps)):
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]
    return maxJumps

#There can be only one highest number of jumps but many people athletes can have the same number of jumps so if j 
def displayNamesHighestJump(forename, surname, jumps, maxJumps):
    for x in range(30):
        if jumps[x]== maxJumps:
            print(forename[x], surname[x] )
"""
def numberFinalists(location):
    countC = 0
    countI = 0
    countK = 0
    countM = 0
    for x in range(30):
        if location[x] == 'Coatbridge':
            countC+=1
        elif location[x] == 'Inverness':
            countI+=1
        elif location[x] == 'Kirkcaldy':
            countK+=1
        elif location[x]== "Motherwell":
            countM +=1

    print("Coatbridge has" + " "+str(countC)+" "+ "finalists")
    print("Inverness has" +" "+ str(countI) +" "+ "finalists")
    print("Kirkcaldy has" +" "+ str(countK) + " "+"finalists")
    print("Motherwell has" + " " +  str(countM) +" "+ "finalists")
"""

def numberFinalists(Locations):
    dif_locations = []
    for loc in Locations:
        if loc not in dif_locations:
            dif_locations.append(loc)

    for difLoc in dif_locations:
        count = 0
        for loc in Locations:
            if difLoc == loc:
                count+= 1
        print(difLoc + "has" + str(count) + "finalists")
            





         


#main
entryID, Locations, forename, surname, jumps = getData()
generate_bibValues(entryID, Locations, forename, surname)
maxJumps = findHighestNumber(jumps)
displayNamesHighestJump(forename, surname, jumps, maxJumps)
numberFinalists(Locations)