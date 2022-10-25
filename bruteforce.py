"""
Algorithme bruteforce qui génère toutes les combinaisons possibles d'achats 
d'actions et qui retourne l'investissement qui génère le plus de profit
"""
from time import perf_counter
import csv
import itertools

def convert_csv(csv_name):
    data = open(csv_name, "r")
    csv_file = csv.reader(data)
    next(csv_file)
    return (list(
    (row[0], int(row[1]), float(row[2])*int(row[1])/100) for row in csv_file))

stocks = convert_csv("dataset/dataset.csv")
budget = 250

def check_cost(combi):
    price = 0
    for i in range(len(combi)):
        price += combi[i][1]
    if price < budget:
        return True
    else:
        return False

def calculate_profit(combi):
    profits = 0
    for i in range(len(combi)):
        profits += combi[i][2]
    return profits

def bruteforce():
    for k in range(7,12):
        combis = list(itertools.combinations(stocks, k))
        print(len(combis))
        for elem in combis:
            combi = list(elem)
            if check_cost(combi):
                calculate_profit(combi)



bruteforce()




