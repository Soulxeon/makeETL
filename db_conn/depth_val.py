import psycopg2
from db_conn.config import config
import settings
import pandas as pd

def retrieve():
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
        cur.execute(f"""SELECT collection,imagery_type,image_type,start_depth,end_depth,start_box,end_box,filepath,flag_error
                        FROM {settings.name_project}
                        WHERE status = 'Pending';"""
                    )
        df = pd.DataFrame(cur.fetchall(), columns = ['collection','imagery_type','image_type','start_depth','end_depth','start_box','end_box','filepath','flag_error'])

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

if __name__ == '__main__':
    retrieve()