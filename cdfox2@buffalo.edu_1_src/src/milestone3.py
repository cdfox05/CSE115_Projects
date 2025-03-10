import milestone1 as m1
import milestone2 as m2
import os
import json
import matplotlib.pyplot as plt
import urllib.request

def loadWebpage(link):

    response = urllib.request.urlopen(link)
    content = response.read().decode()
    
    return content

def cacheAndLoadData(file = __file__):
    KEYS = ['title','category','type','medium','frame',
                'photo_url_link','artist', 'site','street_address',
                'city','zip_code','state','latitude','longitude']
    if not os.path.isfile(file):
        
        lod = json.loads(loadWebpage('https://data.buffalony.gov/resource/6xz2-syui.json'))
        
        al = (m2.convertToLists(KEYS,lod))
        
        final = [KEYS]
        for list in al:
            final.append(list)
        
        m2.writeRecords(file,final)
    
    records = m2.loadRecords(file)
    print(records)

    return m2.convertToDictionaries(KEYS, records)



def cleanData(data = list):

    for dict in data:
            if (dict['category'] != 'GRAPHICS ARTS'):
                dict['category'] = dict['category'].rstrip('S')
            else:
                dict['category'] = "GRAPHIC ARTS"
    return None

def plotPieForKey(key, data):
     
    frequencies = m1.computeFrequency(key,data)

    labelList = []
    for label in frequencies.keys():
        if label not in labelList:
            labelList.append(label)

    values = []
    for label in labelList:
        values.append(frequencies[label])

    
    plt.pie(values, labels =labelList)
    plt.show()

    
def plotBarForKey(key = str, data = list):
    
    frequencies = m1.computeFrequency(key,data)
    
    labelList = []
    for label in frequencies.keys():
        if label not in labelList:
            labelList.append(label)
    
    values = []
    for label in labelList:
        values.append(frequencies[label])
    
    plt.barh(labelList, values, align='center', label=labelList)
    plt.show()
    
def plotFilteredBarForKey(key = str,fkey = str,fval = str,data = list):
    
    records = m1.filterByKey(fkey,fval,data)
    plotBarForKey(key,records)
