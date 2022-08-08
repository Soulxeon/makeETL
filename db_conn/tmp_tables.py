import psycopg2
from db_conn.config import config
import settings

def merge_errorImgs():
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute("""CREATE TEMP TABLE tmp_errorimgs (filepath varchar, status varchar, flag_error varchar, condition_error varchar);""")
        
        print('temp_merge created...')

        cur.execute(f"""COPY tmp_errorimgs FROM '{settings.error_image}' DELIMITER ',' CSV HEADER  ;""")

        cur.execute(f""" UPDATE {settings.table_name}
                         SET    flag_error = tmp_errorimgs.flag_error,
	                            condition_result = tmp_errorimgs.condition_error,
	                            status = tmp_errorimgs.status
                                FROM   tmp_errorimgs
                                WHERE  {settings.table_name}.filepath = tmp_errorimgs.filepath;""")

        cur.execute("DROP TABLE temp_merge;")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit() 
            conn.close()
