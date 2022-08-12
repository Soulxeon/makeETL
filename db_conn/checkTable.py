import psycopg2
from db_conn.config import config
import settings

def checkTable():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(f"select exists(select * from pg_tables where tablename ='{settings.table_name}');")
        return(cur.fetchone()[0])
 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit() 
            conn.close()

def mergeTable():
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute("""CREATE TEMP TABLE temp_merge (filepath varchar, workspace varchar, dataset varchar,collection varchar,filename varchar,imagerytype varchar,imagetype varchar,
                                                     startdepth numeric, enddepth numeric, startbox smallint, endbox smallint, status varchar, flag_error varchar,condition_error varchar,
                                                     exif smallint, width smallint, height smallint ,img_obs varchar);""")
        
        print('temp_merge created...')

        cur.execute(f"""COPY temp_merge FROM '{settings.temp_csv}' DELIMITER ',' CSV HEADER  ;""")

        cur.execute(f"""ALTER TABLE temp_merge ADD COLUMN project_code varchar(50);
                        UPDATE temp_merge  SET project_code = '{settings.code_project}';
                        ALTER TABLE temp_merge ALTER COLUMN project_code SET NOT NULL;"""
                    )

        cur.execute(f""" INSERT INTO {settings.table_name}
                         SELECT * FROM temp_merge  ;""")
        
        print('new data merge...')

        cur.execute(f"DROP TABLE temp_merge;")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit() 
            conn.close()

def createETLTable():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {settings.table_name} (
                        filepath varchar(5000) NOT NULL,                        
                        workspace varchar(250) ,
                        dataset varchar(250) ,
                        collection varchar(250) ,
                        filename varchar(5000) ,
                        imagerytype varchar(250) ,
                        imagetype varchar(250) ,
                        startdepth numeric ,
                        enddepth numeric ,
                        startbox smallint ,
                        endbox smallint ,
                        status varchar(50) ,
                        flag_error varchar(50) ,
                        condition_error varchar(50),
                        exif smallint,
                        width smallint ,
                        height smallint,
                        img_obs varchar(50)
                         );"""
                    )
        cur.execute(f'TRUNCATE TABLE {settings.name_project}')
        cur.execute(f"""COPY {settings.name_project}(filepath, workspace, dataset, 
					    collection, filename, imagerytype, imagetype, startdepth, enddepth, 
                        startbox, endbox, status, flag_error, condition_error, exif, width,
                        height, img_obs)
                       FROM '{settings.temp_csv}'
                       DELIMITER ','
                       CSV HEADER;"""
                    )
        cur.execute(f"""ALTER TABLE {settings.table_name} ADD COLUMN project_code varchar(50);
                        UPDATE {settings.table_name}  SET project_code = '{settings.code_project}';
                        ALTER TABLE {settings.table_name} ALTER COLUMN project_code SET NOT NULL;"""
                    )

        print(f"Table {settings.table_name} was created")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit() 
            conn.close()
            print('Database connection closed.')
