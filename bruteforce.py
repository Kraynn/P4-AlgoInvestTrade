"""
Algorithme bruteforce qui génère l'ensemble des combinaisons possibles d'achats 
d'actions et qui retourne l'investissement le plus profitable
dans la limite du budget imposé en fonction du rendement
"""


import csv
import itertools
from time import perf_counter


def convert_csv(csv_name):
    data = open(csv_name, "r")
    csv_file = csv.reader(data)
    next(csv_file)
    return (list(
    (row[0], float(row[1]), float(row[2])*float(row[1])/100) for row in csv_file))
    
def check_cost(combi, budget):
    price = 0
    for i in range(len(combi)):
        price += combi[i][1]
    if price <= budget:
        return True
    else:
        return False

def calculate_profit(combi):
    profits = 0
    for i in range(len(combi)):
        profits += combi[i][2]
    profit_combi = (profits, combi)
    return profit_combi

def display_results(stock_list):
    portfolio = [shares[0] for shares in stock_list[1]]
    print(
        f"Les actions à acheter sont les suivantes: \n {','.join(portfolio)}",
        f"\n Coût total: {sum(shares[1] for shares in stock_list[1])}",
        f"\n Profit : {stock_list[0]} \n"
    )

def bruteforce():
    data = input("Quel est le nom du fichier au sein de votre répetoire? \n")
    budget = input("Quel est le budget choisi? \n")
    start = perf_counter()
    stocks = convert_csv(f"dataset/{data}.csv")
    stock_selection = []
    for k in range(1,len(stocks)):
        combis = list(itertools.combinations(stocks, k))
        for elem in combis:
            combi = list(elem)
            if check_cost(combi, budget):
                stock_selection.append(calculate_profit(combi))
    sorted_list = sorted(stock_selection, key=lambda n: n[0], reverse=True)
    display_results(sorted_list[0])
    end = perf_counter()
    print(end - start)


bruteforce()