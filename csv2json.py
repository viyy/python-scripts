import csv
import json
import sys

#read args or from console
if len(sys.argv) > 1:
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
else:
    print("input csv file:\n")
    inputFile = input()
    print("output json file:\n")
    outputFile = input()
#load csv
rows = []
with open(inputFile, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        rows.append(row)
#manipulate
headers = rows.pop(0)
data = []
for row in rows:
    obj = {}
    i = 0
    for header in headers:
        obj[header] = row[i]
        i+=1
    data.append(obj)
#save
with open(outputFile, "w") as jsonFile:
    json.dump(data, jsonFile, indent=2)
