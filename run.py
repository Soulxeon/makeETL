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
    # print("-------------------Visual Check----------------------")
    # # startVisualCheck.check_init()
    print("-------------------Validation----------------------")
    startValidation.validation_init()
    #output for ETL for null depths and Copies
    #perfrom better copy by grouping by
    #check wet Dry have same depth
    # # validation
    #merge data and put validate
    print("-------------------Output/Report----------------------")
    #Report
    #Askfor Hand Samples
    #Split in csv
    #Report show depth Issues-Excluded Images
    #Report show front number of hand samples and core boxes, maybe depth Issues
    startReport.report_init()
    # print("-------------------Cloud Check----------------------")
    # #Maybe check Cloud?
    
    print("------------------------Done!-------------------------")
    time_process = round(time.time() - start_time, 2)
    print("Process finished --- {0} seconds ---".format(time_process))

if __name__ == '__main__':  
    run()
