from db_conn import retrieveDB
from validations import validations

def validation_init():

    df_val = retrieveDB.retrieveAllData(mode = 'Pending')
    df = validations.Validations(df_val)
    df.depthVal()

