def partA(oz):
    grams = (oz)*28.35
    return round(grams, 2)

def partB(lbs,oz):
    oz += lbs*16
    return oz

def partC(lbs,oz):
    grams = partA(partB(lbs,oz))
    kg = grams/1000
    return round(kg,4)
    
    
