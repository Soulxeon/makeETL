import re
import pandas as pd
from visualCheck import visualcheck

def checkImageRead(df):
    df_copy = df[['filepath','condition_error','Excluded','flag_error']]
    df_copy['condition_error'] = df_copy.apply(lambda row: visualcheck.readimage(row['filepath']),axis=1)
    df_failedimg =  df_copy.loc[(df_copy['condition_error'] == 'Failed to read image')]
    df_failedimg['status'] = 'Excluded'
    df_failedimg['flag_error'] = 'Error'
    if len(df_failedimg) != 0:
        print(f'found {str(len(df_failedimg))} corrupted images')
        
        pass
    else:
        return('there are no corrupted images')


def checkImageType(filename):

    dry = ["dry", "Dry", "DRY"]
    wet = ["wet", "Wet", "WET"]

    if any(dry in filename for dry in dry):
        imageType = 'Dry'
    elif any(wet in filename for wet in wet):
        imageType = 'Wet'
    else:
        imageType = ''

    return (imageType)

def checkStartEndDepth(filename):
    decimal_expression = r'(\d+\.\d+)'

    result = re.findall(decimal_expression, filename)
    
    try:
        start_depth = result[0]
    except:
        start_depth = ''
    try:
        end_depth = result[-1]
    except:
        end_depth = ''
    if start_depth == end_depth:
        end_depth = ''

    return ([start_depth, end_depth])


# def readFolder(self):
#     for name in glob.glob(self.path + '**\*.[jpt][pni][gf]*', recursive=True):
#         dataset = name.split("\\")[self.n_dataset]
#         entity = name.split("\\")[self.n_entity]
#         filename = name.split("\\")[-1]
#         imageType = filenamecheck.checkImageType(filename)
#         if settings.depth_check is True:
#             startdepth, enddepth = filenamecheck.checkStartEndDepth(filename)
#         else:
#             startdepth, enddepth = ['', '']

#         if settings.img_process is True:
#             exif_info, width, height, img_obs = visualcheck.infoPreview(name)
#         else:
#             exif_info, width, height, img_obs = ['', '', '', '']

#         EtlList.etl.loc[len(EtlList.etl.index)] = [name,'',dataset, entity, filename, '', imageType, startdepth,
#                                 enddepth,'','','Pending','None','', exif_info, width, height, img_obs]

#         EtlList.count += 1
#         if EtlList.count % 1000 == 0:
#             print("{} files processed succesfully".format(EtlList.count))

#     print("total of {} files processed succesfully".format(EtlList.count))

