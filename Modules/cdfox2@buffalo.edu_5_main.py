def postage(oz):
    if (oz < 0 or oz > 3.5):
        return None
    elif (oz <= 1):
        return .66
    elif (oz >1 and oz <= 2):
        return .9
    elif (oz > 2 and oz <= 3):
        return 1.14
    else:
        return 1.38

def bp_category(d, s):
    if (d < 80 and s < 120):
        return 'normal'
    if (d < 80 and s >= 120 and s <130):
        return 'elevated'
    if (d >= 90 or s >= 140):
        return 'hypertension stage 2'
    if ((d >= 80 and d <= 89) or (s >= 130 and s <= 139)):
        return 'hypertension stage 1'

def first_longest(list):
    temp = ''
    for x in range(len(list)):
        if (len(list[x]) > len(temp)):
            temp = list[x]
    return temp

def last_longest(list):
    temp = ''
    for x in range(len(list)):
        if (len(list[x]) >= len(temp)):
            temp = list[x]
    return temp

def total_length(list):
    total = 0
    for x in range(len(list)):
        total += len(list[x])
    return total

def zip(alist, blist):
    temp = []
    for x in range(len(alist)):
        temp.append(alist[x])
        temp.append(blist[x])
    return temp

def unzip(alist):
    temp1 = []
    temp2 = []
    for x in range(0,len(alist),2):
        temp1.append(alist[x])
    for x in range(1,len(alist),2):
        temp2.append(alist[x])
    return [temp1,temp2]

def oddValuesSum(list):
    sum = 0
    for x in range(len(list)):
        if (list[x] % 2 != 0):
            sum += list[x]
    return sum
        
def oddIndexSum(list):
    sum = 0
    for x in range(1,len(list),2):
        sum += list[x]
    return sum

def longStrings(list):
    temp = []
    for x in range(len(list)):
        if (len(list[x]) > 4):
            temp.append(list[x])
    return temp

def long_N_Strings(list, input):
    temp = []
    for x in range(len(list)):
        if (len(list[x]) > input):
            temp.append(list[x])
    return temp

def chooser(slist, blist):
    temp = []
    for x in range(len(slist)):
        if (blist[x]):
            temp.append(slist[x])
    return temp

def is_member(var, list):
    for x in range(len(list)):
        if (list[x] == var):
            return True
    return False

def intersection(alist,blist):
    temp = []
    for x in range(len(alist)):
        for y in range(len(blist)):
            if (alist[x] == blist[y]):
                if(not is_member(alist[x], temp)):
                    temp.append(alist[x])
    return temp

def difference(alist, blist):
    temp = []
    for x in range(len(alist)):
        num = 0
        for y in range(len(blist)):
            if (alist[x] == blist[y]):
                num+=1
        if (num == 0):
            if(not is_member(alist[x], temp)):
                temp.append(alist[x])
    return temp

def plusOne(list):
    for x in range(len(list)):
        list[x]+=1
    return None