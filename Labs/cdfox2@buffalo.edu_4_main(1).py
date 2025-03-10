def partA(al):
    count = 0
    for x in range(len(al)):
        if (al[x] < 0):
            count+=1
    return count

def partB(al):
    nl = []
    for x in range(len(al)):
        if (x % 2 == 0):
            nl.append(len(al[x]))
    return nl

def partC(al):
    for x in range(len(al)):
        if (x % 2 != 0):
            al[x] = len(al[x])
    return None
