import csv #FILE ON WHICH INFORMATON IS EXTRACTED FROM

def validpassword(password):
   valid = False #VALID IS SET TO FALSE TO START THE INFINITE LOOP UNTIL CONDIIOTN IS MET
   while not valid: #PASSWORD WILL BE CHECKED AGAINST CONDIITONS UNTIL IT CORRECTLY MEETS TEH CONDITIONS
     # password - first value a letter in caps and a symbol as the very last value
     if (65 <= ord(password[0]) <= 90) and (password[-1]  == "#"or password[-1]  ==  "$"or password[-1]  == "%"):
            valid = True
    # valid passwword
     else:
       password = input("password again, not valid")
   return password #THIS 
   #invalidpassword

#USE FUNCTION TO GET ALLIN FORMATION FROMA MEMMBER
def getnewmember():
  first_name = input("enter first name")
  surname = input("enter surname")
  category= input("enter cateogry")
  password = input("enter password")
  password = validpassword(password)                  
  return first_name, surname, category, password


def readfromfile(first_name, surname, category, password):
   #CREATE ARRAYS TO STORE VALUES OF ALL MEMBERS
   firstNames = []
   surnames = []
   categories = []
   passwords = []
   #APPEND THE DATA OF THE NEW MEMBER INTO THE CREATD ARRAYS
   firstNames.append(first_name)
   surnames.append(surname)
   categories.append(category)
   passwords.append(password)
 #COPY THE RELETIVE PATH, IN ORDER TO OPEB TEH FILE
   with open("data flow/2022 course work.py/members.csv", "r") as file:
      reader = csv.reader(file) 
      next(reader)
      for row in reader: #SPLITS EACH ROW IN TEH FIEL INTO AN ARRRAY TO MAKE A 2D ARRAY 
         firstNames.append(row[0]) #moves through all the rows and appends sperate values into respective arrays
         surnames.append(row[1])
         categories.append(row[2])
         passwords.append(row[3])
      #prints all teh arrays
   print(firstNames)
   print(surnames)
   print(categories)
   print(passwords)

   
   

def different_category_count(category):
   junior = 0 #declare variables for 3 categories + total
   adult = 0
   senior = 0
   total = len(category)
   for x in range(len(category)): #x is the coutnbter and moves sequentially through teh array and if it lands on a category that mathces one of teh 3 variables, 1 is added to the actegories
      if category[x] == "Junior":
         junior = junior + 1
      elif category[x] == "Senior":
         senior = senior + 1
      else:
         adult = adult + 1
   print(junior, senior, adult, total)


#Main
first_name, surname, category, password = getnewmember() #aligns 4 variables with those returned from the getnewmember function 
category = readfromfile(first_name, surname, category, password) #linked to previous step pass in teh correct variables
print(different_category_count(category)) #pass in parameters to be used in functin









   
#comment all the subprogrammes adn the main


 
  
  
