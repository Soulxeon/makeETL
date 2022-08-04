import pandas as pd

def dropSameData(df1,df2):

    new_df = df1.merge(df2, on='filepath', how='right', indicator=True)\
             .query('_merge == "right_only"')\
             .drop(columns='_merge')
    return (new_df)
