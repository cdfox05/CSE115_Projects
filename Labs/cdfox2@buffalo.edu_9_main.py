import csv

def listNegative(fileName):
    with open(fileName) as fp:
        temp = []
        reader = csv.reader(fp)
        for row in reader:
            if (int(row[len(row)-1]) < 0):
                temp.append(row)

    return temp

def writecsv(record, fileName):
    with open(fileName, 'w') as file:
        writer = csv.writer(file)
        for data in record:
            writer.writerow(data)

def reverseFields(fileName):
    with open(fileName, 'r') as file:
        records = []
        reader = csv.reader(file)
        for row in reader:
            records.append(row)
    with open(fileName, 'w') as file:

        writer = csv.writer(file)

        for alist in records:
            alist.reverse()
            writer.writerow(alist)
        
    
        
