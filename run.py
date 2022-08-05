import time
import settings
from startCheck import startCheck 
from extractInfo import startExtractInfo

def run():
    start_time = time.time()
    settings.init()
    startCheck.check_init()
    # startExtractInfo.extract_init()
    #extract info
    #validation
    #Report
    time_process = round(time.time() - start_time, 2)
    print("Process finished --- {0} seconds ---".format(time_process))

if __name__ == '__main__':  
    run()
