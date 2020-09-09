import json
import requests

class Pitcher:
    def __init__(self, player_id, name):
        response = requests.get("https://statsapi.mlb.com/api/v1/people/"+ str(player_id) +"/stats?stats=statsSingleSeason&gameType=R&group=pitching&season=2012")
        stats = response.json()["stats"][0]["splits"][-1]["stat"]

        self.name = name

        self.pa = (stats["strikeOuts"] + stats["airOuts"] + stats["hitByPitch"] +
                    stats["hits"] + stats["groundOuts"] + stats["baseOnBalls"]
                    - stats["intentionalWalks"])

        self.strikeout_avg = stats["strikeOuts"]/float(self.pa)
        self.flyout_avg = stats["airOuts"]/float(self.pa)
        self.groundout_avg = stats["groundOuts"]/float(self.pa)
        self.hbp_avg = stats["hitByPitch"]/float(self.pa)
        self.double_avg = stats["doubles"]/float(self.pa)
        self.triple_avg = stats["triples"]/float(self.pa)
        self.hr_avg = stats["homeRuns"]/float(self.pa)
        self.single_avg = (stats["hits"] - stats["doubles"] - stats["triples"]
                                - stats["homeRuns"])/float(self.pa)
        self.bb_avg = (stats["baseOnBalls"] -stats["intentionalWalks"])/float(self.pa)

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
