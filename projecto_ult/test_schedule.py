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

def Pair():
    pairs = []
    for i in range(len(teams)):
        for j in range(len(teams)):
            if teams[i] != teams[j]:
                pairs.append({"team1": teams[i], "team2":teams[j]})
    return pairs


perm = list(permutations(teams, 2))
y = set(perm)
t = Pair()

#print(len(t))
#print(len(list(perm)))

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
    for i  in range((len(teams) - 1) * 2):
        tour = []
        count = 0
        elig = True
        while len(tour) < (len(teams)//2) - 1:
            zy = random.randint(1,1000)
            random.seed(count)
            x = random.choice(perm)
            #print(tour)
            #print(len(schedule))

            if len(tour) > 0:
                valid = True
                elig = True
                for element in tour:
                    if valid == False:
                        continue
                    if x[0] in element or x[1] in element:
                        valid = False
                        count = count + 1

                if valid == True:
                    #count = count + 1
                    """Checking for eligibility to include in first half"""
                    tour.append(x)
                    perm.remove(x)

                    if validation(x):
                        #print("Oka")
                        continue
                    else:
                        elig = False
                        #print("error2")
                    #print(len(perm))
                #elif valid == False:
                    #print("error1")
                    #print(len(tour))
                    #print(len(perm))
            else:
                tour.append(x)
                perm.remove(x)
                #print(len(perm))
        game = []
        """Adding last pair to the tour due to inability at current time to find best full simulation formula"""
        for team in teams:
            est = True
            for match in tour:
                if team in match:
                    est = False
            if est == True:
                game.append(team)
        tour.append(game)
        #if tuple(game) in perm:
            #perm.remove(tuple(game))

        lastGameSwap()

        schedule.insert(i,tour)
        if elig == True:
            if len(first) < (len(teams) -1):
                first.append(tour)
            else:
                second.append(tour)
        else:
            if len(second) >= (len(teams) -1):
                first.append(tour)
            else:
                second.append(tour)

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



drawSchedule(perm)

schedule = lastGameSwap()



with open("data/test_schedule.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["tour", "homeTeam","awayTeam"])
    for i in range(len(first)):
        for game in first[i]:
            writer.writerow({"tour": i + 1, "homeTeam": game[0],"awayTeam": game[1] })
    for i in range(len(second)):
        for game in second[i]:
            writer.writerow({"tour": i + len(teams),"homeTeam": game[0],"awayTeam": game[1]})