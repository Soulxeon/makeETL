from db_conn import retrieveDB,tmp_tables
from extractInfo.filenamecheck import FnameExt
from visualCheck import visualcheck
import pandas as pd
import format
import settings


def extract_init():    
    filter_data = retrieveDB.retrieveAllData(mode='extract') #imageType not Sample
    toext_data = FnameExt(filter_data)

    print('checking filename Data')
    toext_data.fnameTransform()
    toext_data.fnameCopy()
    toext_data.fnameSamples()
    toext_data.fnameWetDry()
    toext_data.fnameSetImgry()
    toext_data.fnameDepths()
    toext_data.dropExtractColumns()
    data_extracted = toext_data.ext_df
    print('checking image Data')
    data_imgcheck = visualcheck.checkImageProperties(data_extracted)
    data_imgcheck['status'] = 'InfoExtracted'
    format.etlToCsv(data_imgcheck,settings.extract_visual)
    while True:
        startcheck = input(f"Check the data; do you want to update the DB table? y/n   ")
        if startcheck == "y":
            print("Table will be updated")
            tmp_tables.merge_extract()
            print("Table updated")
            break
        elif startcheck == "n":
            print("Table will no be updated")
            break
        else:
            print("\n please introduce a valid response.\n")
