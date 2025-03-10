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

def wordFrequency(file):
    frequency = {}
    with open(file) as fp:
        for line in fp:
            for word in line.split():
                if (word not in frequency.keys()):
                    frequency[word] = 1
                else:
                    frequency[word] += 1
    return frequency

def top10(aDict):
    temp = []
    while (len(temp) < 10):
        keys = []
        
        for word in aDict.keys():
            keys.append(word)
        
        maxKey = keys[0]

        for word in keys:
            if (aDict[word] >= aDict[maxKey]):
                maxKey = word

        temp.append(maxKey)
        aDict.pop(maxKey, None)
    return temp





def q9(fileIn, fileOut):
    
    words = wordFrequency(fileIn)
    topWords = top10(words)

    with open(fileOut, mode='w') as fp:
        for word in topWords:
            fp.write(word + '\n')


def q10(file1, file2):
    temp1 = []
    temp2 = []
    with open(file1, mode='r') as f1:
        for line in f1:
            temp1.append(line)
    with open(file2, mode='r') as f2:
        for line in f2:
            temp2.append(line)
    with open(file1+file2, mode='w') as fp:
        if (len(temp1) > len(temp2)):
            for x in range(len(temp1)):
                fp.write(temp1[x])
                if (x >= len(temp2)):
                    fp.write('\n')
                else:
                    fp.write(temp2[x])
        else:
            for x in range(len(temp2)):
                if (x >= len(temp1)):
                    fp.write('\n')
                else:
                    fp.write(temp1[x])
                fp.write(temp2[x])

                    

def q11(fileName, n):
    with open(fileName, mode='r') as fp:
        temp = []
        for line in fp:
            line = line.rstrip('\r\n')
            temp.append(line + '\n')
    
    print(temp)

    for i in range(1,n+1):
        with open(fileName.split('.')[0] + str(i) + '.' + fileName.split('.')[1], mode='w') as nf:                
            for x in range(len(temp)):
                val = (i+(x*n))-1
                print(val)
                if (val < len(temp)):
                    nf.write(temp[val])

def q12(fileName):
    with open(fileName) as fp:

        vowels = []
        consonants = []
        others = []

        for line in fp:
            for word in line:
                for letter in word:
                    if (letter.lower() in 'aoueiy'):
                        vowels.append(letter)
                    elif (letter.lower() in 'bcdfghjklmnpqrstvwxz'):
                        consonants.append(letter)
                    else:
                        others.append(letter)

    with open(fileName.split('.')[0] + '.vowels.' + fileName.split('.')[1], mode='w') as fVowel:
        for vowel in vowels:
            fVowel.write(vowel)

    with open(fileName.split('.')[0] + '.consonants.' + fileName.split('.')[1], mode='w') as fConsonant:
        for consonant in consonants:
            fConsonant.write(consonant)

    with open(fileName.split('.')[0] + '.others.' + fileName.split('.')[1], mode='w') as fOther:
        for other in others:
            fOther.write(other)


