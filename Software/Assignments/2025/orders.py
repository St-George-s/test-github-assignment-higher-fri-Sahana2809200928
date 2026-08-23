import csv

def readFromFile():
    company = []
    numEmployees = []
    ceoSalary = []
    with open('Software/Assignments/2025/companies.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            company.append(row[0])
            numEmployees.append(row[1])
            ceoSalary.append(row[2])
    return company, numEmployees, ceoSalary

def findMaxPos(array):
    maxPos = 0
    for index in range (len(array)):
        if array[index] > array[maxPos]:
            maxPos = index
    return maxPos



def findHighestCEOSalary(company, ceoSalary):
    chosenCompany = input("enter chosen company")
    found = False
    maxPos  = findMaxPos(ceoSalary)
    for index in range(len(company)):
        if company[index] == chosenCompany:
            found = True
            companyPos = index
    if found == True:
        salaryDifference = int(ceoSalary[maxPos]) -  int(ceoSalary[companyPos])
        print("the company with highest CEO salary is " + str(company[maxPos]))
        print(chosenCompany + " has a salary differenc of " + str(salaryDifference) + " with the salary of the higehst paid ceo"  )
    else:
        print("company not found")


def highestNumEmployees(numEmployees):
    count = 0
    highestNumPos = findMaxPos(numEmployees)
    for index in range(len(numEmployees)):
        if int(numEmployees[index]) > (int(numEmployees[highestNumPos])* 90)/100:
            count+=1
    print("the number of companies that employ within 10% of the company with highest number of employees is " + str(count))

#main
company, numEmployees, ceoSalary = readFromFile()
findHighestCEOSalary(company, ceoSalary)
highestNumEmployees(numEmployees)

        
