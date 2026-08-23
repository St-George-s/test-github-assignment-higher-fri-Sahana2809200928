from Track import Track

class AlbumTrack(Track): #an extension of class Track
    def __init__(self, title, artist, length, album_name):
        super().__init__(title, artist, length)
        self.album_name = album_name
        
    def get_album(self):
        return self.album_name


song = AlbumTrack("Sultans of swing", "Dire straits", 250, "hi")
song.showTrack()

class Person:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = int(salary)
    
    def introduce(self):
        print('my name is' + self.name)
    
    def showSalary(self):
        print(self.name + 'has a salary of' + str(self.salary))

class Employee(Person):
    def __init__(self, name , salary, company):
        super().__init__(name, salary)
        self.__company = company
    def introduce(self):
        print('hello my name is' + self.name + "and work in " + self.company)
    def showWork(self):
        print('I work in' + self.company)

employee1 = Employee('sahana', 2000, 'google')
employee1.showWork()


    


