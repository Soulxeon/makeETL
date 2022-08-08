
def init():

    global path
    global code_project
    global name_project
    global table_name
    global temp_csv
    global db_csv
    global error_image
    global extract_visual

    # path = r'H:\A0061_YamanaGold_CerroMorro\Old_Batch\\'
    path = r'H:\IM1021_LunnonMetals\\'
    code_project = 'IM1021'

    name_project = path.split('\\')[1]
    table_name = name_project.lower()
    temp_csv = path + name_project + '_RawPreview.csv'
    db_csv = path + name_project + '_DB.csv'
    error_image = path + name_project + '_ErrorImages.csv'
    extract_visual = path + name_project + '_Extract.csv'


    print('                    SETTINGS')
    print("Reading Project: " + code_project +"   ||" +"  Folder Selected: " + path)







