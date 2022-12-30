import csv
import random
import itertools
from pprint import pprint
from collections import defaultdict

teams = []
def teamList():
    with open("data/test_teams.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["name", "rating"])
        for row in reader:
            teams.append(row["name"])
    comb = list(itertools.permutations(teams, 2))      
    return comb


def first_draw(comb):
    random.shuffle(comb)
    li = []
    selected = []
    rejected = []
    count = 0
    for _ in range((len(teams) -1)) :
        li.append([])
    #print(len(li))
    #print(len(comb))
    for pair in comb:
       
        pair = list(pair)
        #print(pair)
        if [pair[1],pair[0]] not in selected:

            for tour in li:
                #print(tour)
                #if any(pair[0] in sl for sl in tour) or any(pair[1] in sl for sl in tour):
                if (pair[0] in itertools.chain(*tour)) or (pair[1] in itertools.chain(*tour)):
                    continue
                    
                else:
                    tour.append(pair)
                    selected.append(pair)
                    break
            if pair not in selected:
                print("oi")
                count += 1
                rejected.append(pair)
        else:
            print("yes")
            count += 1
            #rejected.append(pair)
    #print("*"*20)
    for item in li:
        print(len(item))
        for match in item:
            random.seed()
            x = random.choice([0,1])
            if x :
                match[0],match[1] = match[1],match[0]
    print(f" Accepted  - {len(selected)}")
    print(f" Rejected - {len(rejected)}")
    print(count)
    pprint(li)
    pprint(rejected)
    return li

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
    first = first_draw(comb)
    #drawSchedule(comb)
    #pprint(first)






