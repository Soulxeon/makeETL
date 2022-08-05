
def init():

    global path
    global code_project
    global name_project
    global table_name
    global temp_csv
    global db_csv

    # path = r'H:\A0061_YamanaGold_CerroMorro\Old_Batch\\'
    path = r'H:\ExifTest\\'
    code_project = 'IM6942'

    name_project = path.split('\\')[1]
    table_name = name_project.lower()
    temp_csv = path + name_project + '_RawPreview.csv'
    db_csv = path + name_project + '_DB.csv'


    print('                    SETTINGS')
    print("Reading Project: " + code_project +"   ||" +"  Folder Selected: " + path)







