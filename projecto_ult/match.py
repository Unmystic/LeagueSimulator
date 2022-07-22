import csv
import random

table = []

class Match:

    def __init__(self, homeTeam, awayTeam):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam

    def __str__(self):
        return result(self.homeTeam, self.awayTeam )
"""
    def result(self,x,y):
        self.sc1 = goals(1.05 * x["rating"])
        self.sc2 = goals(0.95 * y["rating"])

        if self.sc1 > self.sc2 :
            return f"Team {x['name']} beat Team {y['name']} with score {self.sc1}:{self.sc2}"

        elif self.sc2 > self.sc1:
            return f"Team {x['name']} lost to Team {y['name']} with score {self.sc1}:{self.sc2}"

        elif self.sc1 == self.sc2:
            return f"Team {x['name']} draw Team {y['name']} with score {self.sc1}:{self.sc2}"

    def goals(self):
        rating = rating

        goal = [0, 1]
        weights = [100 - (rating * 100), rating]

        final = round(random.choices(goal,weights, k = 5))

        return final
"""

def main():

    teams = {}
    with open("data/teams.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["name", "rating"])
        for row in reader:
            teams[row["name"]] = row["rating"]
    #print(teams)

    for team in teams:
        #print(team)
        table.append({'name': team, 'rating' : teams[team],'gamesPlayed' : 0, 'goalsScored' : 0 , 'goalsConceded' : 0, 'points': 0})

    #for element in table:
        #print(element)


    calendar = []
    with open("data/schedule.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["tour", "homeTeam","awayTeam"])
        for row in reader:
            home = {}
            home["tour"] =  row["tour"]
            home["name"] =  row["homeTeam"]
            home["rating"] = teams[row["homeTeam"]]

            away = {}
            away["tour"] = row["tour"]
            away["name"] = row["awayTeam"]
            away["rating"] = teams[row["awayTeam"]]

            calendar.append([{"home": home ,"away":away}])

    for game in calendar:
        #print(game[0]['home'],game[0]['away'] )
        score = Match(game[0]['home'], game[0]['away'])
        #print(score)


    #print("  ")


    table.sort(reverse=True, key=Myfunc)

    #for position in table:
        #print(position)


def goals(r):
    """Determine goals scored by  the team based on rating"""
    #print(r)
    rating = r
    goal = [0, 1]
    if rating < 70:
        weights = [60, 40]
    elif 70 < rating < 75:
        weights = [50, 50]
    elif 75 < rating < 80:
        weights = [45, 55]
    elif 80 < rating < 85:
        weights = [40, 60]
    elif 85 < rating < 90:
        weights = [35, 65]
    elif 90 < rating < 95:
        weights = [25, 75]
    elif rating > 95:
        weights = [10, 90]

    #weights = [100 - rating , rating]
    #print(weights)

    final = round(sum(random.choices(goal,weights, k = 5)))

    return final

def result(x,y):
    """Determine result of the game based on goals scored"""
    #print(x["rating"])
    sc1 = goals(1.05 * float(x["rating"]))
    sc2 = goals(0.95 * float(y["rating"]))

    if sc1 > sc2 :
        for team in table:
            if x['name'] in team.values():
                team['gamesPlayed'] = team['gamesPlayed'] + 1
                team['goalsScored'] = team['goalsScored'] + sc1
                team['goalsConceded'] = team['goalsConceded'] + sc2
                team['points'] = team['points'] + 3

            elif y['name'] in team.values():
                team['gamesPlayed'] = team['gamesPlayed'] + 1
                team['goalsScored'] = team['goalsScored'] + sc2
                team['goalsConceded'] = team['goalsConceded'] + sc1

        return f"Team {x['name']} beat Team {y['name']} with score {sc1}:{sc2}"

    elif sc2 > sc1:
        for team in table:
            if y['name'] in team.values():
                team['gamesPlayed'] = team['gamesPlayed'] + 1
                team['goalsScored'] = team['goalsScored'] + sc2
                team['goalsConceded'] = team['goalsConceded'] + sc1
                team['points'] = team['points'] + 3

            elif x['name'] in team.values():
                team['gamesPlayed'] = team['gamesPlayed'] + 1
                team['goalsScored'] = team['goalsScored'] + sc1
                team['goalsConceded'] = team['goalsConceded'] + sc2


        return f"Team {x['name']} lost to Team {y['name']} with score {sc1}:{sc2}"

    elif sc1 == sc2:
        for team in table:
            if x['name'] in team.values():
                team['gamesPlayed'] = team['gamesPlayed'] + 1
                team['goalsScored'] = team['goalsScored'] + sc1
                team['goalsConceded'] = team['goalsConceded'] + sc2
                team['points'] = team['points'] + 1

            elif y['name'] in team.values():
                team['gamesPlayed'] = team['gamesPlayed'] + 1
                team['goalsScored'] = team['goalsScored'] + sc2
                team['goalsConceded'] = team['goalsConceded'] + sc1
                team['points'] = team['points'] + 1

        return f"Team {x['name']} draw Team {y['name']} with score {sc1}:{sc2}"

def Myfunc(e):
    """sort list with dictionary by one of values"""
    return e['points']


if __name__ == "__main__":
    main()