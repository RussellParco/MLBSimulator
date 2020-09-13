import json
import requests
import team
import batter as bat
import baseDisplay

class Game:
    def __init__(self, team1, team2, pitchers1, pitchers2):
        self.inning = 1
        self.homeScore = 0
        self.awayScore = 0
        self.outs = 0
        self.bases = [0,0,0]
        self.display = baseDisplay.baseDisplay()

        #set avergae players
        response = requests.get("http://lookup-service-prod.mlb.com/json/named.team_hitting_season_leader_master.bam?season=2019&sort_order=%27desc%27&sort_column=%27avg%27&game_type=%27R%27&sport_code=%27mlb%27&recSP=1&recPP=50")
        data = response.json()["team_hitting_season_leader_master"]["queryResults"]["row"]
        for te in data:
                bat.Batter.average_batter["strikeout_avg"] += int(te["so"])
                bat.Batter.average_batter["flyout_avg"] += int(te["ao"])
                bat.Batter.average_batter["groundout_avg"] += int(te["go"])
                bat.Batter.average_batter["hbp_avg"] += int(te["hbp"])
                bat.Batter.average_batter["double_avg"] += int(te["d"])
                bat.Batter.average_batter["triple_avg"] += int(te["t"])
                bat.Batter.average_batter["hr_avg"] += int(te["hr"])
                bat.Batter.average_batter["single_avg"] += (int(te["h"]) - int(te["d"])
                    - int(te["t"]) - int(te["hr"]))
                bat.Batter.average_batter["bb_avg"] += int(te["bb"])
                bat.Batter.league_pa += (int(te["so"]) + int(te["ao"])
                    + int(te["go"]) + int(te["hbp"]) + int(te["h"]) + int(te["bb"]))

        for stat in bat.Batter.average_batter:
            bat.Batter.average_batter[stat] /= float(bat.Batter.league_pa)

        self.home = team.Team(team1, pitchers1)
        self.away = team.Team(team2, pitchers2)

        self.home.setOpponent(self.away)
        self.away.setOpponent(self.home)


    def play(self):
        print("PLAYBALL")
        while self.inning <= 9 or self.homeScore == self.awayScore:
            self.playInning()
            self.inning += 1
        print("Home: %d" %(self.homeScore))
        print("Away: %d" %(self.awayScore))

    def playInning(self):
        print("INNING: %d" %(self.inning))
        self.display.update(self.bases)
        while self.outs < 3:
            result = self.away.atBat()
            self.awayScore += self.moveRunners(result)
            if result < 0:
                self.outs += 1
        self.outs = 0
        self.bases =[0,0,0]
        if not(self.inning == 9 and self.homeScore > self.awayScore):
            print("BOTTOM HALF")
            self.display.update(self.bases)
            while self.outs < 3:
                result = self.home.atBat()
                if result < 0:
                    self.outs += 1
                self.homeScore += self.moveRunners(result)
            self.outs = 0
            self.bases =[0,0,0]
            print("Home: %d" %(self.homeScore))
            print("Away: %d" %(self.awayScore))

    def moveRunners(self, result):
        runs = 0
        if result == 0:
            if self.bases[0]:
                if self.bases[1]:
                    if self.bases[2]:
                        runs = 1
                    self.bases[2] = 1
                self.bases[1] = 1
            self.bases[0] = 1
            self.display.update(self.bases)
        elif result == 1:
            runs = self.bases[1] + self.bases[2]
            self.bases[1] = self.bases[2] = 0

            if self.bases[0]:
                self.bases[1] = 1
            self.bases[0] = 1
            self.display.update(self.bases)

        elif result == 2:
            runs = self.bases[2] + self.bases[1]
            self.bases[2] = 0
            self.bases[1] = 1
            if self.bases[0] :
                self.bases[2] = 1
                self.bases[0] = 0
            self.display.update(self.bases)

        elif result == 3:
            runs = self.bases[2] + self.bases[1] + self.bases[0]
            self.bases[0] = self.bases[1] = 0
            self.bases[2] = 1
            self.display.update(self.bases)

        elif result == 4:
             runs = self.bases[2] + self.bases[1] + self.bases[0] + 1
             self.bases[0] = self.bases[1] = self.bases[2] = 0
             self.display.update(self.bases)

        return runs
