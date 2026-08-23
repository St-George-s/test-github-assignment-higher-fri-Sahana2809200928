import csv

def readFromFile(): #read from file into parralel arrays
    company = []
    numEmployees = []
    ceoSalary = []
    with open('Software/Assignments/2024/companies.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            company.append(row[0])
            numEmployees.append(int(row[1]))
            ceoSalary.append(int(row[2]))
    return company, numEmployees, ceoSalary

def findMaxPos(Array): # for any array given, made up of integers or floats, find the highest value inthis array. 
    maxPos = 0
    for index in range(len(Array)):
        if Array[index] > Array[maxPos]:
            maxPos = index
    return maxPos
        
def displayHighestCEOSalary(ceoSalary, company): #find and display the difference between the salary of the CEo for teh company entered by the user andthe salary of the higehst paid CEO
    companySearch = input("enter company you want to search")
    found = False
    maxPos = findMaxPos(ceoSalary)
    for index in range(len(company)):
        if company[index] == companySearch:
            found = True
            companyPos = index
    if found == True:
        salaryDifference = ceoSalary[maxPos] - ceoSalary[companyPos]
        print(company[maxPos] + " has the highest paid CEO and " + companySearch + " is paid " + str(salaryDifference ) + " less than "  + company[maxPos])
    else:
        print("company not found")

# def findHighestNumEmployees(numEmployees, ceoSalary): #find and display the highest number of employees employed  by any company and the number of companies that have a number of of employees within 10% of that figure
#     maxPos = findMaxPos(numEmployees)
#     count = 0
#     for index in range(len(numEmployees)):
#         if numEmployees[index] >=  ceoSalary[maxPos] * 0.9:
#             count = count + 1
#     print("number of companies that emply within 10% of highest numbe ro of employees is " + str(numEmployees[maxPos]))

        
        

#main
company, numEmployees, ceoSalary =  readFromFile()
displayHighestCEOSalary(ceoSalary, company)
# findHighestNumEmployees(numEmployees)


