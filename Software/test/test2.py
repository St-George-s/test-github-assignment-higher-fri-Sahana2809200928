import csv

def readGameData():
    with open ('Software/test/gamesExtended.csv', 'r') as file:
        gameTitles= []
        genres = []
        ageRatings = []  
        Platforms = []
        reader = csv.reader(file)
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(row[2])
            Platforms.append(row[3])
    return gameTitles, genres, ageRatings, Platforms


def countSuitableGames(genre_to_check):
    count = 0
    for index in range(len(genres)):
        if genres[index] == genre_to_check:
                print(genres[index])
                count = count + 1
    print(count)

def genre_count(genre_to_count):
    with open('platform_suitable_games.txt', 'w' ) as file:
        for index in range(len(gameTitles)):
            if str(genres[index]) == str(genre_to_count) and int(ageRatings[index]) < 18:
                file.write(str(gameTitles[index]) + "-" + Platforms[index])

          
          

    #main
gameTitles, genres, ageRatings, Platforms =readGameData()
genre_count("Sci-Fi")
countSuitableGames("Sci-Fi")
