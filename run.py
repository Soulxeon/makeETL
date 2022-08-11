import time
import settings
from startCheck import startCheck 
from extractInfo import startExtractInfo
from visualCheck import startVisualCheck
from validations import startValidation
from report import startReport

def run():
    start_time = time.time()
    settings.init()
    # print("-------------------Starting Check----------------------")
    # startCheck.check_init()
    # print("-------------------Extracting Info----------------------")
    # startExtractInfo.extract_init()
    print("-------------------Visual Check----------------------")
    startVisualCheck.check_init()
    # print("-------------------Validation----------------------")
    # startValidation.validation_init()
    # #validation
    # print("-------------------Output/Report----------------------")
    # #Report
    # startReport.report_init()
    # print("-------------------Cloud Check----------------------")
    # #Maybe check Cloud?
    
    print("------------------------Done!-------------------------")
    time_process = round(time.time() - start_time, 2)
    print("Process finished --- {0} seconds ---".format(time_process))

if __name__ == '__main__':  
    run()
