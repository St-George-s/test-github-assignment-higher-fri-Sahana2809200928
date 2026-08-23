import csv

def readData():
    attraction = []
    category = []
    visitor = []
    daysOpen = []
    height = []
    with open('Software/Assignments/2023/attractions.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            attraction.append(row[0])
            category.append(row[1])
            visitor.append(int(row[2]))
            daysOpen.append(row[3])
            height.append(row[4])
        
    return attraction, category, visitor, daysOpen, height


def displayMostAndLeastVisited(attraction, visitor):
    mostVisited = int(visitor[0])
    leastVisited = int(visitor[0])

    for index in range(len(attraction)):
        if int(visitor[index]) < leastVisited:
            leastVisited = visitor[index]
        elif int(visitor[index]) > mostVisited:
            mostVisited = visitor[index]

    print("mostVisited: ")
    for index in range(len(attraction)):
        if visitor[index] == mostVisited:
            print(attraction[index])

    print("least visited")
    for index in range(len(visitor)):
        if visitor[index] == leastVisited:
            print(attraction[index])



    
def writeToFileAttractionsForService(attraction, daysOpen, category):
    with open('service.csv', 'w') as file:
        for index in range(len(attraction)):
            if category[index] =='Roller Coaster':
                days = int(daysOpen[index]) % 90
                if (90-days) <= 7:
                    file.write(attraction[index] + '\n')

def updateHeightRestriction(height):
    for index in range(len(height)):
        if height[index][0] == '1':
            height[index] = '1.4m'
        

#main
attraction, category, visitor, daysOpen, height = readData()

displayMostAndLeastVisited(attraction, visitor)

writeToFileAttractionsForService(attraction, daysOpen, category)

updateHeightRestriction(height)
print(height)

print(695% 90)