import csv

def readGameDatafromCSV():
    with open("Software/test/gamesExtended.csv", "r") as file:
        gameTitles = []
        genres = []
        ageRatings = []
        platforms= []

        reader = csv.reader(file) 
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(int(row[2]))
            platforms.append(row[3])

        return gameTitles, genres, ageRatings, platforms

# Part B
def countSuitableGames(gameTitles, genres, ageRatings, genre_to_check):
    count = 0
    for index in range (len(gameTitles)): 
        if genres[index] == genre_to_check and ageRatings[index] <18:
            count= count +1
    print(count)
        
#Part C
def countSuitableGames(gameTitles, genres, ageRatings, genre_to_check, platform_to_check, platforms):
    count = 0
    with open("Software/test/platform_suitable_games.txt", "w") as file:
        for index in range(len(genres)): 
            if platform_to_check == platforms[index] and genres[index] == genre_to_check and ageRatings[index] <18:
                count= count +1
                file.write(gameTitles[index] + "-" + global_Platform[index])
    

#main


global_gameTitles, global_genres, global_ageRatings, global_Platform = readGameDatafromCSV()
countSuitableGames(global_gameTitles,  global_genres, global_ageRatings,"Fantasy", "PC", global_Platform)

