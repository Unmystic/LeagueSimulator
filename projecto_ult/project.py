import random
import statistics
import csv
from itertools import permutations
from tabulate import tabulate
from test_teams import createTeams
import test_schedule
from test_match import matchEngine


def main():
    createTeams()

    perm = test_schedule.teamList()
    test_schedule.drawSchedule(perm)
    table = matchEngine()
    #for position in table:
        #print(position)
    writeTable(table)
    drawTable()



def writeTable(table):
    with open("data/table.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["position","name", "rating", "gamesPlayed", "goalsScored", "goalsConceded", "points"])
        writer.writeheader()
        for i in range(len(table)):
            writer.writerow({'position': i+1, 'name': table[i]['name'], 'rating': table[i]['rating'], 'gamesPlayed': table[i]['gamesPlayed'],'goalsScored': table[i]['goalsScored'], 'goalsConceded': table[i]['goalsConceded'],'points': table[i]['points']})


def drawTable():

    with open("data/table.csv", "r") as file:
        reader = csv.DictReader(file)
    #for row in reader:
        print(tabulate(reader, headers="keys", tablefmt="grid", stralign='center'))





if __name__ == "__main__":
    main()
