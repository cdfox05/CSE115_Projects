def partA(fileName, letter):
    number = 0
    with open(fileName, 'r') as fp:
        for line in fp:
            for x in range(len(line)):
                if (line[x] == letter):
                    number +=1
    return number

def partB(file,al):
    with open(file, 'w') as fp:
        for string in al:
            fp.write(string + '\n')

def partC(file):
    temp = []
    with open(file, 'r') as fI:
        for line in fI:
            line.rstrip('\r\n')
            temp.append(line)
    with open(file + '.rev', 'w') as fO:
        while(len(temp) > 0):
            fO.write(temp.pop())
            
