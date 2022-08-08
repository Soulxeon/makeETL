import time
import settings
from startCheck import startCheck 
from extractInfo import startExtractInfo

def run():
    start_time = time.time()
    settings.init()
    print("-------------------Starting Check----------------------")
    startCheck.check_init()
    print("-------------------Extracting Info----------------------")
    startExtractInfo.extract_init()
    #extract info
    #validation
    #Report
    print("------------------------Done!-------------------------")
    time_process = round(time.time() - start_time, 2)
    print("Process finished --- {0} seconds ---".format(time_process))

if __name__ == '__main__':  
    run()
