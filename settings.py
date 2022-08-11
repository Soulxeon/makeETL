import datetime

def init():

    global path
    global code_project
    global name_project
    global table_name
    global temp_csv
    global db_csv
    global error_image
    global extract_visual
    global check_depths
    global today_format
    global report
    global pre_upload
    global upload

    # path = r'H:\A0061_YamanaGold_CerroMorro\Old_Batch\\'
    path = r'H:\IM1037_CRG\\'
    code_project = 'IM1037'
    pre_upload = True

    name_project = path.split('\\')[1]
    table_name = name_project.lower()


    temp_csv = path + name_project + '_RawPreview.csv'
    db_csv = path + name_project + '_DB.csv'
    error_image = path + name_project + '_ErrorImages.csv'
    extract_visual = path + name_project + '_Extract.csv'
    check_depths = path + name_project + '_DChecks.csv'
    upload = path + name_project + '_toUpload.csv'

    today = datetime.datetime.now().date()
    today_format = today.strftime("%d-%m-%Y")
    report =  path + name_project + '_Report_' + today_format + '.xlsx'


    print('                    SETTINGS')
    print("Reading Project: " + code_project +" - " + name_project +"   ||" +"  Folder Selected: " + path)







