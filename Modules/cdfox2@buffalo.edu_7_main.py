import csv

def q1(file = __file__):
    
    temp = []
    
    with open(file) as fp:
        
        reader = csv.reader(fp)
        keys = next(reader)
        
        for row in reader:
            aDict = {}
            for x in range(len(row)):
                aDict[keys[x]] = row[x]
                
            temp.append(aDict)
            
    return temp

def q2(file = __file__, dList = list):
    
    with open(file, 'w') as fp:
        
        writer = csv.writer(fp)
        keys = []
        
        for key in dList[0].keys():
            keys.append(key)
        
        writer.writerow(keys)
        for dict in dList:
            writer.writerow(dict.values())
            
    return None

def q3(fileIn = __file__, fileOut = __file__, fieldNames = list):
    
    with open(fileIn) as fI:
        
        reader = csv.reader(fI)
        headers = next(reader)
        keys = fieldNames
        
        data = []
        
        for row in reader:
            aDict = {}
            for x in range(0,len(row),1):
                aDict[headers[x]] = row[x]
            
            data.append(aDict)
           
        print(data)
        
        temp = [] 
        for dict in data:
            for x in range(len(keys)):
                if (keys[x] in dict.keys()):
                    
                    temp.append(dict[keys[x]])
                    
        print(temp)
        
        with open(fileOut, 'w') as fO:
            
            writer = csv.writer(fO)
            writer.writerow(keys)
            
                            
            lines = []
            
            for x in range(0,len(temp),len(keys)):
                line = []
                for y in range(len(keys)):
                    line.append(temp[x+y])
                lines.append(line)
            
            print(lines)
            
            for l in lines:  
                writer.writerow(l)
    
    return None

def q4(fileIn, fileOut, fieldName, val):
    
    data = q1(fileIn)
    with open(fileIn) as fI:
        
        reader = csv.reader(fI)
        header = next(reader)
        
    with open(fileOut, 'w') as fO:
        
        writer = csv.writer(fO)
        writer.writerow(header)
        
        for record in data:
            print(record)
            if (record[fieldName] == val):
                writer.writerow(record.values())        