class Menu():
    # main menu

    def mainMenu():
        print("What would you like to access?")
        print("1) Field Goal Percentage")
        print("2) Attempted Zone Percentage")
        print("3) Effective Field Goal Percentage")
        print("4) Everything")
        print("5) Back")
        return int(input("Please enter a number to choose: "))

    # asks user which zone they want their stats for
    def zoneMenu():
        print("Which zone would you like to access?")
        print("1) 2 Pointers")
        print("2) Three Pointers")
        print("3) Corner Three")
        print("4) Non Corner Three")
        print("5) Everything")
        print("6) Back")
        return int(input("Please enter a number to choose: "))

    # prints attempted zone percentage
    def printZone2PT(player):
        print("Percentage of shots attempted in 2PT Zone: " + str(player.getZone2PT()))
    def printZone3PT(player):
        print("Percentage of shots attempted in 3PT Zone: " + str(player.getZone3PT()))
    def printZoneC3(player):
        print("Percentage of shots attempted in C3 Zone: " + str(player.getZoneC3()))
    def printZoneNC3(player):
        print("Percentage of shots attempted in NC3 Zone: " + str(player.getZoneNC3()))
    def printAllZones(self, player):
        self.printZone2PT(player)
        self.printZone3PT(player)
        self.printZoneC3(player)
        self.printZoneNC3(player)



