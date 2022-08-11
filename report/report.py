import settings
import pandas as pd
from report.excelformat import front

class Report:

    def __init__(self,df):
        self.df = df

    def generateReport(self):
        etl = self.df
        etl = etl.drop(etl.columns[[14,15,16,17,18]], axis = 1)
        etl['Package'] = etl['filepath'].str.split('\\').str[2]
        df1 = etl.pop('filepath')
        etl['filepath'] = df1

        excluded = etl['filepath'][etl['status'] =='Excluded'].count()

        dataset = etl.groupby("Package").agg({"collection": ["nunique"], "filepath": ["count"]})
        dataset = dataset.rename(columns={'nunique': 'n_collections', 'count': 'n_images'})
        dataset = dataset.append(dataset.sum(numeric_only=True).rename('Total'))

        front.front(etl, dataset, excluded)

        togroup = etl.rename(columns={'filepath': 'n_images'})
        passedimages = etl[etl['status'] =='Pending']
        imageType = togroup.groupby(["collection","imagerytype","imagetype"])['n_images'].count()

        count = togroup.groupby(["dataset","collection"])['n_images'].count()

        maxmin = passedimages.groupby(['collection']).agg({"startdepth": ['min'],
                                                        "enddepth": ['max']
                                                        })


        with pd.ExcelWriter(settings.report, mode='a', engine="openpyxl") as writer:  
            imageType.to_excel(writer, sheet_name='Imageries')
            count.to_excel(writer, sheet_name='TREE')
            maxmin.to_excel(writer, sheet_name='StartEnd')
