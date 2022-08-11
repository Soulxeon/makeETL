from tkinter.tix import COLUMN
import pandas as pd
import settings
import numpy as np
import format

class Validations:

    def __init__(self,df):
        self.df = df

    def depthVal(self):
        tramsorted = self.df.drop(columns = ['workspace' ,'dataset', 'status', 'flag_error', 'exif','width','height','img_obs','project_code'])
        tramsorted = tramsorted.sort_values(by=['collection','imagerytype','imagetype','startdepth'])

        pd.to_numeric(tramsorted['startdepth'])
        pd.to_numeric(tramsorted['enddepth'])

        tramsorted['SAMEFT'] = (tramsorted['startdepth'] == tramsorted['enddepth'])
        tramsorted['tramsfixto'] = tramsorted.groupby(['collection','imagerytype','imagetype'])['enddepth'].shift(1)
        tramsorted['tramsfixfrom'] = tramsorted.groupby(['collection','imagerytype','imagetype'])['startdepth'].shift(-1)
        tramsorted['OVERLAP'] = (tramsorted['startdepth']-tramsorted['tramsfixto'] < 0) | (tramsorted['tramsfixfrom']-tramsorted['enddepth'] < 0)
        tramsorted['GAP'] = (tramsorted['startdepth']-tramsorted['tramsfixto'] > 0) | (tramsorted['tramsfixfrom']-tramsorted['enddepth'] > 0)
        tramsorted['COPY'] = tramsorted['tramsfixto'] == tramsorted['tramsfixfrom']
        tramsorted['delta'] = tramsorted['startdepth'] - tramsorted['tramsfixto']
        tramsorted.loc[ (0 < abs(tramsorted['delta'])) & (abs(tramsorted['delta']) < 1), 'fix_startdepth'] = tramsorted['tramsfixto']
        tramsorted.loc[ (0 < abs(tramsorted['delta'])) & (abs(tramsorted['delta']) < 1), 'fix_enddepth'] = tramsorted['enddepth']
        tramsorted.loc[ abs(tramsorted['delta']) == 0, 'fix_startdepth'] = tramsorted['startdepth']
        tramsorted.loc[ abs(tramsorted['delta']) == 0, 'fix_enddepth'] = tramsorted['enddepth']

        tramsorted.loc[(tramsorted['OVERLAP'] == True),'condition_error'] = 'Overlap'
        tramsorted.loc[(tramsorted['GAP'] == True),'condition_error'] = 'GAP'
        tramsorted.loc[(tramsorted['COPY'] == True),'condition_error'] = 'Copy'
        tramsorted.loc[(tramsorted['SAMEFT'] == True),'condition_error'] = 'Same Depth'

        tramsorted = tramsorted.drop(["tramsfixto", "tramsfixfrom","SAMEFT","COPY","OVERLAP","GAP"], axis = 1)
        onlyneedval = tramsorted.loc[(tramsorted['condition_error'].notnull())]

        if len(onlyneedval) == 0:
            print('you dont have depth issues! WOHO!!!')
        else:
            print(f'there are {len(onlyneedval)} depth issues')
            format.etlToCsv(onlyneedval,settings.check_depths)
