from db_conn import retrieveDB
import pandas as pd
from visualCheck import visualDepths,visualcheck
import format
import settings

def check_init():
    null_depth = retrieveDB.retrieveNullDepths()
    rotate_imgs = retrieveDB.retrieveRotate()
    while True:
        startcheck = input(f"there are {len(null_depth)} files with no depth: do you want to check it? y/n   ")
        if startcheck == "y":
            print("depth check selected")
            visual_check = visualDepths.visualDepthCheck(null_depth)
            format.etlToCsv(visual_check,settings.check_depths)
            break
        elif startcheck == "n":
            print("No depth check")
            break
        else:
            print("\n please introduce a valid response.\n")

    while True:
        startrotcheck = input(f"there are {len(rotate_imgs)} files with need to check the rotation: do you want to check it manually? y/n   ")
        if startrotcheck == "y":
            print("manual rotation check selected")
            visual_check = visualcheck.checkRotateImgs(rotate_imgs)
            break
        elif startrotcheck == "n":
            print("No manual rotation check")
            break
        else:
            print("\n please introduce a valid response.\n")
    

