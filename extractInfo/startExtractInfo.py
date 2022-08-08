from db_conn import retrieveDB
from extractInfo.filenamecheck import FnameExt
from visualCheck import visualcheck
import pandas as pd
import format
import settings

def extract_init():
    all_data = retrieveDB.retrieveAllData()

    visualcheck.checkImageRead(all_data)
    
    filter_data = retrieveDB.retrieveAllData(mode='pending') #imageType not Sample

    toext_data = FnameExt(filter_data)

    toext_data.fnameTransform()
    toext_data.fnameCopy()
    toext_data.fnameSamples()
    toext_data.fnameWetDry()
    toext_data.fnameSetImgry()
    toext_data.fnameDepths()
    toext_data.dropExtractColumns()

    data_extracted = toext_data.ext_df
    data_imgcheck = visualcheck.checkImageProperties(data_extracted)


    format.etlToCsv(data_imgcheck,settings.extract_visual)



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

