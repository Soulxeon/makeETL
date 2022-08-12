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
        
        print('tmp_errorimgs created...')

        cur.execute(f"""COPY tmp_errorimgs FROM '{settings.error_image}' DELIMITER ',' CSV HEADER  ;""")

        cur.execute(f""" UPDATE {settings.table_name}
                         SET    flag_error = tmp_errorimgs.flag_error,
	                            condition_error = tmp_errorimgs.condition_error,
	                            status = tmp_errorimgs.status
                                FROM   tmp_errorimgs
                                WHERE  {settings.table_name}.filepath = tmp_errorimgs.filepath;""")

        cur.execute("DROP TABLE tmp_errorimgs;")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit() 
            conn.close()

def merge_extract():
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute("""CREATE TEMP TABLE temp_merge (filepath varchar, workspace varchar, dataset varchar,collection varchar,filename varchar,imagerytype varchar,imagetype varchar,
                                                     startdepth numeric, enddepth numeric, startbox smallint, endbox smallint, status varchar, flag_error varchar,condition_error varchar,
                                                     exif smallint, width smallint, height smallint ,img_obs varchar,project_code varchar );""")
        
        print('temp_merge created...')

        cur.execute(f"""COPY temp_merge FROM '{settings.extract_visual}' DELIMITER ',' CSV HEADER  ;""")

        cur.execute(f""" UPDATE {settings.table_name}
                         SET workspace = temp_merge.workspace,
                             dataset = temp_merge.dataset,
                             collection = temp_merge.collection,
                             filename = temp_merge.filename,
                             imagerytype =  temp_merge.imagerytype,
                             imagetype = temp_merge.imagetype,
                             startdepth = temp_merge.startdepth,
                             enddepth = temp_merge.enddepth,
                             startbox = temp_merge.startbox,
                             endbox = temp_merge.endbox,
                             status = temp_merge.status,	   
                             flag_error = temp_merge.flag_error,
                             condition_error = temp_merge.condition_error,
                             exif = temp_merge.exif,
                             width = temp_merge.width,
                             height = temp_merge.height,
                             img_obs = temp_merge.img_obs,
                             project_code = temp_merge.project_code
                         FROM   temp_merge
                                WHERE  {settings.table_name}.filepath = temp_merge.filepath;""")

        cur.execute("DROP TABLE temp_merge;")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit() 
            conn.close()

def merge_depthVal():
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute("""CREATE TEMP TABLE temp_depthmerge (filepath varchar,collection varchar,filename varchar,imagerytype varchar,imagetype varchar,
                                                     startdepth numeric, enddepth numeric, startbox smallint, endbox smallint, condition_error varchar,
                                                     delta numeric, fix_startdepth numeric, fix_enddepth numeric);""")
        
        print('temp_depthmerge created...')

        cur.execute(f"""COPY temp_depthmerge FROM '{settings.check_depths}' DELIMITER ',' CSV HEADER  ;""")

        cur.execute(f""" UPDATE {settings.table_name}
                         SET startdepth = temp_depthmerge.fix_startdepth,
                             enddepth = temp_depthmerge.fix_enddepth,
                             startbox = temp_depthmerge.startbox,
                             endbox = temp_depthmerge.endbox,
                             condition_error = temp_depthmerge.condition_error
                         FROM   temp_depthmerge
                                WHERE  {settings.table_name}.filepath = temp_depthmerge.filepath;""")

        cur.execute("DROP TABLE temp_depthmerge;")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit() 
            conn.close()