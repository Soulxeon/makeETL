import pandas as pd

class FnameExt:

    ext_df = pd.DataFrame(columns=['filepath', 'workspace', "dataset", "collection", "filename", 'imagerytype',
                                       'imageType', 'startDepth', 'endDepth', 'startbox','endbox','status','flag_error',
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

        FnameExt.ext_df.loc[FnameExt.ext_df['filename_fix'].str.contains('DETA|SAMPL'),'imageType'] = 'Sample'
    
    def fnameWetDry(self):

        # FnameExt.ext_df.loc[FnameExt.ext_df['filepath'].str.upper().str.contains('DRY|_D'),'imageType'] = 'DryUncropped'
        # FnameExt.ext_df.loc[FnameExt.ext_df['filepath'].str.upper().str.contains('WET|_W|'),'imageType'] = 'WetUncropped'
        FnameExt.ext_df.loc[FnameExt.ext_df['filename_fix'].str.contains('DRY|_D'),'imageType'] = 'DryUncropped'
        FnameExt.ext_df.loc[FnameExt.ext_df['filename_fix'].str.contains('WET|_W'),'imageType'] = 'WetUncropped'
    
    def fnameSetImgry(self):

        FnameExt.ext_df.loc[FnameExt.ext_df['imageType'].str.contains('Uncropped'),'imageryType'] = 'Core Boxes'
        FnameExt.ext_df.loc[FnameExt.ext_df['imageType'] == 'Sample', 'imageryType'] = 'Core Boxes'


    #box number
        # if filename *BX* or *BOX*
        #  \d+- or _+d
        
    def fnameDepths(self):

        FnameExt.ext_df['onlynumbers'] = FnameExt.ext_df['filename_fix'].str.replace("[A-Z]+[0-9]+", "", regex=True)
        FnameExt.ext_df['onlynumbers'] = FnameExt.ext_df['onlynumbers'].str.replace("[A-Z]", "", regex=True)
        FnameExt.ext_df['depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+\.\d+)-(\d+\.\d+)')
        # FnameExt.ext_df.loc[(pd.isnull(FnameExt.ext_df['depths'])),'depths'] = FnameExt.ext_df['filename_fix'].str.findall(r'(\d+\.\d+)_(\d+\.\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+\.\d+)_(\d+\.\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+\.\d+)-(\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+)-(\d+\.\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+\.\d+)_(\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+)_(\d+\.\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+)-(\d+)')
        FnameExt.ext_df.loc[(FnameExt.ext_df['depths'].str.len()==0),'depths'] = FnameExt.ext_df['onlynumbers'].str.findall(r'(\d+)_(\d+)')

        # pd.to_numeric(FnameExt.ext_df['startDepth'])
        # pd.to_numeric(FnameExt.ext_df['endDepth'])

        # print(FnameExt.ext_df)

        FnameExt.ext_df['startDepth'] = FnameExt.ext_df['depths'].str[-1].str[0].apply(lambda x: float(x))
        FnameExt.ext_df['endDepth'] = FnameExt.ext_df['depths'].str[-1].str[1].apply(lambda x: float(x))

        # pd.to_numeric(FnameExt.ext_df['startDepth'],errors='coerce')
        # pd.to_numeric(FnameExt.ext_df['endDepth'],errors='coerce')

        # print(FnameExt.ext_df.dtypes)


        # print( FnameExt.ext_df)

        # FnameExt.ext_df.loc[(FnameExt.ext_df['startDepth'] > FnameExt.ext_df['endDepth']) | (abs(FnameExt.ext_df['startDepth'] - FnameExt.ext_df['endDepth']) > 100 ),'startDepth'] = ''
        # FnameExt.ext_df.loc[(FnameExt.ext_df['startDepth'] > FnameExt.ext_df['endDepth']) | (abs(FnameExt.ext_df['startDepth'] - FnameExt.ext_df['endDepth']) > 100 ),'endDepth'] = ''
    
    def dropExtractColumns(self):
        FnameExt.ext_df = FnameExt.ext_df.drop(columns= ['depths','filename_fix','onlynumbers'])



