import batter as bat
import pitcher as pitch


class Team:
    def __init__(self, batters, pitchers):
        self.batters = []
        self.pitchers = []
        self.batPos = 0
        self.opponent = None

        for b in batters:
            #add player to team
            player = bat.Batter(b["player_id"], b["name"], b["year"])
            self.batters.append(player)

        for p in pitchers:
            #add player to team
            player = pitch.Pitcher(p["player_id"], p["name"], b["year"])
            self.pitchers.append(player)

        self.curr_pitcher = self.pitchers[0]
    def atBat(self):
        outcome = self.batters[self.batPos].atBat()
        self.batPos += 1
        if self.batPos == 9 :
            self.batPos = 0
        return outcome

    def setPitcher(self, pitcher):
        self.curr_pitcher = pitcher
        self.opponent.newOpposingPitcher(pitcher)

    def newOpposingPitcher(self, pitcher):
        for batter in self.batters:
            batter.updateProbs(pitcher)

    def setOpponent(self, opp):
        self.opponent = opp
        opp.newOpposingPitcher(opp.curr_pitcher)

    def replay(self):
        self.batPos = 0
