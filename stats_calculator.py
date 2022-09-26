class Stats_Calculator():
    # calculates percentage of shots attempted in zone
    def updateZone(zoneAttempted, totalAttempted):
        return float(zoneAttempted) / totalAttempted

    # calculates effective field goal percentage in given 2 pt zone
    def update2EFGP(madeShots, attemptedShots):
        return float(madeShots) / attemptedShots

    # calculates effective field goal percentage in given 3 pt zone
    def update3EFGP(madeShots, attemptedShots):
        return (1.5 * madeShots) / attemptedShots
    
    # calculates total effective field goal percentage
    def updateEFGP(madeShots, made3PT, attemptedShots):
        return (madeShots + 1.5 * made3PT) / attemptedShots

    # calculates field goal percentage
    def updateFGP(madeShots, attemptedShots):
        return madeShots / attemptedShots