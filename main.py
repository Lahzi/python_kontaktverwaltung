from os import listdir
from os.path import isfile, join

def importCSV () :
    filePath = './import/pending/'
    files = [f for f in listdir(filePath) if isfile(join(filePath, f))]


if __name__ == '__main__':
    importCSV()