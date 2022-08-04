import settings
from startCheck.gen_dataframe import EtlList
from startCheck import format
from db_conn import createETLTable

def check_init():

    folderdata = EtlList(1, 2)
    folderdata.emptyDirs()
    folderdata.readFolder()
    folder_df = folderdata.etl
    format.imageSettingEtlcsv(folder_df)
    format.rawEtlcsv(folder_df)
    createETLTable.connect()


if __name__ == '__main__':
    settings.init()
    check_init()


