import csv

def readGameDataFromCSV():
    with open('Software/Assignments/TEST/gamesExtended.csv', 'r') as file:
        gameTitles = []
        genres= []
        ratings = []
        Platforms = []

        reader = csv.reader(file)
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ratings.append(row[2])
            Platforms.append(row[3])

        return(gameTitles, genres, ratings, Platforms)

def CountSuitableGames(genre_to_check):
    count = 0
    for x in range(len(genres)):
        if genres[x] == genre_to_check and int(ratings[x]) <18:
            count = count + 1
    print(count)
   
def CountSuitableGamesOnPlatform(genre_to_check):
    with open ("platform_suitable_games.txt", "w") as file:
        count = 0
        for index in range(len(genres)):
            if genres[index] == genre_to_check and int(ratings[index]) <18 :

                newRow = (gameTitles[index] + "-" + Platforms[index])
                file.write(newRow)
            
        



#main
gameTitles, genres, ratings, Platforms = readGameDataFromCSV()

CountSuitableGames("Fantasy")

CountSuitableGamesOnPlatform("Fantasy")


