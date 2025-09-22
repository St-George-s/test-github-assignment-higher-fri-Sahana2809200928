
import csv

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
            visitors.append(row[2])
            daysOpen.append(row[3])
            height.append(row[4])
    
    return attractions, category, visitors, daysOpen, height

attractions, category, visitors, daysOpen, height = readfile() # functin readfile() return value is now aligned with listed variables






def mostandleastVisited(attractions, visitors): 
# starting value will be first of visitors array and will get replaced if not true- also sets up the variable to beused in function
    Highest = visitors[0]
    Lowest = visitors[0]
    
    for x in range(len(visitors)): 
        if int(visitors[x]) > int(Highest): #assuming that no 2 attraction have had same number of visitors
            Highest = int(visitors[x])
            Highest_attraction = attractions[x]
            
        if int(visitors[x]) < int(Lowest):
            Lowest = visitors[x]
            Lowest_attraction = attractions[x]
    
    print("Lowest:", Lowest_attraction)
    print("Highest:", Highest_attraction)







def service_due_rollercoasters(attractions, category, daysOpen): #category to check if it is a rollercoaster, days open until service ad to attractions to write the correspinding rollercoaster name to the service.csv
    for x in range(len(attractions)): 
                 if category[x] == "Roller Coaster":
                    days= int(daysOpen[x]) % 90 # programme si given numbers that have not restarted after every service day, so mofulus findd number of days until next multiple of 90 is reached
                    if 90 - days <= 7:
                         with open ('data flow/attractions 2023 coursework/service.csv', 'w') as file:
                            file.write(attractions[x]) # write the corresponding function


service_due_rollercoasters(attractions, category, daysOpen)
mostandleastVisited(attractions, visitors)


                         
               
               
               
               
    
     
     





    

        


                
              









  


   
