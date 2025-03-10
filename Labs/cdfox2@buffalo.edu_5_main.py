def can_fit_in_room(ad,size):
    al = []
    for key in ad.keys():
        print(key)
        print(ad[key])
        if (size >= ad[key]):
            al.append(key)
    return al


def rooms_party_can_fit_in(size, ad):
    al = []
    for key in ad.keys():
        if (ad[key] >= size):
            al.append(key)
    return al

def possible_rooms(aDict, bDict):
    newDict = {}
    for key in aDict.keys():
        newDict[key] = rooms_party_can_fit_in(aDict[key], bDict)
    return newDict
    
