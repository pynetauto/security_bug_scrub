# -*- coding: utf-8 -*-
import json
import csv

# Load the json file
with open("./data3.json") as f:
    data = json.load(f)

# create the csv writer object
data1 = open('data3.csv', 'w')
csvwriter = csv.writer(data1)

count = 0

for dt in data:
    if count == 0:
        header = dt.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(dt.values())

data1.close()

