import psycopg2
from db_conn.config import config
import settings
import pandas as pd

def retrieveFilepath():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        cur.execute(f"""SELECT filepath
                        FROM {settings.name_project};"""
                    )
        df = pd.DataFrame(cur.fetchall(), columns = ['filepath'])
        print("number of files: that exist " + str(len(df)))

	# close the communication with the PostgreSQL
        cur.close()
        return (df)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit() 
            conn.close()
            print('Database connection closed.')