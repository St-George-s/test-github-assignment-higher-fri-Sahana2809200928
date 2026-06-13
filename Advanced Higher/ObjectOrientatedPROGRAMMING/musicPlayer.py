from Album import Album
from AlbumTrack import AlbumTrack

album = Album( "Lana Del Ray ", "Sirens")
album.addTrack(AlbumTrack("Next to Me", "Lana del ray", 250, "Sirens"))
album.addTrack(AlbumTrack("For K", "lana del ray", 300,  "Sirens"))
album.printSongs()

album1 = Album("Lana Del Ray", "born to die")
album. addTrack(AlbumTrack("national anthem", "Lana del Ray", 400, "born to die"))
album. addTrack(AlbumTrack("diet mountain dew", "Lana del Ray", 450, "born to die"))
album.printSongs()



