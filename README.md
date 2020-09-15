# MLBSimulator
## Description 
This python project is built to simulate MLB baseball games. We first create two customised teams composed of 9 hitters and a pitcher to compete against one another.
Using the MLB Stats API we can choose to use up-to-date current season stats or previous seasons stats. 
This allows us to build teams made from current stars like MIke Trout to basbeall legends like Babe Ruth. 
We then find the average statistics for MLB players, using the average stats and the individual stats of a hitter, pitcher pair we are able to find an effective estimate of the 
probabilities of all the outcomes for the matchup between the hitter and pitcher. From this we can use simple base running rules and how to score runs to simulate the rest of the game.


## Background
This project takes inspiration from the vast sabermetrics community, [r\Sabermetrics](https://www.reddit.com/r/Sabermetrics/), and their work to better 
explain the sport that so many love, including myself.  Further research was done to find an effective way to simulate a hitter, pitcher matchup. Some of the following papers provided
insight on both simulating the matchups and base runners.   
https://tht.fangraphs.com/10-lessons-i-learned-from-creating-a-baseball-simulator/   
https://cdn.shopify.com/s/files/1/1633/3369/files/VersionFinale.pdf

## How To Run
Download the files and install required libraries
```
pip install json
pip install requests 
pip install random
```
Finally to run,
```
python main.py
```
