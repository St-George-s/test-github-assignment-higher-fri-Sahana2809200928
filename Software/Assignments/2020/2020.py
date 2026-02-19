import csv

def getNewMemberData ():
    firstName = input("enter firstname")
    surname = input("enter surname")
    category= input("enter category")
    password = checkValidPassword()
    return firstName, surname, category, password


def checkValidPassword():
    valid = False
    while valid == False:
        password = input("enter a password")
        if ord(password[0]) >=65 and ord(password[0]) <=90 and ord(password[-1]) <=37 and ord(password[-1]) >=35:
            valid = True
    return password


def readAndDisplayData(firstName, surname, category, password):
    firstNames = []
    surnames = []
    categories = []
    passwords = []
    with open('Software/Assignments/2020/members.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            firstNames.append(row[0])
            surnames.append(row[1])
            categories.append(row[2])
            passwords.append(row[3])
    firstNames.append(firstName)
    surnames.append(surname)
    categories.append(category)
    passwords.append(password)
    for index in range(len(firstNames)):
        print(firstNames[index], surnames[index], categories[index])
    return categories
# Oliver Wilson, Adult, Ninjago$
    
#main
firstName, surname, category, password = getNewMemberData()
categories = readAndDisplayData(firstName, surname, category, password)


