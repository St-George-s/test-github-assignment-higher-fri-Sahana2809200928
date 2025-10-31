import csv

def getNewMember():
    Valid = False

    newMember = input("Newmember:")
    firstName = input("firstName:")
    Category = input("Category:")
    
    while Valid == False:
         Password = input("enter a password")
         if ord(Password[0]) <= 90 and ord(Password[0]) >=65 and ord(Password[-1]) <= 37 and ord(Password[-1]) >=35:
              Valid = True


    return newMember, firstName, Category, Password

     

def readFromFile():
    with open("Software/Assignments/2020/members (1).txt", "r") as file:

        Members = []
        firstNames = []
        Categories = []
        Passwords = []

        reader = csv.reader(file)

        Members.append(newMember)
        firstNames.append(firstName)
        Categories.append(Category)
        Passwords.append(Password)

        for row in reader:
            Members.append(row[0])
            firstNames.append(row[1])
            Categories.append(row[2])
            Passwords.append(row[3])
            
        print("our current members are:")
        for index in range(len(Members)):
             print(Members[index], firstNames[index], Categories[index] + "/n")



             
            
        return Members, firstNames, Categories, Passwords
    
def totals():
        count_Adult = 0
        count_Senior = 0
        count_Junior= 0
        for index in Categories:
            if index == "Adult":
                count_Adult += 1
            elif index == "Junior":
                 count_Junior += 1
            else:
                 count_Senior+=1
        Total_members = count_Adult + count_Senior + count_Junior
        print("The Total current membership " + str(Total_members))
        print("There are currently " + str(count_Adult) +  " Adult members")
        print("There are currently " + str(count_Senior) + " Senior members")
        print("There are currently " + str(count_Junior) + " Junior members")
                  

    
#main
newMember, firstName, Category, Password = getNewMember()
Members, firstNames, Categories, Passwords= readFromFile()
totals()

