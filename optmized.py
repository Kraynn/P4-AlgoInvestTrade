"""
Algorithme optimisé qui retourne un investissement en se basant
sur un classement du profit des actions
"""


import csv
from time import perf_counter


def convert_csv(csv_name):
    data = open(csv_name, "r")
    csv_file = csv.reader(data)
    next(csv_file)
    return (list(
    (row[0], float(row[1]), float(row[2])) for row in csv_file))

def greedy_approximation(stocks, budget):
    stocks = sorted(stocks, key=lambda n:n[2], reverse=True)
    portfolio = {}
    shares_price = 0
    profit = 0
    for i in range(len(stocks)):
        name, price, value = stocks[i]
        if shares_price <= float(budget) and shares_price + price <= float(budget):
            shares_price += price
            portfolio[name] = price
            profit += value
        else:
            break
    return portfolio, shares_price, round(profit,2) 

def display_results(shares, shares_price, profit):        
    print(
        f"Les actions à acheter sont les suivantes: \n {','.join(shares)}",
        f"\n Coût total: {(shares_price)}",
        f"\n Profit : {profit} \n"
    )

def optimize():
    data = input("Quel est le nom du fichier au sein de votre répetoire? \n")
    budget = input("Quel est le budget choisi? \n")
    start = perf_counter()
    stocks = convert_csv(f"dataset/{data}.csv")
    shares, shares_price, profit = (greedy_approximation(stocks, budget))
    display_results(shares, shares_price, profit)
    end = perf_counter()
    print(end - start)


optimize()