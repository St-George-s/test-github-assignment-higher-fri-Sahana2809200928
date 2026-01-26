import csv

def getData():
    with open('Database - Database Test/athletes.csv', 'r')as file:
        entryID = []
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



def bibValues(entryID, location, forename, surname):
    
    with open ('BibValues.csv', 'w' ) as file:
        for x in range(30):
             bibValue = (forename[x][0]) + surname[x] + str(ord(location[x][0]))
             file.write(bibValue + '\n')



def highestNumber(jumps):
    maxJumps = 0
    for x in range(len(jumps)):
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]


    return maxJumps

def namesHighestJump(forename, surname, jumps, maxJumps):
    for x in range(30):
        if jumps[x]== maxJumps:
            print(forename[x], surname[x] )


entryID, location, forename, surname, jumps = getData()
bibValues(entryID, location, forename, surname)
maxJumps =highestNumber(jumps)
namesHighestJump(forename, surname, jumps, maxJumps)
