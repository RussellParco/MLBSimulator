import json
import requests
import random

class Batter:
    average_batter = {
        "strikeout_avg" : 0,
        "flyout_avg" : 0,
        "groundout_avg" : 0,
        "hbp_avg" : 0,
        "double_avg" : 0,
        "triple_avg" : 0,
        "hr_avg" : 0,
        "single_avg" : 0,
        "bb_avg" : 0
    }
    league_pa = 0
    def __init__(self, player_id, name):

        response = requests.get("https://statsapi.mlb.com/api/v1/people/"+ str(player_id) +"/stats?stats=statsSingleSeason&gameType=R&group=hitting&season=2012")
        stats = response.json()["stats"][0]["splits"][-1]["stat"]

        self.name = name

        self.pa = (stats["strikeOuts"] + stats["airOuts"] + stats["hitByPitch"] +
                    stats["hits"] + stats["groundOuts"] + stats["baseOnBalls"])
                    #- stats["intentionalWalks"] )

        self.strikeout_avg = stats["strikeOuts"]/float(self.pa)
        self.flyout_avg = stats["airOuts"]/float(self.pa)
        self.groundout_avg = stats["groundOuts"]/float(self.pa)
        print(stats["hitByPitch"])
        self.hbp_avg = stats["hitByPitch"]/float(self.pa)
        self.double_avg = stats["doubles"]/float(self.pa)
        self.triple_avg = stats["triples"]/float(self.pa)
        self.hr_avg = stats["homeRuns"]/float(self.pa)
        self.single_avg = (stats["hits"] - stats["doubles"] - stats["triples"]
                                - stats["homeRuns"])/float(self.pa)
        self.bb_avg = (stats["baseOnBalls"])/float(self.pa)
        self.probs = [0,0,0,0,0,0,0,0]

    def __str__(self):
            return (str(self.name) + "\n" +
            "pa: " + str(self.pa) + "\n" +
            "so: " + str(self.strikeout_avg)  + "\n" +
            "ao: " + str(self.flyout_avg)+ "\n" +
            "go: " + str(self.groundout_avg) + "\n" +
            "hbp: " + str(self.hbp_avg) + "\n" +
            "d: " + str(self.double_avg) + "\n" +
            "t: " + str(self.triple_avg) + "\n" +
            "hr: " + str(self.hr_avg) + "\n" +
            "s: " + str(self.single_avg) + "\n"
            "bb: " + str(self.bb_avg) + "\n")

    def updateProbs(self, pitcher):

        sum = (self.strikeout_avg * pitcher.strikeout_avg / Batter.average_batter["strikeout_avg"] +
                self.flyout_avg * pitcher.flyout_avg / Batter.average_batter["flyout_avg"] +
                self.groundout_avg * pitcher.groundout_avg / + Batter.average_batter["groundout_avg"] +
                self.hbp_avg * pitcher.hbp_avg / Batter.average_batter["hbp_avg"] +
                self.double_avg * pitcher.double_avg / Batter.average_batter["double_avg"] +
                self.triple_avg * pitcher.triple_avg / Batter.average_batter["triple_avg"] +
                self.hr_avg * pitcher.hr_avg / Batter.average_batter["hr_avg"] +
                self.single_avg * pitcher.single_avg / Batter.average_batter["single_avg"] +
                self.bb_avg * pitcher.bb_avg / Batter.average_batter["bb_avg"])
        print(sum)
        self.probs[0] = (((self.hbp_avg * pitcher.hbp_avg) /
                            Batter.average_batter["hbp_avg"]/sum)
                            + ((self.bb_avg * pitcher.bb_avg /
                            Batter.average_batter["bb_avg"])/ sum))
        self.probs[1] = self.probs[0] + ((self.single_avg * pitcher.single_avg) /
                            Batter.average_batter["single_avg"]) / sum
        self.probs[2] = self.probs[1] + ((self.double_avg * pitcher.double_avg) /
                            Batter.average_batter["double_avg"]) / sum
        self.probs[3] = self.probs[2] + ((self.triple_avg * pitcher.triple_avg) /
                            Batter.average_batter["triple_avg"]) / sum
        self.probs[4] = self.probs[3] + ((self.hr_avg * pitcher.hr_avg) /
                            Batter.average_batter["hr_avg"]) / sum
        self.probs[5] = self.probs[4] + ((self.flyout_avg * pitcher.flyout_avg) /
                            Batter.average_batter["flyout_avg"]) / sum
        self.probs[6] = self.probs[5] + ((self.groundout_avg * pitcher.groundout_avg) /
                            Batter.average_batter["groundout_avg"]) / sum
        self.probs[7] = self.probs[6] + ((self.strikeout_avg * pitcher.strikeout_avg) /
                            Batter.average_batter["strikeout_avg"]) / sum
        print(self.probs)
    def atBat(self):
        print(self.name),
        num = random.random()
        outcome = 0

        if num <=self.probs[0] :
            outcome = 0
            print(": walk")
        elif num <=self.probs[1] :
            outcome = 1
            print(": single")
        elif num <=self.probs[2] :
            outcome = 2
            print(": double")
        elif num <=self.probs[3] :
            outcome = 3
            print(": triple")
        elif num <=self.probs[4] :
            outcome = 4
            print(": homerun")
        elif num <=self.probs[5] :
            outcome = -1
            print(": flyout")
        elif num <=self.probs[6] :
            outcome = -2
            print(": groundout")
        else:
            outcome = -3
            print(": strikeout")
        return outcome
