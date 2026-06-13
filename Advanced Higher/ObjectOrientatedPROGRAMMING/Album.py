
class Album:
    def __init__(self, title, artist):
            self.title = title
            self.artist = artist
            self.songs = []

    def printAlbum(self):
        print("Title;" + self.title + "Arist:" + self.artist)

    def addTrack(self, track):
        print(self, track)
        self.songs.append(track)

    def printSongs(self):
         for t in self.songs:
              print(t.title)
     


