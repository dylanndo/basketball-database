import csv
from player import Player

players = {}    # dictionary of playerName:Player()

# extract data from shots_data.csv
with open('shots_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        if row[0] in players:   #if player is in database already
            players[row[0]].addShot(row)
        else:   #otherwise add player first then add stats
            globals()[row[0]] = Player()
            players[row[0]] = row[0]
            players[row[0]].addShot(row)

