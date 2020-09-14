import json
import requests
import game as g
class Menu:
    def __init__(self):
        print("***Welcome to MLB Simulator***")
        self.team1 = []
        self.team2 = []

    def pickPlayer(self):
        while True:
            player = input()
            response = requests.get("http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&name_part='"+ player +"%'")
            data = response.json()["search_player_all"]["queryResults"]
            length = int(data["totalSize"])
            if length == 0 :
                print("Found no players please try again")
            elif length == 1 :
                print("You choose " + data["row"]["name_display_first_last"])
                player_id = data["row"]["player_id"]
                break
            else:
                print("Found " + data["totalSize"] + ": The first "+ str(min(5, length)) +" are")
                for x in range(0, min(5, length)):
                    print(str(x + 1) + ": " + data["row"][x]["name_display_first_last"] + ", Born " + data["row"][x]["birth_date"])
                i = input("To pick one of first five enter 1-5 or press enter to continue: ")
                if i.isdigit() and int(i) >= 1 and int(i) <= min(5, length) :
                    player_id = data["row"][int(i) - 1]["player_id"]
                    break
                print("Pick a player")
        while True:
            year = input("Pick a year for player stats: ")
            response = requests.get("https://statsapi.mlb.com/api/v1/people/"+player_id +"/stats?stats=statsSingleSeason&gameType=R&season="+ year)
            length = len(response.json()["stats"])
            if(length == 0):
                print("Player did not play in " + year)
            else:
                break
        return {"player_id": player_id, "name" : player,"year": year}
    def startup(self):
        print("Press Enter to Pick Home Team:")
        input()
        for i in range(0,9) :
            print("Pick Next Batter")
            self.team1.append(self.pickPlayer())
        print("Pick Home Team Pitcher")
        pitcher1 = self.pickPlayer()
        print("Press Enter to Pick Away Team:")
        input()
        for i in range(0,9) :
            print("Pick Next Batter")
            self.team2.append(self.pickPlayer())
        print("Pick Away Team Pither")
        pitcher2 = self.pickPlayer()
        game = g.Game(self.team1, self.team2, [pitcher1], [pitcher2])
        print("Press Enter to Play:")
        input()
        response = 'r'
        game.play()
        while true:
            print("[r] to replay game")
            print("[p] to start new game")
            print("[q] to quit simulator")
            response = input()
            if response == "r":
                game.replay()
            elif response == "p" or response == "q"
                break
        if response == 'p':
            self.startup()
