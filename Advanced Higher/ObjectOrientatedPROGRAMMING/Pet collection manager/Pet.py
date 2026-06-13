class Pet:
    def __init__(self, name, type, age, hunger):
        self.name = name
        self.type = type
        self.age = age
        self.hunger = hunger

    def showPet(self):
        print(f"name: {self.name} - type: {self.type} -age: {self.age} - hunger: {self.hunger}") 

    def feed(self):
        self.hunger = int(self.hunger) -1
    
    def isHungry(self):
        if self.hunger >5:
            return(True)
        else:
            return(False)
    