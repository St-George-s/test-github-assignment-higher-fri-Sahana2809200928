from Track import Track

class AlbumTrack(Track): #an extension of class Track
    def __init__(self, title, artist, length, album_name):
        super().__init__(title, artist, length)
        self.album_name = album_name
        
    def get_album(self):
        return self.album_name


song = AlbumTrack("Sultans of swing", "Dire straits", 250, "hi")
song.showTrack()

