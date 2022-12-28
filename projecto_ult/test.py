import csv
import random
from itertools import permutations
from pprint import pprint

teams = []
def teamList():
    with open("data/test_teams.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["name", "rating"])
        for row in reader:
            teams.append(row["name"])
    teamList = []
    for team in teams:
        teamList.append({"teamName": team, "opposition": [x for x in teams if x != team], "drawable": True})
    return teamList

def drawTour(tm):
    #Draw 1 round of tournament:
    tour = []
    random.shuffle(tm)
    for element in  tm:
        if element["drawable"]:
            for team in element["opposition"]:
                if not any(team in sl for sl in tour):
                    tour.append([element["teamName"], team])
                    element["drawable"] = False
                    element["opposition"] = [ x for x in element["opposition"] if x != team]
                    idx = [i for i in range(len(tm)) if tm[i]["teamName"] == team][0]
                    tm[idx]["drawable"] = False
                    tm[idx]["opposition"] = [ x for x in tm[idx]["opposition"] if x != element["teamName"]]
                    break
    return tour, tm
        
    

def drawSchedule(tm):
    """Function simulates schedule for the teams"""
    pass




""" with open("data/test_schedule.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["tour", "homeTeam","awayTeam"])
    for i in range(len(first)):
        for game in first[i]:
            writer.writerow({"tour": i + 1, "homeTeam": game[0],"awayTeam": game[1] })
    for i in range(len(second)):
        for game in second[i]:
            writer.writerow({"tour": i + len(teams),"homeTeam": game[0],"awayTeam": game[1]}) """

if __name__ == "__main__":
    tm = teamList()
    # pprint(tm)
    tour, tm = drawTour(tm)
    pprint(tour)
    