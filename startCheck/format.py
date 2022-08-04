import pandas as pd
import settings

def rawEtlcsv(df):
     df.to_csv(settings.path + settings.name_project + '_RawPreview.csv', index=False)

# def simpleEtlcsv(df):
    #to fix with new columns
    # df.drop(columns=['exif', 'width', 'height'])
    # df['imageryName'] = ""
    # df['x'] = ""
    # df['y'] = ""
    # df['z'] = ""
    # df['flag'] = "None"
    # df = df[['workspace', 'dataset', 'collection', 'imageryType',
    #                        'imageType', 'imageryName', 'x', 'y', 'z', 'startDepth',
    #                        'endDepth', 'startBox', 'endBox', 'status', 'flag', 'filePath']]
    # df.to_csv(settings.path + settings.name_project + '_preview.csv', index=False)

def imageSettingEtlcsv(df):

    df = df[['filePath','exif','width','height',"img_obs"]]
    df.to_csv(settings.path + settings.name_project + 'ImageSetting.csv', index=False)
