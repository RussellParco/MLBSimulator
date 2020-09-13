import requests
import json

response = requests.get("https://statsapi.mlb.com/api/v1/stats?stats=season&sportIds=1&season=2012&group=hitting&limit=144&fields=stats,type,displayName,group, totalSplits,splits,season,stat,homeRuns & sortState=homeRuns")
data = response.json()
print(data)
homeruns = 0
for player in data["stats"][0]["splits"]:
    homeruns += player["stat"]["homeRuns"]
response = requests.get("https://statsapi.mlb.com/api/v1/stats?stats=season&sportIds=1&season=2012&group=pitching&limit=124&fields=stats,type,displayName,group, totalSplits,splits,season,stat,homeRuns & sortState=homeRuns")
data = response.json()
for player in data["stats"][0]["splits"]:
    homeruns += player["stat"]["homeRuns"]
print(homeruns)
