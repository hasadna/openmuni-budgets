import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'openbudget.settings.base'
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import incoming.importers
import tablib

#   This function recieves a Entry object and metaData from a gdata spreadsheet,
#   and writes it to a csv file in openbudget.fixures.israel
def writeToCsv((entry,metaData)):
    fileName = createFilenameFromMetadata(metaData)
    
    f=open('../../fixtures/israel/'+fileName,'w')
    
    headers=[]
    titleRow = entry[0]
    data = tablib.Dataset()

    for key in titleRow.custom:
        headers.append(key)

    data.headers = headers

    for row in entry:
        record = []
        for key in row.custom:
            if row.custom[key].text == None: record.append("NONE")
            else: record.append(row.custom[key].text.decode('utf-8'))
        data.append(record)    
        
    f.write(data.csv)
    f.close()
    
def createFilenameFromMetadata(metaData):
    typeName = metaData['typeName']
    muniName = metaData['muniName']
    year = metaData['year']
    fileName = typeName+"_entity="+muniName+",period_start="+year+"-01-01;period_end="+year+"-12-31.csv"
    return fileName
