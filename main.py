import csv
import os
import json
from os import listdir
from os.path import isfile, join

currentDirectoryPath = './current/'
currentFileName = 'data.json'


def createRow (columnHeaders) :
    data = []
    amountOfColumn = len(columnHeaders)

    for column in columnHeaders :
        value = input("Bitte geben Sie den Wert für die Spalte " + column + " ein: ")
        data.append(value)

    return data

def importCSV () :
    filePath = './import/pending/'
    fileSavePath = './import/processed/'
    files = [f for f in listdir(filePath) if isfile(join(filePath, f))]

    for file in files:
        with open((filePath + file), newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            headers = data[0][0].split(';')
            mode = 1

            while mode != "0":
                print("aktuelle Datei: " + file)
                print("Menü:")
                print("1: Zeile hinzufügen")
                print("0: Speichern und beenden")

                mode = input("Was möchten Sie tun ? ")

                if mode == "1" :
                    newData = createRow(headers)
                    data.append(newData)

                if mode == "0" :
                    saveF = open(fileSavePath + file, 'w')
                    writer = csv.writer(saveF, delimiter=';')
                    for row in data :
                        writer.writerow(row)
                        saveF.flush()

                    saveF.flush()
                    saveF.close()
                    os.remove(filePath + file)




if __name__ == '__main__':
    importCSV()