import csv

def readFromFile():
    tools= []
    manufacturers= []
    dateRented = []
    returned = []
    fees = []
    with open('Courseworks Databases/Coursework 2026/Software/tools.csv', 'r') as file:    
        reader = csv.reader(file)
        for row in reader:
            tools.append(row[0])
            manufacturers.append(row[1])
            dateRented.append(row[2])
            returned.append(row[3])
            fees.append(row[4])
    return tools, manufacturers, dateRented, returned, fees


def displayNameandNumberOfTools(tools, manufacturers):
    count = 0
    chosenManufacturer = input("enter a manufacturer: ")
    for index in range(len(manufacturers)):
        if manufacturers[index] == chosenManufacturer:
            count = count + 1
            print(tools[index])
    print("total: " + str(count))


def calculateLateFee(dateRented, returned, fees):
    for index in range(len(dateRented)):
        if dateRented[index][6:10] == "2025" and returned[index] == "No":
            if int(dateRented[index][3:5])<=6:
                fees[index] = int(fees[index]) + 5
            else:
                fees[index] = int(fees[index]) + 10
    return fees


def writeLateFeeToolsToFile(tools, dateRented, fees):
    with open ('lateTools.csv' ,'w' ) as file:
        for index in range(len(tools)):
            if fees[index] != 0:
                file.write(str(tools[index]) + " "+dateRented[index] +" " +fees[index])

    
#main

tools, manufacturers, dateRented,returned, fees = readFromFile()
displayNameandNumberOfTools(tools, manufacturers)
fees = calculateLateFee(dateRented, dateRented, fees)
print(fees)
writeLateFeeToolsToFile(tools, dateRented, fees)





