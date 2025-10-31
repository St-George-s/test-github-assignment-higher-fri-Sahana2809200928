import csv
class Game(): 
    def __init__(self, gameTitle, genre, ageRating, platform):
        #ALL ATRIBUTES
        self.gameTitle = gameTitle
        self.genre = genre
        self.ageRating = ageRating
        self.ageRating = ageRating
        self.platform = platform

def readGameDatafromCSV():
    games = []#WHERE TEH ATTRIBUTES FOR GAMES WILL BE STORED
    with open("Software/test/gamesExtended.csv", "r") as file:
        #reader is equal to whole CSV file
        reader = csv.reader(file) 
        for row in reader:
           #loop through each row which are made int eh sam format, add each component into a parallelarrays
           newGame = Game(row[0], row[1], int(row[2]), row[3]) #EACH ROW HAS BEEN SPERATED INTO INDIVIDUAL ARRAY
           games.append(newGame)
        return games

# Part B
def countSuitableGames(games, genre_to_check):
    count = 0
    for index in range (len(games)): 
        if games[index].genre == genre_to_check and games[index].ageRating <18: #it is assumed that the CSSV is in parallel arrays, and that attributes that belong to same game.
            count= count +1
    print(count) #after for loop, how many games meet conditions
        
#Part C
def writeSuitableGames(games, genre_to_check, platform_to_check):
    count = 0
    with open("Software/test/platform_suitable_games.txt", "w") as file:
        for index in range(len(games)): 
            if platform_to_check == games[index].platform and games[index].genre == genre_to_check and games[index].ageRating <18: #MEETS CONDITIONS
                count= count +1
                file.write(games[index].gameTitle + "-" + games[index].platform)
    

#main


games = readGameDatafromCSV() #C
countSuitableGames(games, "Fantasy")
writeSuitableGames(games, "Fantasy", "PC", )


