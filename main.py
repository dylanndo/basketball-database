import csv
from player import Player
from menu import Menu

players = {}    # dictionary of Player objects
userInput = ""  # user's input/choice
mainMenuOption = 0
menuOption = 0
quit = False    # true if user wants to quit program
bypass = False  # true in the instance that user wants to choose a new player, skips main menu

# extract data from shots_data.csv
with open('shots_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        name = row[0].upper()
        if name in players:   #if player is in database already
            players.get(name).addShot(row)
        else:   #otherwise add player first then add stats
            globals()[name] = Player()
            players[name] = (globals()[name])
            players.get(name).addShot(row)

while(quit == False):   # while user hasn't quit
    print()
    if bypass == False: # if user hasn't chosen to select a new player, get a main menu option
        mainMenuOption = int(float(Menu.mainMenu()))
        print()

    if mainMenuOption == 1: # ask for which player to access
        userInput = input("Who's statistics would you like to access? (Type 'done' to exit): ").upper()
        print()

        if(userInput.lower() == "done"):    # if user is done, quit
            quit = True

        else:
            while not userInput in players:    # while user has input an invalid player
                print("This player is not in the database.")
                print()
                userInput = input("Who's statistics would you like to access? (Type 'done' to exit): ").upper()
                print()
                if(userInput.lower() == "done"):    # if user is done, quit
                    quit = True


            menuOption = int(float(Menu.playerStatsScreen()))   # options for stats
            print()

            # please refer to menu.py for descriptions of choices and methods
            if menuOption == 1:
                menuOption = int(float(Menu.zoneMenu1()))
                print()

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
                menuOption = int(float(Menu.zoneMenu2()))
                print()

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
                menuOption = int(float(Menu.zoneMenu1()))
                print()

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
                print()
                print("Statistics for " + userInput + ":")
                Menu.printAllFGp(players[userInput])
                print()
                Menu.printAllZones(players[userInput])
                print()
                Menu.printAllEFGp(players[userInput])
                print()

            elif menuOption == 5:
                bypass = True
                
            elif menuOption == 6:
                bypass = False

            elif menuOption == 7:
                quit = True
            
    # display players
    elif mainMenuOption == 2:
        print()
        print("Here is a list of the players in our current database:")
        
        for x in players:
            print(x)
        
        print()

    # quit
    elif mainMenuOption == 3:
        quit = True
