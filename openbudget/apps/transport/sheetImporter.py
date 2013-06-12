import sys
sys.path.append('../../../')
import gdata.docs
import gdata.docs.service
import gdata.spreadsheet.service
import openbudget.settings.base as settings

metadataTypeIndex = 1
metadataYearIndex = 2
metadataMuniNameIndex = 0

#  This function recieves a google spreadsheet key and a workSheet index, 
#  and returns a tuple of the gdata entry object of that spreadsheet and it's metadata (muni name, type and year)
#  by default, the key points to the 'Hura Budget Data' sheet, and the workSheetNum to the Budget of 2010
def importSheet(key='0AoJzAmQXH28mdDZNakxVUHpZRnNKd0hzT2ZBQmNpMlE',workSheetNum = 2):    
    metaData = {}
    gd_client = gdata.spreadsheet.service.SpreadsheetsService()
    gd_client.email = settings.OPENBUDGET_GDATA_USER
    gd_client.password = settings.OPENBUDGET_GDATA_PASSWORD
    gd_client.source = 'payne.org-example-1'
    gd_client.ProgrammaticLogin()
    
    feed = gd_client.GetWorksheetsFeed(key = key)
    worksheet_id = feed.entry[workSheetNum].id.text.rsplit('/',1)[1]
   
    entry = gd_client.GetListFeed(key, worksheet_id).entry
    metaData['muniName'] = feed.title.text.split()[metadataMuniNameIndex].lower()
    metaData['typeName'] = feed.entry[workSheetNum].title.text.split()[metadataTypeIndex].lower()
    metaData['year'] = str(int(feed.entry[workSheetNum].title.text.split()[metadataYearIndex])) 
    return entry,metaData
