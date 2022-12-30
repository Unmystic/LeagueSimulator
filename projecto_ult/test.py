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
    #Draw one round of tournament:
    tour = []
    mylist = tm.copy()
    #random.seed()
    while len(tour) < (len(teams) // 2) :
               
        random.seed()
        random.shuffle(mylist)     
        for element in  mylist:
            if element["drawable"]:
                for team in element["opposition"]:
                    if not any(team in sl for sl in tour):
                        tour.append([element["teamName"], team])
                        element["drawable"] = False
                        element["opposition"] = [ x for x in element["opposition"] if x != team]
                        
                        pprint(len(element["opposition"]))
                        idx = [i for i in range(len(mylist)) if mylist[i]["teamName"] == team][0]
                        mylist[idx]["drawable"] = False
                        mylist[idx]["opposition"] = [ x for x in mylist[idx]["opposition"] if x != element["teamName"]]
                        
                        pprint(len(tm[idx]["opposition"]))
                        break
    for elm in  mylist:
        elm["drawable"] = True
    tm = mylist     
                   
    pprint(tour)
    return tour, tm
           

def drawSchedule(tm):
    """Function simulates schedule for the teams"""
    schedule = []
    for _ in range(len(teams)- 1):
        tour, tm = drawTour(tm)
        schedule.append(tour)
    pprint(schedule)




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
    #pprint(tm)
    #tour, tm = drawTour(tm)
    #pprint(tour)
    #pprint(tm)
    drawSchedule(tm)
"""     for pos in tm:
        pprint([pos["teamName"], pos["opposition"]]) """