def how_many_singletons(al):
    num = 0
    for x in range(len(al)):
        if (len(al[x]) == 1):
            num+=1
    return num

def sum_of_index_matching_lengths(al):
    sum = 0;
    for x in range(len(al)):
        if (len(al[x]) == x):
            sum += x
    return sum

def running_length(al):
    intL = []
    for x in range(len(al)):
        sum = len(al[x])
        if (len(intL) >= 1):
            for y in range(len(intL)):
                sum += len(al[y])
        intL.append(sum)
    return intL
            
                
