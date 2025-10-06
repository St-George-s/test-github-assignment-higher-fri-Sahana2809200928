import csv

def readGameDatafromCSV():
    with open("Software/test/gamesExtended.csv", "r") as file:
        gameTitles = []
        genres = []
        ageRatings = []
        platform= []

        reader = csv.reader(file) 
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(row[2])
            platform.append(row[3])

            return gameTitles, genres, ageRatings, platform

# Part B
def countSuitableGames(gameTitles, genres, ageRatings, genre_to_check):
    count = 0
    for counter in range (len(gameTitles)): 
        if genres[counter] == genre_to_check and ageRatings[counter] <18:
            count= count +1
    print(count)
        
# Part C
# def countSuitableGames(gameTitles, genres, ageRatings, genre_to_check):
#     count = 0
#     with open("Software/test/platform_suitable_games.txt", "w") as file:
#         for index in gameTitles: 
#             if genres[index] == genre_to_check and ageRatings[0] <18:
#                 count= count +1
#                 file.write(gameTitles[index], global_Platform[index])
    

#main

# globa_gameTitles, global_genres, global_ageRatings, global_Platform = readGameDatafromCSV()
# countSuitableGames(globa_gameTitles,  global_genres, global_ageRatings,"Fantasy")
countSuitableGames(["GTA 6", "Assasin's creed"], ["Action", "Action"], [18, 18],"Action")
