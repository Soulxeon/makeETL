from db_conn import retrieveDB
from report import report
import format

def report_init():
    df_retrieve = retrieveDB.retrieveAllData()
    df_report = report.Report(df_retrieve)
    df_report.generateReport()
    print('Report Done!')
    retrieveDB.exportUpload()
    print('Upload File Done!')


