from db_conn import retrieveDB

def extract_init():
    all_data = retrieveDB.retrieveAllData()
        
    #filepath normal
        #validation file
        #excluded corrupted images
        #return [condition_error = 'Failed to read image', status = 'Excluded', flag_error = 'Error', filepath = 'filepath' ] => corrupted_imgs.csv
        #temp table -> update Table 
    
    filter_data = retrieveDB.retrieveAllData(mode='Pending') #imageType not Sample


        #extract class
            #filepath change
                #send randoms filenames
                #transform filenames
                    #remove multiple spaces preg_replace('/\s\s+/', ' ',$row['message']);
                    #remove special characters " ' "
                    #replaces "," for "."
                    #eliminate extension
                    #put all UPPER
                    #replace " " for "_"

                #check Copies - match *COP* unless entity match *COP* - return condition_error 'CheckCopy'
                #check HandSamples - *DETA* - *SAMPL* -> image type = 'Sample'

                #image_types
                    #extract filepath UPPER imagery type (WET,DRY,_W,_D) or filename (WET,DRY,_W,_D) -> image type = WetUncropped or DryUncropped

                #set imagerie type -> WetUncropped or DryUncropped = 'Core Boxes' and Sample = "Hand Samples"

                #box number
                    # if filename *BX* or *BOX*
                    #  \d+- or _+d

                #depths
                    # if filename has d\+M


    
            #filepath normal
                #called function for visualcheck
                    #visual check
                    #extract width

