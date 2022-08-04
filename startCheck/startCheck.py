import settings
from startCheck.gen_dataframe import EtlList
from startCheck import format
from db_conn import checkTable, createETLTable

def check_init():

    print(checkTable.checkTable())
    # folderdata = EtlList(3, 4)
    # folderdata.emptyDirs()
    # folderdata.readQuick()
    # folder_df = folderdata.etl
    # if settings.img_process:
    #     format.imageSettingEtlcsv(folder_df)
    # format.rawEtlcsv(folder_df)
    # createETLTable.connect()


if __name__ == '__main__':
    settings.init()
    check_init()


