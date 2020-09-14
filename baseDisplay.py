class baseDisplay:
    def __init__(self, team1, team2):
        self.bases=['O','O','O']
        self.stats = [{},{}]
        for player in team1:
            self.stats[0][player["name"]] = {
                'H' : 0,
                "BB" : 0,
                "2B" : 0,
                "3B" : 0,
                "HR" : 0,
                "SO" : 0,
                "PA" : 0
            }
        for player in team2:
            self.stats[1][player["name"]] = {
                'H' : 0,
                "BB" : 0,
                "2B" : 0,
                "3B" : 0,
                "HR" : 0,
                "SO" : 0,
                "PA" : 0
            }

    def updateBases(self, newBases):
        for x in range(3):
            self.bases[x] = 'x' if newBases[x] else 'O'
        self.render()

    def updateStats(self, half, batter, outcome):
        self.stats[half][batter][outcome] += 1
        if outcome in ["2B", "3B", "HR"] :
            self.stats[half][batter]["H"] += 1
            self.stats[half][batter]["PA"] += 1
        elif outcome == "SO":
            self.stats[half][batter]["PA"] += 1
    def render(self):
        print("     " + self.bases[1])
        print("    / \\")
        print("   /   \\")
        print("  /     \\")
        print(" /       \\")
        print(self.bases[2] + "         " + self.bases[0])
        print(" \\       /")
        print("  \\     /")
        print("   \   /")
        print("    \\ /")
        print("     O")

    def renderStats(self):
        print("Home Stats:")
        print("Player\t\t\tH\tBB\t2B\t3B\tHR\tSO\tPA")

        for player in self.stats[0].keys() :
            print(player, end="\t\t")
            for stat in self.stats[0][player].keys():
                print(self.stats[0][player][stat], end="\t")
            print()
        print("\nAway Stats:")
        print("Player\t\t\tH\tBB\t2B\t3B\tHR\tSO\tPA")

        for player in self.stats[1].keys() :
            print(player, end="\t\t")
            for stat in self.stats[1][player].keys():
                print(self.stats[1][player][stat], end="\t")
            print()

    def finalStats(self, score):
        print("Home: %d" %(score[0]))
        print("Away: %d" %(score[1]))
        self.renderStats()

    def replay(self):
        self.bases=['O','O','O']
        for player in self.stats[0].keys() :
            for stat in self.stats[0][player].keys():
                self.stats[0][player][stat] = 0
        for player in self.stats[1].keys() :
            for stat in self.stats[1][player].keys():
                self.stats[1][player][stat] = 0
