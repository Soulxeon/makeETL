import pandas as pd
import settings

def rawEtlcsv(df):
     df.to_csv(settings.path + settings.name_project + '_RawPreview.csv', index=False)

def imageSettingEtlcsv(df):

    df = df[['filePath','exif','width','height',"img_obs"]]
    df.to_csv(settings.path + settings.name_project + 'ImageSetting.csv', index=False)
