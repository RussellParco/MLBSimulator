import json
import requests
class Batter:
    def __init__(self, player_id):

        response = requests.get("https://statsapi.mlb.com/api/v1/people/"+ str(player_id) +"/stats?stats=statsSingleSeason&gameType=R&group=hitting&season=2019")
        stats = response.json()["stats"][0]["splits"][0]["stat"]
        self.pa = stats["plateAppearances"]
        self.strikeout_avg = stats["strikeOuts"]/float(self.pa)
        self.flyout_avg = stats["airOuts"]/float(self.pa)
        self.groundout_avg = stats["groundOuts"]/float(self.pa)
        self.hbp_avg = stats["hitByPitch"]/float(self.pa)
        self.double_avg = stats["doubles"]/float(self.pa)
        self.triple_avg = stats["triples"]/float(self.pa)
        self.hr_avg = stats["homeRuns"]/float(self.pa)
        self.single_avg = (1 - self.double_avg - self.triple_avg
                                - self.hr_avg)
        self.bb_avg = (stats["baseOnBalls"] + stats["intentionalWalks"])/float(self.pa)

    def __str__(self):
            return (str(self.pa) + "\n" +
            str(self.strikeout_avg)  + "\n" +
            str(self.flyout_avg)+ "\n" +
            str(self.groundout_avg) + "\n" +
            str(self.hbp_avg) + "\n" +
            str(self.double_avg) + "\n" +
            str(self.triple_avg) + "\n" +
            str(self.hr_avg) + "\n" +
            str(self.single_avg) + "\n")

    def updateProbs(self, pitcher):
        probs = []
        probs.append(self.hbp_avg)
        probs.append(probs[-1] + self.single_avg)
        probs.append(probs[-1] + self.triple_avg)
        probs.append(probs[-1] + self.double_avg)
        probs.append(probs[-1] + self.hr_avg)
        probs.append(probs[-1] + self.flyout_avg)
        probs.append(probs[-1] + self.groundout_avg)
        probs.append(probs[-1] + self.strikeOut_avg)
