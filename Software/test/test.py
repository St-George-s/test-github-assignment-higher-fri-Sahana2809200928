import csv

def readGameDatafromCSV():
    with open("Software/test/games.csv", "r") as file:
        gameTitles = []
        genres = []
        ageRatings = []
        reader = csv.reader(file) 
        next(reader)
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(row[2])

            return(gameTitles, genres, ageRatings)

def countSuitableGames(genre_to_check):
    count = 0
    for index in global_gameTitles: 
        if global_genres[index] == genre_to_check and global_ageRatings[0] <18:
            print(global_gameTitles[index])
            count= count +1
    print(count)

#main

global_gameTitles, global_genres, global_ageRatings = readGameDatafromCSV()
countSuitableGames()
