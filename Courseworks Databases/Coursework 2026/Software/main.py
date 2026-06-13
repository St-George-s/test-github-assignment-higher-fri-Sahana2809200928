import csv

#Read file into parallel arrays.
def readFromFile():
    tool= []
    manufacturer= []
    dateRented = []
    returned = []
    fee = []
    with open('Courseworks Databases/Coursework 2026/Software/tools.csv', 'r') as file:    
        reader = csv.reader(file)
        for row in reader:
            tool.append(row[0])
            manufacturer.append(row[1])
            dateRented.append(row[2])
            returned.append(row[3])
            fee.append(row[4])
    return tool, manufacturer, dateRented, returned, fee


#Find and display the name of each tool and the total number of tools by a chosen manufacturer.
#code works because every tool is assigned to only one manufacturer
def displayNameandNumberOfTools(tool, manufacturer):
    count = 0
    chosenManufacturer = input("enter a manufacturer: ")
    for index in range(len(manufacturer)):
        if manufacturer[index] == chosenManufacturer:
            count = count + 1 
            print(tool[index])
    print("total: " + str(count))


#Calculate late fee for tools rented in 2025 and not returned.
def calculateLateFee(dateRented, returned, fee):
    for index in range(len(tool)):
        if str(returned[index]) == "No" and str(dateRented[index][6:10]) == '2025':
            if int(dateRented[index][3:5]) <= 6: #access month by converting the substring taken from teh year which is a string
                fee[index] = int(fee[index] )+ 10
            else:
                fee[index] = int(fee[index]) + 5
    return fee
   

#Write the tool name, date rented and fee of any tool with a late fee to an external file.
def writeLateFeeToolsToFile(tools, dateRented, fee):
    with open ('lateTools.csv' ,'w' ) as file:
        for index in range(len(tools)):
            if int(fee[index]) != 0: # if fee has been added, add to seperate file
                file.write(str(tools[index]) + " " + dateRented[index] +" " + str(fee[index]) + '\n')


#main
tool, manufacturer, dateRented, returned, fee = readFromFile()
displayNameandNumberOfTools(tool, manufacturer)
fee = calculateLateFee(dateRented, returned, fee)
writeLateFeeToolsToFile(tool, dateRented, fee)






