import csv

def convert_csv(csv_name):
    data = open(csv_name, "r")
    csv_file = csv.reader(data)
    next(csv_file)
    return (list(
    (row[0], float(row[1]), float(row[2])*float(row[1])/100) for row in csv_file))
