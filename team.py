import batter as bat
import pitcher as pitch


class Team:
    def __init__(self, batters, pitchers, players):
        self.batters = []
        self.pitchers = []
        self.batPos = 0
        self.opponent = None

        for name in batters:
            #find player id
            for player in players["people"]:
                if player["fullName"].lower() == name.lower():
                    player_id = player["id"]

                    #add player to hteam
                    player = bat.Batter(player_id, name)
                    self.batters.append(player)
                    break

        for name in pitchers:
            for player in players["people"]:
                if player["fullName"].lower() == name.lower():
                    player_id = player["id"]
                    #add player to team
                    player = pitch.Pitcher(player_id, name)
                    self.pitchers.append(player)
                    print(name)
                    break

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
