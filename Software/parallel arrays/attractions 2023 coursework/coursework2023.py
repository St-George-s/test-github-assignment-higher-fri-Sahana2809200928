import csv

# Explain
def readfile():
    attractions = []
    category = []
    visitors = []
    daysOpen = []
    height = []
    
    with open('data flow/attractions 2023 coursework/attractions.csv', 'r') as file:
        reader = csv.reader(file) #reader represents whoel file
        for row in reader: #row represents arrays within file
            #following rows append corresponding data value to correct array group from each row
            attractions.append(row[0])
            category.append(row[1])
            visitors.append(int(row[2]))
            daysOpen.append(int(row[3]))
            height.append(row[4])
    
    return attractions, category, visitors, daysOpen, height

# Explain
def mostandleastVisited(attractions, visitors): 
# starting value will be first of visitors array and will get replaced if not true- also sets up the variable to beused in function
    highest = visitors[0]
    lowest = visitors[0]
    
    for x in range(len(visitors)): 
        if visitors[x] > highest: #assuming that no 2 attraction have had same number of visitors
            highest = visitors[x]
            highest_attraction = attractions[x]
            
        if visitors[x] < lowest:
            lowest = visitors[x]
            lowest_attraction = attractions[x]
    
    print("Lowest:", lowest_attraction)
    print("Highest:", highest_attraction)


def service_due_rollercoasters(attractions, category, daysOpen): #category to check if it is a rollercoaster, days open until service ad to attractions to write the correspinding rollercoaster name to the service.csv
    with open ('data flow/attractions 2023 coursework/service.csv', 'w') as file:    
        writer = csv.writer(file) #reader represents whoel file

        for x in range(len(attractions)): 
            if category[x] == "Roller Coaster":
                days= int(daysOpen[x]) % 90 # programme si given numbers that have not restarted after every service day, so mofulus findd number of days until next multiple of 90 is reached
                if 90 - days <= 7:
                    writer.writerow([attractions[x]]) # write the corresponding function


# Main Program
attractions, category, visitors, daysOpen, height = readfile() # functin readfile() return value is now aligned with listed variables
service_due_rollercoasters(attractions, category, daysOpen)
mostandleastVisited(attractions, visitors)


                         
               
               
               
               
    
     
     





    

        


                
              









  


   
