class Track:
    #thi is the constructor
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
        


