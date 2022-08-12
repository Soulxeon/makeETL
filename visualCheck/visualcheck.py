from PIL import Image, ExifTags
import pandas as pd
import settings
from db_conn import tmp_tables
import format
import cv2

def readimage(name):
    try:
        Image.open(name)
        return('')
    except:
        return('Failed to read image')

def verticalImg(df):
    df.loc[(df['width'] < df['height']),'img_obs'] = 'Vertical Image'
    return(df)


def checkImageRead(df):
    df_copy = df[['filepath','status','flag_error','condition_error']]
    df_copy['condition_error'] = df_copy.apply(lambda row: readimage(row['filepath']),axis=1)
    df_failedimg =  df_copy.loc[(df_copy['condition_error'] == 'Failed to read image')]
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
        try:
            width,height = image.size

        except:
            width,height = 0,0

        return ([0,width,height])


def checkImageProperties(df):
    df['img_properties'] = df.apply(lambda x: imageProperties(x['filepath']),axis=1)
    df[['exif','width','height']] = pd.DataFrame(df['img_properties'].tolist(), index= df.index)
    df = df.drop(columns = 'img_properties')
    df_check = verticalImg(df)
    return(df_check)



def checkRotateImgs(df):
    df_rot = df.loc[(df['img_obs']=='Rotate')]
    df_rot.apply(lambda x: rotateImg(x['filepath']),axis=1)



def rotateImg(name):
    # percent of original size
    scale_percent = 20
    im = cv2.imread(name)
    height = im.shape[0]
    width = im.shape[1]
    print('h = ' + str(height) + ', w = ' + str(width))
    widthfix = int(width * scale_percent / 100)
    heightfix = int(height * scale_percent / 100)
    dim = (widthfix, heightfix)
    resized_original = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized_original, cv2.COLOR_BGR2GRAY)

    cv2.imshow(name, gray)
    k = cv2.waitKey(0)
    if k == ord('s'):         # wait for 's' key to exit
        cv2.destroyAllWindows()
    elif k == ord('d'):  # wait for 'd' key to save and exit
        cv2.imwrite(name, cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE))
        cv2.destroyAllWindows()
    elif k == ord('a'): # wait for 'a' key to conutrerotate save and exit
        cv2.imwrite(name, cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE))
        cv2.destroyAllWindows()
    elif k == ord('w'):
        cv2.imwrite(name, cv2.rotate(im, cv2.ROTATE_180))
        cv2.destroyAllWindows()
