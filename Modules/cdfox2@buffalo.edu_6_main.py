def q1(ad):
    max = 0
    for value in ad.values():
        if (value > max or max == 0):
            max = value
    return max

def q2(ad, value):
    temp = []
    for key in ad.keys():
        if (ad[key] == value):
            temp.append(key)
    return temp

def q3(al, aStr):
    temp = []
    for ad in al:
        for key in ad.keys():
            if (key == aStr and ad not in temp):
                temp.append(ad)
    return temp


def q4(al, aInt):
    temp = []
    for ad in al:
        for value in ad.values():
            if (value == aInt and ad not in temp):
                temp.append(ad)
    return temp

def q5(dict1, dict2):
    finalDict = {}
    for key1 in dict1.keys():
        for key2 in dict2.keys():
            if (key1 == key2):
                finalDict[key1] = dict1[key1] + dict2[key2]
            elif (key1 not in finalDict.keys()):
                finalDict[key1] = dict1[key1]
    for key2 in dict2.keys():
        if (key2 not in finalDict.keys()):
            finalDict[key2] = dict2[key2]
    return finalDict

def q6(dict1, dict2):
    finalDict = {}
    for key1 in dict1.keys():
        for key2 in dict2.keys():
            if (key1 == key2):
                finalDict[key1] = [dict1[key1],dict2[key1]]
    return finalDict

def q7(filename):
    temp = []
    with open(filename) as fp:
        for line in fp:
            line.rstrip("\r\n")
            for word in line.split():
                if (word not in temp):
                    temp.append(word)
    return temp

def q8(fileIn, fileOut):
    with open(fileIn) as fI:
        with open(fileOut, mode='w') as fO:
            for line in fI:
                fO.write(line)

print(q5({'q': 5, 'c': 6, 'N': 4, 'J': 4, 'R': 7, 'A': 7, '7': 6, 'E': 7, 'i': 5, 'I': 5, 'u': 4, 'j': 7, 'Z': 6, 'n': 5, 'Q': 4, 'D': 7, 's': 6, 'l': 5, 'p': 7, 'Y': 5}, {'N': 7, 'H': 4, '4': 6, '9': 4, 'w': 7, '5': 6, 'm': 4, 'G': 6, 'p': 8, 'I': 8}))         
            