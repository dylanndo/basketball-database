import csv
from player import Player
from menu import Menu

players = {}    # dictionary of Player objects
userInput = ""  # user's input/choice
menuOption = 0

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

while(userInput.lower() != "done" and menuOption != 6):
    userInput = input("Who's statistics would you like to access? (Type 'done' to exit) ")

    if userInput in players:
        menuOption = Menu.mainMenu()

        if menuOption == 1:
            menuOption = Menu.zoneMenu1()

            if menuOption == 1:
                Menu.printFGp2PT(players[userInput])
            elif menuOption == 2:
                Menu.printFGp3PT(players[userInput])
            elif menuOption == 3:
                Menu.printFGpC3(players[userInput])
            elif menuOption == 4:
                Menu.printFGpNC3(players[userInput])
            elif menuOption == 5:
                Menu.printFGp(players[userInput])
            elif menuOption == 6:
                Menu.printAllFGp(players[userInput])
        
        elif menuOption == 2:
            menuOption = Menu.zoneMenu2()

            if menuOption == 1:
                Menu.printZone2PT(players[userInput])
            elif menuOption == 2:
                Menu.printZone3PT(players[userInput])
            elif menuOption == 3:
                Menu.printZoneC3(players[userInput])
            elif menuOption == 4:
                Menu.printZoneNC3(players[userInput])
            elif menuOption == 5:
                Menu.printAllZones(players[userInput])

        elif menuOption == 3:
            menuOption = Menu.zoneMenu1()

            if menuOption == 1:
                Menu.printEFGp2PT(players[userInput])
            elif menuOption == 2:
                Menu.printEFGp3PT(players[userInput])
            elif menuOption == 3:
                Menu.printEFGpC3(players[userInput])
            elif menuOption == 4:
                Menu.printEFGpNC3(players[userInput])
            elif menuOption == 5:
                Menu.printEFGp(players[userInput])
            elif menuOption == 6:
                Menu.printAllEFGp(players[userInput])

        elif menuOption == 4:
            Menu.printAllFGp(players[userInput])
            print()
            Menu.printAllZones(players[userInput])
            print()
            Menu.printAllEFGp(players[userInput])

        elif menuOption == 5:
            break            
            
    else:
        print("This player is not in the database. Enter anything to continue ")
    
    menuOption = 0

