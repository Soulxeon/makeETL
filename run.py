import time
import settings
from startCheck import startCheck 

def run():
    start_time = time.time()
    settings.init()
    startCheck.check_init()
    #Validation
    #Report
    time_process = round(time.time() - start_time, 2)
    print("Process finished --- {0} seconds ---".format(time_process))

if __name__ == '__main__':  
    run()
