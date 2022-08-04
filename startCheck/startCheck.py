import settings
from startCheck.gen_dataframe import EtlList
from startCheck import format
from db_conn import checkTable, createETLTable, onlyFilepath
from validations import dropExistData

def check_init():

    if checkTable.checkTable() == False:

        print('First Time Project')
        folderdata = EtlList(3, 4)
        folderdata.emptyDirs()
        folderdata.readQuick()
        folder_df = folderdata.etl
        if settings.img_process:
            format.imageSettingEtlcsv(folder_df)
        format.rawEtlcsv(folder_df)
        # createETLTable.connect()

    else:

        print('There is already images in this project')
        exist_data = onlyFilepath.retrieveFilepath()
        new_data = EtlList(3, 4)
        new_data.emptyDirs()
        new_data.readQuick()
        new_data_df = new_data.etl
        new_data_filter = dropExistData.dropSameData(exist_data,new_data_df)
        print("new images will be listed: " + str(len(new_data_filter)))
        format.rawEtlcsv(new_data_filter)

        # merge a la table existente




if __name__ == '__main__':
    check_init()


