
import psycopg2
from db_conn.config import config
import settings

def checkTable():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(f"select exists(select * from pg_tables where tablename ='{settings.name_project.lower()}');")
        return(cur.fetchone()[0])
 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit() 
            conn.close()
            print('Database connection closed.')