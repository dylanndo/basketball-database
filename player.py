class Player():
    def __init__(self):
        # lists of raw extracted data
        self.two = []
        self.cornerThree = []
        self.nonCornerThree = []

        # count of attempted shots
        self.attempted2PT = 0
        self.attemptedC3 = 0
        self.attemptedNC3 = 0
        self.attempted3 = 0 #C3 + NC3

        # count of made shots
        self.made2PT = 0
        self.madeC3 = 0
        self.madeNC3 = 0
        self.made3 = 0  #C3 + NC3

        # percentage of shots taken
        self.zone2PT = 0.0
        self.zoneC3 = 0.0
        self.zoneNC3 = 0.0
        self.zone3 = 0.0    #C3 + NC3

        # effective field goal percentage
        self.eFGp2PT = 0.0
        self.eFGpC3 = 0.0
        self.eFGpNC3 = 0.0
        self.eFGp3 = 0.0    #C3 + NC3

    # extracts data from given row in CSV File
    def addShot(self, row):
        if(abs(float(row[2])) <= 7.8):  # if shot was taken within 7.8 ft from the x-axis (x <= 7.8)
            if(abs(float(row[1])) < 22):   # inside 22ft from the corner = two pt
                self.attempted2PT += 1  # +1 to 2pt attempt
                if(int(row[3]) == 1):   # +1 to 2pt made
                    self.made2PT += 1    
                self.two.append(row)    # add data to two pointers list 

            else:   # 22ft and beyond from the corner = corner three
                self.attemptedC3 += 1  # +1 to corner 3 attempt
                self.attempted3 += 1     # +1 to 3 attempt
                if(int(row[3]) == 1):   # +1 to corner 3 and 3 made
                    self.madeC3 += 1    
                    self.made3 += 1 
                self.cornerThree.append(row)    # add data to corner 3 list 
            
        else:   # if shot was taken beyond 7.8 ft from the x-axis (x > 7.8 ft)
            if(float(row[1])**2 + float(row[2])**2 < 564.0625):   #pyt. theorem - inside 23.75ft from the arc = two pt
                self.attempted2PT += 1  # +1 to 2pt attempt
                if(int(row[3]) == 1):   # +1 to 2pt made
                    self.made2PT += 1    
                self.two.append(row)    # add data to two pointers list 

            else:   # 23.75ft and beyond from the arc = non corner three
                self.attemptedNC3 += 1  # +1 to non corner 3 attempt
                if(int(row[3]) == 1):   # +1 to non corner 3 made
                    self.madeNC3 += 1    
                self.nonCornerThree.append(row)    # add data to non corner 3 list

    # calculates percentage of shots attempted in zone
    def calculateZone(self, zoneAttempted):
        return zoneAttempted / (self.attempted2PT + self.attemptedC3 + self.attemptedNC3)

    # calculates effective field goal percentage in given zone
    def calculateEFGP(self, madeShots, attemptedShots, madeThrees):
        return (madeShots + (0.5 * madeThrees)) / attemptedShots

    # calculates percetage of shots attempted in each zone and efg% in each zone
    def calculateEverything(self):
        self.zone2PT = self.calculateZone(self.attempted2PT)
        self.zoneC3 = self.calculateZone(self.attemptedC3)
        self.zoneNC3 = self.calculateZone(self.attemptedNC3)

        self.eFGp2PT = self.calculateEFGP(self.made2PT, self.attempted2PT, 0)
        self.eFGpC3 = self.calculateEFGP(self.madeC3, self.attemptedC3, self.madeC3)
        self.eFGpNC3 = self.calculateEFGP(self.madeNC3, self.attemptedNC3, self.madeNC3)

    # prints calculated percentages for each zone
    def printAnswers(self):
        print("Percentage of shots attempted in 2PT Zone: " + str(self.zone2PT))
        print("Percentage of shots attempted in NC3 Zone: " + str(self.zoneNC3))
        print("Percentage of shots attempted in C3 Zone: " + str(self.zoneC3))
        print("Effective FG Percentage in 2PT Zone: " + str(self.eFGp2PT))
        print("Effective FG Percentage in NC3 Zone: " + str(self.eFGpNC3))
        print("Effective FG Percentage in C3 Zone: " + str(self.eFGpC3))
