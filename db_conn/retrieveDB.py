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
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        # execute a statement
        if mode == 'pending':
            cur.execute(f"""SELECT * FROM {settings.table_name} WHERE (status = 'Pending') AND imagetype is distinct from 'Sample' ORDERBY collection, filepath ;""")
        elif mode == 'extract':
            cur.execute(f"""SELECT * FROM {settings.table_name} WHERE (status = 'FirstCheck') AND imagetype is distinct from 'Sample'ORDERBY collection, filepath ;""")
        elif mode == 'validation':
            cur.execute(f"""SELECT * FROM {settings.table_name} WHERE (status = 'InfoExtracted') AND imagetype is distinct from 'Sample'ORDERBY collection, filepath ;""")
        else:
            cur.execute(f"""SELECT * FROM {settings.table_name};""")

        df = pd.DataFrame(cur.fetchall(), columns=['filepath', 'workspace', "dataset", "collection", "filename", 'imagerytype',
                                                   'imagetype', 'startdepth', 'enddepth', 'startbox','endbox','status','flag_error',
                                                   'condition_error','exif', 'width', 'height','img_obs','project_code'])
        
        if mode == 'pending':
            print("Data retrieved: " + str(len(df)) + " pending Core Boxes Files in DB")
        elif mode == 'extract':
            print("Data retrieved: " + str(len(df)) + " First check files going to extract info")
        elif mode == 'validation':
            print("Data retrieved: " + str(len(df)) + " First check files going to validation")
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

def retrieveNullDepths():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        # execute a statement
        cur.execute(f"""SELECT * FROM {settings.table_name} WHERE (status = 'Pending') 
                                                            AND (imagerytype = 'Core Boxes' OR imagerytype ISNULL) 
                                                            AND (startdepth ISNULL OR enddepth ISNULL);""")

        df = pd.DataFrame(cur.fetchall(), columns=['filepath', 'workspace', "dataset", "collection", "filename", 'imagerytype',
                                                   'imagetype', 'startdepth', 'enddepth', 'startbox','endbox','status','flag_error',
                                                   'condition_error','exif', 'width', 'height','img_obs','project_code'])

        print("Null depths retrieved: " + str(len(df)) + " Files in DB")

        cur.close()
        return (df)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit() 
            conn.close()

def exportUpload():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        # execute a statement
        cur.execute(f"""COPY (SELECT workspace,dataset,collection,imagerytype,imagetype,filepath,startdepth,enddepth FROM {settings.table_name} WHERE (status = 'Pending')) 
                              TO '{settings.upload}'
                              WITH DELIMITER ',' CSV HEADER;""")

        print("Table exported")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit() 
            conn.close()

def retrieveRotate():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        # execute a statement
        cur.execute(f"""SELECT filepath,img_obs FROM {settings.table_name} WHERE (status = 'Pending') 
                                                            AND ( img_obs = 'Rotate') ;""")

        df = pd.DataFrame(cur.fetchall(), columns=['filepath','img_obs'])
        cur.close()
        return (df)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit() 
            conn.close()

