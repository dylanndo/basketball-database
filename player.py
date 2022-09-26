from stats_calculator import Stats_Calculator

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
        self.attempted3PT = 0
        self.attempted = 0

        # count of made shots
        self.made2PT = 0
        self.madeC3 = 0
        self.madeNC3 = 0
        self.made3PT = 0
        self.made = 0

        # percentage of shots taken
        self.zone2PT = 0.0
        self.zone3PT = 0.0    #C3 + NC3
        self.zoneC3 = 0.0
        self.zoneNC3 = 0.0

        # field goal percentage
        self.fgp2PT = 0.0
        self.fgp3PT = 0.0
        self.fgpC3 = 0.0
        self.fgpNC3 = 0.0
        self.fgp = 0.0

        # effective field goal percentage
        self.eFGp2PT = 0.0
        self.eFGp3PT = 0.0    #C3 + NC3
        self.eFGpC3 = 0.0
        self.eFGpNC3 = 0.0
        self.eFGp = 0.0


    # extracts data from given row in CSV File
    def addShot(self, row):
        if(abs(float(row[2])) <= 7.8):  # if shot was taken within 7.8 ft from the x-axis (x <= 7.8)
            if(abs(float(row[1])) < 22):   # inside 22ft from the corner = two pt
                self.attempted2PT += 1  # +1 to 2pt attempt
                self.attempted += 1 # +1 to total attempt
                
                if(int(row[3]) == 1):   # +1 to 2pt made and shot made
                    self.made2PT += 1
                    self.made += 1    
                
                self.updateZones() # update zones after new shot attempt
                self.eFGp2PT = Stats_Calculator.updateEFGP(self.made2PT, self.attempted2PT)   # update 2PT EFG%
                self.eFGp = Stats_Calculator.updateEFGP(self.made, self.made3PT, self.attempted)    # update overall EFG%
                self.fgp2PT = self.eFGp2PT  # update 2PT FG%
                self.fgp = Stats_Calculator.updateFGP(self.made, self.attempted)   # update  overall FG%
                
                self.two.append(row)    # add data to two pointers list 

            else:   # 22ft and beyond from the corner = corner three
                self.attemptedC3 += 1  # +1 to corner 3 attempt
                self.attempted3PT += 1  # +1 to 3 attempt
                self.attempted += 1 # +1 to total attempt

                if(int(row[3]) == 1):   # +1 to corner 3, 3 made, shot made
                    self.madeC3 += 1   
                    self.made3PT += 1 
                    self.made += 1

                self.updateZones() # update zones after new shot attempt
                self.eFGpC3 = Stats_Calculator.update3EFGP(self.madeC3, self.attemptedC3)   # update C3 EFG%
                self.eFGp = Stats_Calculator.updateEFGP(self.made, self.made3PT, self.attempted)    # update overall EFG%
                self.fgpC3 = Stats_Calculator.updateFGP(self.madeC3, self.attemptedC3)   # update C3 FG%
                self.fgp3PT = Stats_Calculator.updateFGP(self.made3PT, self.attempted3PT)   # update 3PT FG%
                self.fgp = Stats_Calculator.updateFGP(self.made, self.attempted)   # update  overall FG%
                
                self.cornerThree.append(row)    # add data to corner 3 list 
            
        else:   # if shot was taken beyond 7.8 ft from the x-axis (x > 7.8 ft)
            if(float(row[1])**2 + float(row[2])**2 < 564.0625):   #pyt. theorem - inside 23.75ft from the arc = two pt
                self.attempted2PT += 1  # +1 to 2pt attempt
                self.attempted += 1 # +1 to total attempt

                if(int(row[3]) == 1):   # +1 to 2pt made and shot made
                    self.made2PT += 1
                    self.made += 1
                
                self.updateZones() # update zones after new shot attempt
                self.eFGp2PT = Stats_Calculator.updateEFGP(self.made2PT, self.attempted2PT)   # update 2PT EFG%
                self.eFGp = Stats_Calculator.updateEFGP(self.made, self.made3PT, self.attempted)    # update overall EFG%
                self.fgp2PT = self.eFGp2PT  # update 2PT FG%
                self.fgp = Stats_Calculator.updateFGP(self.made, self.attempted)   # update  overall FG%
                
                self.two.append(row)    # add data to two pointers list 

            else:   # 23.75ft and beyond from the arc = non corner three
                self.attemptedNC3 += 1  # +1 to non corner 3 attempt
                self.attempted3PT += 1  # +! to 3 attempt
                self.attempted += 1 # +1 to total attempt

                if(int(row[3]) == 1):   # +1 to non corner 3 made, 3 made, and shot made
                    self.madeNC3 += 1
                    self.made3PT += 1 
                    self.made += 1    
                
                self.updateZones() # update zones after new shot attempt
                self.eFGpNC3 = Stats_Calculator.update3EFGP(self.madeNC3, self.attemptedNC3)   # update NC3 EFG%
                self.eFGp = Stats_Calculator.updateEFGP(self.made, self.made3PT, self.attempted)    # update overall EFG%
                self.fgpNC3 = Stats_Calculator.updateFGP(self.madeNC3, self.attemptedNC3)   # update NC3 FG%
                self.fgp3PT = Stats_Calculator.updateFGP(self.made3PT, self.attempted3PT)   # update 3PT FG%
                self.fgp = Stats_Calculator.updateFGP(self.made, self.attempted)   # update  overall FG%

                self.nonCornerThree.append(row)    # add data to non corner 3 list
    
    # updates zones after new shot attempt
    def updateZones(self):
        self.zone2PT = Stats_Calculator.updateZone(self.attempted2PT, self.attempted) # update 2PT zone
        self.zoneC3 = Stats_Calculator.updateZone(self.attemptedC3, self.attempted) # update C3 zone
        self.zoneNC3 = Stats_Calculator.updateZone(self.attemptedNC3, self.attempted) # update NC3 zone
        self.zone3PT = self.zoneC3 + self.zoneNC3

    # getter methods
    def getFGp2PT(self):
        return self.fgp2PT

    def getFGp3PT(self):
        return self.fgp3PT

    def getFGpC3(self):
        return self.fgpC3

    def getFGpNC3(self):
        return self.fgpNC3

    def getFGp(self):
        return self.fgpNC3
    
    def getZone2PT(self):
        return self.zone2PT
    
    def getZone3PT(self):
        return self.zone3PT

    def getZoneC3(self):
        return self.zoneC3

    def getZoneNC3(self):
        return self.zoneNC3

    def getEFGp2PT(self):
        return self.eFGp2PT

    def getEFGp3PT(self):
        return self.eFGp3PT

    def getEFGpC3(self):
        return self.eFGpC3

    def getEFGpNC3(self):
        return self.eFGpNC3

    def getEFGp(self):
        return self.eFGp
