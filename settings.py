
def init():

    global path
    global img_process
    global code_project
    global depth_check
    global name_project

    path = r'H:\A0061_YamanaGold_CerroMorro\Old_Batch\\'
    code_project = 'A0061'
    depth_check = False
    img_process = False
    name_project = path.split('\\')[1]

    print("Reading Project: " + code_project)
    print("Folder Selected: " + path)

    if img_process is True:
        print("image Process Selected")
    else:
        print("Simple Process Selected")
    
    if depth_check is True:
        print("Intial Depths check Selected")




