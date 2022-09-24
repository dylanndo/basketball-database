class Stats_Calculator():
    # calculates percentage of shots attempted in zone
    def updateZone(zoneAttempted, totalAttempted):
        return float(zoneAttempted) / totalAttempted

    # calculates effective field goal percentage in given 2 pt zone
    def updateEFGP(madeShots, attemptedShots):
        return float(madeShots) / attemptedShots

    # calculates effective field goal percentage in given 3 pt zone
    def update3EFGP(madeShots, attemptedShots):
        return (1.5 * madeShots) / attemptedShots
