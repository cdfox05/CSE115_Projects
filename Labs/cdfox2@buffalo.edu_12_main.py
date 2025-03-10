def countAlpha(fName):
    count = 0
    with open(fName) as fp:
        for line in fp:
            line = line.rstrip('\r\n')
            for letter in line:
                if (letter.isalpha()):
                    count += 1
    return count


def readAddressBook(fName):
    adict = {}
    with open(fName) as fp:
        for line in fp:
            line = line.rstrip("\r\n")
            adict[line.split(':')[0]] = line.split(':')[1]
    return adict

def writeAddressBook(fName, aDict):
    with open(fName, mode = 'w') as fp:
        for key in aDict.keys():
            aStr = str(key) + ":" + str(aDict[key]) + '\n'
            fp.write(aStr)
        
        
