import csv 

def get_newMemberData():
    firstName = input("enter first name")
    surName = input("enter surname")
    category = input("enter category")
   
    Valid = False
    while Valid == False:
        password = input("enter password")
        if ord(password [0]) <=90 and ord(password[0]) >=65 and ord(password [-1]) <=37 and ord(password[-1]) >=35:
            Valid = True
    return firstName, surName, category, password

def readFile():
    firstNames= [] 
    surNames= []
    categories= []
    passwords = []
    with open("Software/Assignments/2020/members (1).txt", 'r' ) as file:
        reader = csv.reader(file)
        for row in reader:
            firstNames. append(row[0])
            surNames.append(row[1])
            categories.append(row[2])
            passwords.append(row[3])
        print(firstNames, surNames,categories, passwords)


firstName, surName, category, password = get_newMemberData()

readFile()

