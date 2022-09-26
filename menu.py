class Menu():
    # main menu

    def mainMenu():
        print("What would you like to access?")
        print("1) Field Goal Percentage")
        print("2) Attempted Zone Percentage")
        print("3) Effective Field Goal Percentage")
        print("4) Everything")
        print("5) New Player")
        print("6) Quit")
        return int(input("Please enter a number to choose: "))

    # asks user which zone they want their stats for
    def zoneMenu1():
        print("Which zone would you like to access?")
        print("1) 2 Pointers")
        print("2) Three Pointers")
        print("3) Corner Three")
        print("4) Non Corner Three")
        print("5) Overall")
        print("6) Everything")
        return int(input("Please enter a number to choose: "))

    def zoneMenu2():
        print("Which zone would you like to access?")
        print("1) 2 Pointers")
        print("2) Three Pointers")
        print("3) Corner Three")
        print("4) Non Corner Three")
        print("5) Everything")
        return int(input("Please enter a number to choose: "))


    # prints field goal percentage
    def printFGp2PT(player):
        print("Field goal percentage (2PT): " + str(player.getFGp2PT()))
    def printFGp3PT(player):
        print("Field goal percentage (3PT): " + str(player.getFGp3PT()))
    def printFGpC3(player):
        print("Field goal percentage (C3): " + str(player.getFGpC3()))
    def printFGpNC3(player):
        print("Field goal percentage (NC3): " + str(player.getFGpNC3()))
    def printFGp(player):
        print("Field goal percentage (overall): " + str(player.getFGp()))

    def printAllFGp(self, player):
        Menu.printFGp2PT(player)
        Menu.printFGp3PT(player)
        Menu.printFGpC3(player)
        Menu.printFGpNC3(player)
        Menu.printFGp(player)

    # prints attempted zone percentage
    def printZone2PT(player):
        print("Percentage of shots attempted in 2PT Zone: " + str(player.getZone2PT()))
    def printZone3PT(player):
        print("Percentage of shots attempted in 3PT Zone: " + str(player.getZone3PT()))
    def printZoneC3(player):
        print("Percentage of shots attempted in C3 Zone: " + str(player.getZoneC3()))
    def printZoneNC3(player):
        print("Percentage of shots attempted in NC3 Zone: " + str(player.getZoneNC3()))

    def printAllZones(player):
        Menu.printZone2PT(player)
        Menu.printZone3PT(player)
        Menu.printZoneC3(player)
        Menu.printZoneNC3(player)

    # prints effective field goal percentage
    def printEFGp2PT(player):
        print("Effective field goal percentage (2PT): " + str(player.getEFGp2PT()))
    def printEFGp3PT(player):
        print("Effective field goal percentage (3PT): " + str(player.getEFGp3PT()))
    def printEFGpC3(player):
        print("Effective field goal percentage (C3): " + str(player.getEFGpC3()))
    def printEFGpNC3(player):
        print("Effective field goal percentage (NC3): " + str(player.getEFGpNC3()))
    def printEFGp(player):
        print("Effective field goal percentage (overall): " + str(player.getEFGp()))

    def printAllEFGp(player):
        Menu.printEFGp2PT(player)
        Menu.printEFGp3PT(player)
        Menu.printEFGpC3(player)
        Menu.printEFGpNC3(player)
        Menu.printEFGp(player)