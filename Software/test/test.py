import csv

def readGameDatafromCSV():
    with open("Software/test/gamesExtended.csv", "r") as file:
        gameTitles = []
        genres = []
        ageRatings = []
        Platform= []

        reader = csv.reader(file) 
        next(reader)
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(row[2])
            Platform.append(row[3])

            return(gameTitles, genres, ageRatings, Platform)

def countSuitableGames(genre_to_check):
    count = 0
    with open("Software/test/platform_suitable_games.txt", "w") as file:
        for index in global_gameTitles: 
            if global_genres[index] == genre_to_check and global_ageRatings[0] <18:
                print(global_gameTitles[index])
                count= count +1
                file.write(global_gameTitles[index], global_Platform[index])
        print(count)
    

#main

global_gameTitles, global_genres, global_ageRatings, global_Platform = readGameDatafromCSV()
countSuitableGames("Fantasy")

