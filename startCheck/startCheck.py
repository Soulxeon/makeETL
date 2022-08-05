import settings
from startCheck.gen_dataframe import EtlList
from startCheck import format
from db_conn import checkTable, retrieveDB
from validations import dropExistData

def check_init():

    if checkTable.checkTable() == False:

        print('First Time Project')
        folderdata = EtlList(3, 4)
        folderdata.emptyDirs()
        #check special images .tiff .RAW .CR2
        folderdata.readQuick()
        folder_df = folderdata.etl
        if settings.img_process:
            format.imageSettingEtlcsv(folder_df)
        format.rawEtlcsv(folder_df)
        checkTable.createETLTable()

    else:

        print('There is already images in this project')
        exist_data = retrieveDB.retrieveFilepath()
        new_data = EtlList(3, 4)
        new_data.emptyDirs()
        #check special images .tiff .RAW .CR2
        new_data.readQuick()
        new_data_df = new_data.etl
        new_data_filter = dropExistData.dropSameData(exist_data,new_data_df)
        if len(new_data_filter) == 0:
            print("There are no new images!")
        else:
            print("new images will be listed: " + str(len(new_data_filter)))
            format.rawEtlcsv(new_data_filter)
            checkTable.mergeTable()
        
    all_data = retrieveDB.retrieveAllData()
    format.etlDB(all_data)





if __name__ == '__main__':
    check_init()


