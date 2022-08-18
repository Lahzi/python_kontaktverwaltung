import csv
import os
import json
from os import listdir
from os.path import isfile, join

currentDirectoryPath = './current/'
currentFileName = 'data.json'

def saveJSON () :
    if os.path.exists(currentDirectoryPath + currentFileName):
        os.remove(currentDirectoryPath + currentFileName)

def importCSV () :
    filePath = './import/pending/'
    files = [f for f in listdir(filePath) if isfile(join(filePath, f))]

    for file in files:
        with open((filePath + file), newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            headers = data[0][0].split(';')
            jsonList = []
            index = 0

            for row in data:
                if index > 0:
                    fields = row[0].split(';')
                    i = 0
                    entry = []
                    for header in headers:
                        entry.append([
                            header,
                            fields[i]
                        ])
                        i = i + 1

                    jsonList.append(entry)
                index = index + 1

            jsonString = json.dumps(jsonList, indent=4, sort_keys=True)
            print(jsonString)
            f = open(currentDirectoryPath + file + '.json', "w")
            f.write(jsonString)
            f.close()

if __name__ == '__main__':
    importCSV()
    saveJSON()