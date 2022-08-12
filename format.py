import pandas as pd

def etlToCsv(df,path):
     df.to_csv(path, index=False)


