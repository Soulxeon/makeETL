from PIL import Image, ExifTags
import pandas as pd
import settings
from db_conn import tmp_tables
import format


def readimage(name):
    try:
        Image.open(name)
        return('')
    except:
        return('Failed to read image')

def checkImageRead(df):
    df_copy = df[['filepath','status','flag_error','condition_error']]
    df_copy['condition_error_example'] = df_copy.apply(lambda row: readimage(row['filepath']),axis=1)
    df_failedimg =  df_copy.loc[(df_copy['condition_error_example'] == 'Failed to read image')]
    df_failedimg['status'] = 'Excluded'
    df_failedimg['flag_error'] = 'Error'
    if len(df_failedimg) > 0:
        print(f'found {str(len(df_failedimg))} corrupted images')
        format.etlToCsv(df_failedimg,settings.error_image)
        tmp_tables.merge_errorImgs()
        print('files excluded merged')
    else:
        print('there are no corrupted images')

def imageProperties(name):

    image = Image.open(name)
    try:

        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = dict(image._getexif().items())
        exif_info = str(exif[orientation])
        width,height = image.size
        return ([int(exif_info),width,height])

    except:
        return ([0,0,0])


def checkImageProperties(df):
    df['img_properties'] = df.apply(lambda x: imageProperties(x['filepath']),axis=1)
    df[['exif','width','height']] = pd.DataFrame(df['img_properties'].tolist(), index= df.index)
    df = df.drop(columns = 'img_properties')
    return(df)

