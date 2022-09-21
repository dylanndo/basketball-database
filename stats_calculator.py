class Stats_Calculator():
    # calculates percentage of shots attempted in zone
    def updateZone(player, zoneAttempted):
        return zoneAttempted / (player.attempted2PT + player.attemptedC3 + player.attemptedNC3)

    # calculates effective field goal percentage in given 2 pt zone
    def updateEFGP(madeShots, attemptedShots):
        return madeShots / attemptedShots

    # calculates effective field goal percentage in given 3 pt zone
    def update3EFGP(madeShots, attemptedShots):
        return (1.5 * madeShots) / attemptedShots
