"""
This is the main file!

Use it to simulate finich results.
"""

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

    comb = test_schedule.teamList()
    test_schedule.drawSchedule(comb)
    table = matchEngine()
    #for position in table:
        #print(position)
    writeTable(table)
    drawTable()



def writeTable(table):

    #Writing results of simulation in csv-file
    with open("data/table.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["position","name", "rating", "gamesPlayed", "goalsScored", "goalsConceded", "points"])
        writer.writeheader()
        for i in range(len(table)):
            writer.writerow({'position': i+1, 'name': table[i]['name'], 'rating': table[i]['rating'], 'gamesPlayed': table[i]['gamesPlayed'],'goalsScored': table[i]['goalsScored'], 'goalsConceded': table[i]['goalsConceded'],'points': table[i]['points']})


def drawTable():
    #Portraying genetated result in tabled form
    with open("data/table.csv", "r") as file:
        reader = csv.DictReader(file)
    #for row in reader:
        print(tabulate(reader, headers="keys", tablefmt="grid", stralign='center'))





if __name__ == "__main__":
    main()
