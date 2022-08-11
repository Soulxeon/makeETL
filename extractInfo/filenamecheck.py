import pandas as pd
import numpy as np
class FnameExt:

    ext_df = pd.DataFrame(columns=['filepath', 'workspace', "dataset", "collection", "filename", 'imagerytype',
                                   'imagetype', 'startdepth', 'enddepth', 'startbox','endbox','status','flag_error',
                                   'condition_error','exif', 'width', 'height','img_obs','project_code'])

    def __init__(self,df) :
        self.df = df
        FnameExt.ext_df = df

    def fnameTransform(self):

        FnameExt.ext_df['filename_fix'] = FnameExt.ext_df['filename'].str.replace('(\s\s+)', ' ', regex=True)
        FnameExt.ext_df['filename_fix'] = FnameExt.ext_df['filename_fix'].str.replace("[#,@,&,!,']", '').str.replace("&", '-')
        FnameExt.ext_df['filename_fix'] = FnameExt.ext_df['filename_fix'].str.upper()
        FnameExt.ext_df['filename_fix'] = FnameExt.ext_df['filename_fix'].replace({ '.JPG' : '', '.PNG' : '', '.JPEG' : '' }, regex=True)
        FnameExt.ext_df['filename_fix'] = FnameExt.ext_df['filename_fix'].str.replace(",", ".").str.replace(" ", "_")
        FnameExt.ext_df['filename_fix'] = FnameExt.ext_df['filename_fix'].str.replace("__", "_")

    def fnameCopy(self):

        FnameExt.ext_df.loc[FnameExt.ext_df['filename_fix'].str.contains('COP'),'condition_error'] = 'Check Copy'

    def fnameSamples(self):

        FnameExt.ext_df.loc[FnameExt.ext_df['filename_fix'].str.contains('DETA|SAMPL'),'imagetype'] = 'Sample'
    
    def fnameWetDry(self):

        # FnameExt.ext_df.loc[FnameExt.ext_df['filepath'].str.upper().str.contains('DRY|_D'),'imageType'] = 'DryUncropped'
        # FnameExt.ext_df.loc[FnameExt.ext_df['filepath'].str.upper().str.contains('WET|_W|'),'imageType'] = 'WetUncropped'
        FnameExt.ext_df.loc[(FnameExt.ext_df['filename_fix'].str.contains('DRY|_D')),'imagetype'] = 'DryUncropped'
        FnameExt.ext_df.loc[(FnameExt.ext_df['filename_fix'].str.contains('WET|_W')),'imagetype'] = 'WetUncropped'
    
    def fnameSetImgry(self):

        FnameExt.ext_df['imagerytype'] = 'Core Boxes'
        FnameExt.ext_df.loc[FnameExt.ext_df['imagerytype'] == 'Sample', 'imagerytype'] = 'Hand Samples'


    #box number
        # if filename *BX* or *BOX*
        #  \d+- or _+d
        
    def fnameDepths(self):

        FnameExt.ext_df['onlynumbers'] = FnameExt.ext_df['filename_fix'].str.replace("[A-Z]+[0-9]+", "", regex=True)
        FnameExt.ext_df['onlynumbers'] = FnameExt.ext_df['onlynumbers'].str.replace("[A-Z]", "", regex=True)
        FnameExt.ext_df['depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+\.\d+)-(\d+\.\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+\.\d+)_(\d+\.\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+\.\d+)-(\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+)-(\d+\.\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+\.\d+)_(\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+)_(\d+\.\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+)-(\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+)_(\d+)')
        FnameExt.ext_df['startdepth'] = FnameExt.ext_df['depths'].str[-1].str[0].apply(lambda x: float(x))
        FnameExt.ext_df['enddepth'] = FnameExt.ext_df['depths'].str[-1].str[1].apply(lambda x: float(x))
        FnameExt.ext_df.loc[(FnameExt.ext_df['startdepth'] > FnameExt.ext_df['enddepth']) | (abs(FnameExt.ext_df['startdepth'] - FnameExt.ext_df['enddepth']) > 100 ),['startdepth','enddepth']] = np.nan,np.nan

    def dropExtractColumns(self):
        FnameExt.ext_df = FnameExt.ext_df.drop(columns= ['depths','filename_fix','onlynumbers'])



