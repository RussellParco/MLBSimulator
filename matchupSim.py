import batter as bat
import pitcher as pitch
import requests
import json

class matchupSim:
    def __init__(self, batter, pitcher, rounds):
        self.rounds = rounds
        #set avergae players
        response = requests.get("http://lookup-service-prod.mlb.com/json/named.team_hitting_season_leader_master.bam?season=2012&sort_order=%27desc%27&sort_column=%27avg%27&game_type=%27R%27&sport_code=%27mlb%27&recSP=1&recPP=50")
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
            bat.Batter.average_batter["bb_avg"] += int(te["bb"]) - int(te["ibb"])
            bat.Batter.league_pa += (int(te["so"]) + int(te["ao"])
                + int(te["go"]) + int(te["hbp"]) + int(te["h"]) + int(te["bb"]) - int(te["ibb"]))

        for stat in bat.Batter.average_batter:
            bat.Batter.average_batter[stat] /= float(bat.Batter.league_pa)
        #get list of active players
        response = requests.get("https://statsapi.mlb.com/api/v1/sports/1/players?season=2012")
        players = response.json()

        for player in players["people"]:
            if player["fullName"].lower() == batter.lower():
                player_id = player["id"]
                self.batter = bat.Batter(player_id, batter)
                break

        for player in players["people"]:
            if player["fullName"].lower() == pitcher.lower():
                player_id = player["id"]
                self.pitcher = pitch.Pitcher(player_id, pitcher)
                break

        self.batter.updateProbs(self.pitcher)

    def play(self, loops):
        totals = {
            "so": 0,
            "fo": 0,
            "go": 0,
            "bb": 0,
            "s": 0,
            "d": 0,
            "t": 0,
            "hr": 0
        }
        for x in range(loops):
            for x in range(self.rounds):
                outcome = self.batter.atBat()
                if outcome == 0 :
                    totals["bb"] += 1
                elif outcome == 1:
                    totals["s"] += 1
                elif outcome == 2 :
                    totals["d"] += 1
                elif outcome == 3 :
                    totals["t"] += 1
                elif outcome == 4 :
                    totals["hr"] += 1
                elif outcome == -1 :
                    totals["fo"] += 1
                elif outcome == -2 :
                    totals["go"] += 1
                else:
                    totals["so"] += 1

        for x in totals:
            totals[x] /= float(loops)
