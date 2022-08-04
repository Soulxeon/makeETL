import psycopg2
from db_conn.config import config
import settings

def connect():
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
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {settings.name_project.lower()} (
                        filepath varchar(5000) NOT NULL,                        
                        workspace varchar(250) ,
                        dataset varchar(250) ,
                        collection varchar(250) ,
                        filename varchar(5000) ,
                        imageryType varchar(250) ,
                        imageType varchar(250) ,
                        startDepth numeric ,
                        endDepth numeric ,
                        startBox smallint ,
                        endBox smallint ,
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
					    collection, filename, imageryType, imageType, startDepth, endDepth, 
                        startBox, endBox, status, flag_error, condition_error, exif, width,
                        height, img_obs)
                       FROM '{settings.path + settings.name_project + '_RawPreview.csv'}'
                       DELIMITER ','
                       CSV HEADER;"""
                    )
        cur.execute(f"""ALTER TABLE {settings.name_project} ADD COLUMN project_code varchar(50);
                        UPDATE {settings.name_project}  SET project_code = '{settings.code_project}';
                        ALTER TABLE {settings.name_project} ALTER COLUMN project_code SET NOT NULL;"""
                    )

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit() 
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()