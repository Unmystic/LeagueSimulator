import csv
import random
from itertools import chain
from pprint import pprint

teams = []
def teamList():
    with open("data/test_teams.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["name", "rating"])
        for row in reader:
            teams.append(row["name"])
    
    return teams

def first_draw(comb):
    n = int(len(teams) / 2)

    stages = []
    for i in range(len(teams) - 1):
        t = teams[:1] + teams[-i:] + teams[1:-i] if i else teams
        stages.append(list(zip(t[:n], reversed(t[n:]))))

    #print(len(stages))
    #pprint(stages)
    stages = tuple_conv(stages)
    #pprint(stages)
    for tour in stages:
        for game in tour:
            random.seed()
            x = random.choice([0,1])
            if x:
                game[0],game[1] = game[1],game[0]
            #print(game)
    #pprint(stages)
    return stages
    
def tuple_conv(stages):
    cel = []
    for tour in stages:
        tour = [list(elem) for elem in tour]
        cel.append(tour)
  
    return cel


def second_draw(first):
    second = first.copy()
    for tour in second:
        for match in tour:
            match[0],match[1] = match[1],match[0]
    random.shuffle(second)
    return second

def drawSchedule(comb):
    first = first_draw(comb)
    second = second_draw(first)

    with open("data/test_schedule.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["tour", "homeTeam","awayTeam"])
        for i in range(len(first)):
            for game in first[i]:
                writer.writerow({"tour": i + 1, "homeTeam": game[0],"awayTeam": game[1] })
        for i in range(len(second)):
            for game in second[i]:
                writer.writerow({"tour": i + len(teams),"homeTeam": game[0],"awayTeam": game[1]}) 

if __name__ == "__main__":
    
    #pprint(tm)
    #idx = [i for i in range(len(tm)) if tm[i]["teamName"] == "Flawless Tigers"][0]
    #print(idx)
    comb = teamList()
    #pprint(comb)
    #first = first_draw(comb)
    drawSchedule(comb)
    #pprint(first)