import csv
import random
from itertools import permutations

teams = []
def teamList():
    with open("data/test_teams.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["name", "rating"])
        for row in reader:
            teams.append(row["name"])
    x = list(permutations(teams, 2))
    return x

d

firstHalf = []
for i in range(len(perm)//2):
    x = random.choice(perm)
    if perm not in firstHalf:
        firstHalf.insert(i,x)
#print(len(firstHalf))

schedule = []
first = []
second = []
def drawSchedule(perm):
    """Function simulates schedule for the teams"""

    with open("data/test_schedule.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["tour", "homeTeam","awayTeam"])
        for i in range(len(first)):
            for game in first[i]:
                writer.writerow({"tour": i + 1, "homeTeam": game[0],"awayTeam": game[1] })
        for i in range(len(second)):
            for game in second[i]:
                writer.writerow({"tour": i + len(teams),"homeTeam": game[0],"awayTeam": game[1]})

def lastGameSwap():
    for tour in schedule:
        for element in schedule:
            x = tour[len(tour)- 1]
            y = element[:len(element)-1]
            #print(x)
            #print(y)

            if tuple(x) in y:
                tour[len(tour)-1] = x[::-1]

                #print(f"yep{x}")
                break
    return schedule
Discarded = []

def validation(pair):

    """Check if reverse pair already in schedule"""

    Add = True
    for element in schedule:
        if pair[::-1] in element:
            Add = False

    if Add == True:
        return True
    else:
        return False


def firstHalf():
    FHalf = []

    for tour in schedule:
        Add = True
        if len(FHalf) > 0:
            for game in tour:
                for element in FHalf:
                    if game[::-1] in element:
                        print(f"{game}Nana{element}")
                        print(" ")
                        Add = False

            if Add == True:
                FHalf.append(tour)
            elif Add ==False:
                Discarded.append(tour)

        else:
            FHalf.append(tour)

    return FHalf



schedule = lastGameSwap()


with open("data/test_schedule.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["tour", "homeTeam","awayTeam"])
    for i in range(len(first)):
        for game in first[i]:
            writer.writerow({"tour": i + 1, "homeTeam": game[0],"awayTeam": game[1] })
    for i in range(len(second)):
        for game in second[i]:
            writer.writerow({"tour": i + len(teams),"homeTeam": game[0],"awayTeam": game[1]})