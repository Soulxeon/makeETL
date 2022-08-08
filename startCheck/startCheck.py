import os
import settings
import format
from startCheck.gen_dataframe import EtlList
from db_conn import checkTable, retrieveDB
from validations import dropExistData

def check_init():

    if checkTable.checkTable() == False:

        print('First Time Project')
        folderdata = EtlList(2, -2)
        folderdata.emptyDirs()
        #check special images .tiff .RAW .CR2
        folderdata.readQuick()
        folder_df = folderdata.etl
        format.etlToCsv(folder_df,settings.temp_csv)
        checkTable.createETLTable()
        os.remove(settings.temp_csv) 

    else:

        print('There is already images in this project')
        exist_data = retrieveDB.retrieveFilepath()
        new_data = EtlList(2, -2)
        new_data.emptyDirs()
        #check special images .tiff .RAW .CR2
        new_data.readQuick()
        new_data_df = new_data.etl
        new_data_filter = dropExistData.dropSameData(exist_data,new_data_df)
        if len(new_data_filter) == 0:
            print("There are no new images!")
        else:
            print("new images will be listed: " + str(len(new_data_filter)))
            format.etlToCsv(new_data_filter,settings.temp_csv)
            checkTable.mergeTable()
            os.remove(settings.temp_csv) 
        
    all_data = retrieveDB.retrieveAllData()
    format.etlToCsv(all_data,settings.db_csv)

if __name__ == '__main__':
    check_init()
