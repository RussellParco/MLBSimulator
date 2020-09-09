class scorecard:
    def __init__(self, home, away):
        import numpy as np
        import pandas as pd
        homeLineup = pd.DataFrame(home["batters"])
        homePitchers = pd.DataFrame(home["pitcher"])
        awayLineup = pd.DataFrame(away["batters"])
        awayPitchers = pd.DataFrame(away["pitcher"])

        batterStats = dict.fromkeys(["ab", "h", "r", "rbi", "1", "2", "3",
            "4", "5", "6", "7", "9", "10"], 0)
        homeLineup.assign(**batterStats)
        awayLineup.assign(**batterStats)

        pitcherStats = dict.fromkeys(['w/l/s', 'ip', 'h', 'r', 'er', 'bb',
            'so', 'hb', 'bk', 'tbf'])
        homePitchers.assign(**pitcherStats)
        awayPitchers.assign(**pitcherStats)
        
