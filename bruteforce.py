"""
Algorithme bruteforce qui génère une grande combinaisons possibles d'achats 
d'actions et qui retourne l'investissement qui génère le plus de profit 
dans la limite du budget imposé
"""


import csv
import itertools


def convert_csv(csv_name):
    data = open(csv_name, "r")
    csv_file = csv.reader(data)
    next(csv_file)
    return (list(
    (row[0], int(row[1]), float(row[2])*int(row[1])/100) for row in csv_file))

def check_cost(combi, budget = 500):
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
    profit_combi = (profits, combi)
    return profit_combi

def display_results(stock_list):
    portfolio = [shares[0] for shares in stock_list[1]]
    print(
        f"Les actions à acheter sont les suivantes: \n {','.join(portfolio)}",
        f"\n Coût total: {sum(shares[1] for shares in stock_list[1])}",
        f"\n Rendement : {stock_list[0]} \n"
    )

def bruteforce():
    stocks = convert_csv("dataset/dataset.csv")
    stock_selection = []
    for k in range(7,18):
        combis = list(itertools.combinations(stocks, k))
        for elem in combis:
            combi = list(elem)
            if check_cost(combi):
                stock_selection.append(calculate_profit(combi))
    sorted_list = sorted(stock_selection, key=lambda n: n[0], reverse=True)
    display_results(sorted_list[0])



bruteforce()




