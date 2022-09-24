import csv
from player import Player

players = {}    # dictionary of Player objects

# extract data from shots_data.csv
with open('shots_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        name = row[0]
        if name in players:   #if player is in database already
            players.get(name).addShot(row)
        else:   #otherwise add player first then add stats
            globals()[name] = Player()
            players[name] = (globals()[name])
            players.get(name).addShot(row)

for x in players:
    print("Stats for " + x + ":")
    players.get(x).printStats()
    print()