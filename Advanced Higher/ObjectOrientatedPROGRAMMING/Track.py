class Track:
    #this is the constructor
    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = length

    def convertMinutes(self):
        min = self.length//60
        sec = seconds = self.length %60
        return min, sec
        
    def showTrack(self):
        min, sec =  self.convertMinutes()
        print(f"Title: {self.title} - Artist: {self.artist} ")
        print(min, sec)
        

        
class Track:
    self.title = title
    self.length = length
    self.artist = artist
    # function: convert into mintues
def convertMinutes(self):
    min = self.length //60 
    sec = self.length % 60
    return min, sec
def showTrack(self):
    min, sec = self.convertMinutes()
    print(self.artist + "wrote" + self.title + "which is" + str(min) + "minutes" and str(sec) + 'seconds' )

        


