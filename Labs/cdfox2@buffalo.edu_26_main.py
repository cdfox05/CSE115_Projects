import csv

def partA(file):

    with open(file) as fp:

        reader = csv.reader(fp)
        header = next(reader)

    return header

def partB(file, al):

    with open(file, 'w') as fp:

        writer = csv.writer(fp)

        strings = []
        for alist in al:
            if (alist[0] not in strings):
                strings.append(alist[0])

        vals = []
        for string in strings:
            strTotal = 0
            for alist in al:
                if (alist[0] == string):
                    strTotal += alist[1]
            vals.append(strTotal)

        for x in range(len(strings)):
            writer.writerow([strings[x],vals[x]])

    
def partC(fileIn, fileOut, ad):

    with open(fileIn) as fI:

        reader = csv.reader(fI)
        headers = next(reader)

        data = []
        for row in reader:
            data.append(row)

        with open(fileOut, 'w') as fO:

            writer = csv.writer(fO)

            
            for key in ad.keys():
                if (key in headers):
                    writer.writerow([headers,ad[key]])
                
            

            for val in data:
                for key in ad.keys():
                    if (key not in val):
                        val.append('***')
                        writer.writerow(val)
                        val.pop()
                    else:
                        val.append(ad[key])
                        writer.writerow(val)
                        val.pop()

    return None
                    
                
            
            
