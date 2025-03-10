def isNewValue(value, list):
    for val in list:
        if (value == val):
            return False
    return True


def getValuesForKey(key,records):
    temp = []
    for dict in records:
        for k in dict.keys():
            if (key == k):
                if(isNewValue(dict[key],temp)):
                    temp.append(dict[key])
    return temp

def countMatchesByKey(key,value,records):
    count = 0
    for dict in records:
        for k in dict.keys():
            if (k == key and dict[key] == value):
                count += 1
    return count

def countMatchesByKeys(key1,value1,key2,value2,records):
    count = 0
    for dict in records:
        for k in dict.keys():
            if (k == key1 and dict[key1] == value1):
                for k2 in dict.keys():
                    if (k2 == key2 and dict[key2] == value2):
                        count += 1
                
    return count

def filterByKey(key,value,records):
    listOfDicts = []
    for dict in records:
        for k in dict.keys():
            if (k == key and dict[key] == value):
                listOfDicts.append(dict)
    return listOfDicts

def computeFrequency(key, records):
    aDict = {}
    for dict in records:
        if (key in dict.keys()):
            if dict[key] not in aDict.keys():
                aDict[dict[key]]=1
            else:
                aDict[dict[key]]+=1
    return aDict



