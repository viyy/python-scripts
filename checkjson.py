import os
import sys
import json

if len(sys.argv) > 1:
    inputFile = sys.argv[1]
else:
    print("input json file:\n")
    inputFile = input()
if os.path.exists(inputFile):
    file = open(inputFile, "r")
    json.load(file)
    file.close()
    print("Validate JSON!")
else:
    print(inputFile + " not found")