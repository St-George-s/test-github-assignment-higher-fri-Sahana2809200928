from Pet import Pet

Valid = True 

array = []
#data
array.append(Pet("Oscar", "Cat", 4, 5))
array.append(Pet("Leo", "Fish",5, 7))
array.append(Pet("Fluffy", "Dog", 2, 8))

def getInputs():
    name = input("name")
    type = input("type")
    age = int(input("age"))
    hunger = int(input("hunger"))
    newPet = Pet(name, type, age, hunger)
    array.append(newPet)

def displayPets():
    for x in range(len(array)):
         array[x].showPet()
        
def searchPet():
    Found = False
    index = -1
    enterName = input("enter name")
    for x in range(len(array)):
        if array[x].name == enterName:
            print("pet Found")
            Found = True
            index = x
    if Found == False:
        print("pet not found")
    
    return index

def Feedpet():      
    index = searchPet()                                      
    if index != -1 and array[index].hunger>5:
        array[index].feed()
    print(array[index].hunger)



def print_tombstone(name):
    print(f"""
      _________
     /         \\
    /   RIP     \\
   /  {name[:7]:^7}\\
  /                \\
  |             |
  |             |
  |             |
  |_____________|
    """)
def Terminate():
    index = searchPet()

    if index != -1:
        pet = array[index]

        # tombstone marker (instead of removing)
        pet.deleted = True

        # optional: clear visible data but keep object alive
        pet.name_backup = pet.name
        pet.name = "DELETED"

        print_tombstone(pet.name_backup)


def addPet(new_pet, array):
    x = 0
    while x > len(array) and array[x].name[0] < new_pet.name[0]:
        x += 1
    
    
while Valid == True:
    answer = int(input("which one -add pet, view, search, feed, exit , enter 1 - 6 "))
    if answer == 1:
        getInputs()
        displayPets()
    elif answer ==2:
        displayPets()
    elif answer ==3:  
        searchPet()
    elif answer ==4:
        Feedpet()
    elif answer == 5:
        Valid = False
    elif answer == 6:
        Terminate()
        displayPets()
    else:
        print("invalid")
    
v

petEmojis = {
    "cat": "🐈",
    "dog": "🐶", 
    "Fish": "🐟"
}

petEmojis["cat"]




