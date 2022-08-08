import psycopg2
from db_conn.config import config
import settings
import pandas as pd

def retrieveFilepath():
    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        # execute a statement
        cur.execute(f"""SELECT filepath
                        FROM {settings.table_name};"""
                    )
        df = pd.DataFrame(cur.fetchall(), columns = ['filepath'])
        print("number of files that exist in DB: " + str(len(df)))

	# close the communication with the PostgreSQL
        cur.close()
        return (df)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit() 
            conn.close()


def retrieveAllData(mode = 'a'):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        # execute a statement
        if mode == 'pending':
            cur.execute(f"""SELECT * FROM {settings.table_name} WHERE (status = 'Pending') AND imagetype is distinct from 'Sample';""")
        else:
            cur.execute(f"""SELECT * FROM {settings.table_name};""")

        df = pd.DataFrame(cur.fetchall(), columns=['filepath', 'workspace', "dataset", "collection", "filename", 'imageryType',
                                                   'imageType', 'startDepth', 'endDepth', 'startBox','endBox','status','flag_error',
                                                   'condition_error','exif', 'width', 'height','img_obs','project_code'])
        
        if mode == 'pending':
            print("Data retrieved: " + str(len(df)) + " pending Core Boxes Files in DB")
        
        else:
            print("All data retrieved: " + str(len(df)) + " Files in DB")

        cur.close()
        return (df)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit() 
            conn.close()