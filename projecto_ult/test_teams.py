import random
import statistics
import csv

def createTeams():
    number = int(input("How many teams are in a league? : "))

    firstName = []
    lastName = []
    #teams = []
    with open("data/firstName.txt") as file:
        for line in file:
            firstName.append(line.rstrip())


    with open("data/lastName.txt") as file:
        for line in file:
            lastName.append(line.rstrip())

    with open("data/test_teams.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "rating"])
        for i in range(number):
            x = random.randint(0, 1000)
            random.seed(i + x)
            teamName = f"{firstName[random.randint(0, len(firstName) - 1)]} {lastName[random.randint(0, len(lastName) - 1)]}"
            ratings = [random.uniform(50, 59.99),random.uniform(60.00, 69.99),random.uniform(70.00, 79.99),random.uniform(80.00, 89.99),random.uniform(90.00, 94.99)]
            weights = [5, 10, 30, 40, 15]
            teamRating = round(statistics.fmean(random.choices(ratings,weights, k = 5)), 2)
            writer.writerow({"name": teamName, "rating": teamRating})


