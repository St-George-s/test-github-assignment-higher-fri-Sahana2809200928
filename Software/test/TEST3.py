import csv

titles = []


def readGameDataFromCSV():
    with open("games.CSV", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            titles.a