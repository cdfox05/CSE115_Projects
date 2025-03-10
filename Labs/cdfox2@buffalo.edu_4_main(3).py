def how_many_single_digit_numbers(al):
    num = 0
    for x in range(len(al)):
        if (al[x] > -10):
            if (al[x] < 10):
                num+=1
    return num

def sum_of_single_digit_numbers(al):
    num = 0
    for x in range(len(al)):
        if (al[x] > -10):
            if (al[x] < 10):
                num += al[x]
    return num

print(sum_of_single_digit_numbers([9,3]))

def squares(al):
    for x in range(len(al)):
        al[x] = al[x]**2
    return al

print(squares([2,3,4]))
