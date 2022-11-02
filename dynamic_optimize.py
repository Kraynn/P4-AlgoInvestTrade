"""
Algorithme dynamique utilisant la méthode knapsack pour renvoyer la meilleur
stragégie d'investissement sur un grand nombre de données.
Budget = W, Coût de l'action = wt, Profit = val, Nombres d'actions = n
"""


import csv
import os, psutil
from time import perf_counter


def convert_csv(csv_name):
    data = open(csv_name, "r")
    csv_file = csv.reader(data)
    next(csv_file)
    return (list(
    {"share" : row[0],
     "price": float(row[1]),
     "profit": float(row[2])*float(row[1])/100} for row in csv_file))

def filter_stocks(stocks):
    filtered_stocks = []
    for items in stocks:
        if float(items["price"]) > 0 and float(items["profit"]) > 0:
            items["price"] = int(items["price"])
            items["profit]"] = int(items["profit"])
            filtered_stocks.append(items)
    return filtered_stocks    
        
def dynamic_optimize(budget, stocks):
    n = len(stocks) 
    portfolio = []
    k = [[0 for x in range(budget + 1)]for x in range(n+1)] 
    for i in range(1, n+1):  
        for w in range(1, budget+1):  
            if stocks[i-1]["price"] < w: 
                k[i][w] = max((stocks[i-1]["profit"])+ k[i-1]
                               [w-(stocks[i-1]["price"])], k[i-1][w]) 
            else:
                k[i][w] = k[i-1][w]  

    while budget >= 0 and n >= 0: 
        share = stocks[n-1] 
        if k[n][budget] == k[n-1][budget - share["price"]] + share["profit"]: 
            portfolio.append(share) 
            budget -= share["price"]
        n -= 1 
    return portfolio

def display_results(portfolio):   
    price = 0
    profit = 0
    shares = []
    for items in portfolio:     
        price += items["price"]
        profit += items["profit"]
        shares.append(items["share"])
    print(
        f"Les actions à acheter sont les suivantes: \n {','.join(shares)}",
        f"\n Coût total: {(price)}",
        f"\n Profit : {round(profit,2)} \n"
    )

def optimize():
    data = input("Quel est le nom du fichier au sein de votre répetoire? \n")
    budget = int(input("Quel est le budget choisi? \n"))
    start = perf_counter()
    process = psutil.Process(os.getpid())
    stocks = convert_csv(f"dataset/{data}.csv")
    stocks = filter_stocks(stocks)
    portfolio = dynamic_optimize(budget, stocks)
    print("\n Solution optimisée (méthode dynamique)")
    display_results(portfolio)
    end = perf_counter()
    print(f"Temps d'execution: {end - start}")
    print(f"Mémoire utilisée: {process.memory_info().rss / 1048576} MB")

optimize()
