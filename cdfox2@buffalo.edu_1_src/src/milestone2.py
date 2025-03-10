import csv

def convertToDictionaries(keys = list, values = list):
    newList = []

    for list in values:
        newDict = {}
        
        for x in range(len(keys)):
            newDict[keys[x]] = list[x]
        
        newList.append(newDict)

    return newList

def loadRecords(fileName):
    finalList = []

    with open(fileName) as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        for row in reader:
            finalList.append(row)
    
    return finalList

def convertToLists(keys = list, lod = list):
    finalList = []

    for dict in lod:
        newList = []

        for x in range(len(keys)):

            if (keys[x] in dict):
                newList.append(dict[keys[x]])
            else:
                newList.append("")

        finalList.append(newList)
    return finalList

def writeRecords(fileName = __file__, records = list):
    with open(fileName, 'a') as file:
        
        writer = csv.writer(file)

        for record in records:
            writer.writerow(record)

    return None