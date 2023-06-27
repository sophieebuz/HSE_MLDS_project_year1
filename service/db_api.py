import sqlite3
import pandas as pd
from fastapi import File, UploadFile
import io

class db_api(object):
    DB = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(db_api, cls).__new__(cls)
            cls.instance.DB = sqlite3.connect(':memory:')
        return cls.instance


    def __db_action(type):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                conn = self.DB.cursor()
                res = func(self, conn=conn, **kwargs)
                if type == 'put':
                    self.DB.commit()
                conn.close()
                return res
            return wrapper
        return decorator
    
    @__db_action('put')
    def push_csv(self, conn, uploaded_file: UploadFile = File(...)):
        csv_name = uploaded_file.filename
        assert csv_name
        csv = io.StringIO(uploaded_file.file.read().decode())
        df = pd.read_csv(csv)
        table = csv_name.replace('.', '_')
        conn.execute(f"CREATE TABLE IF NOT EXISTS {table}(date,url,topic,tags,title,text)")
        df.to_sql(table, self.DB, if_exists='replace', index=False)
        # res = conn.execute(f"SELECT * FROM {table}")
        # print(res.fetchone())
        return table
    
    @__db_action('put')
    def push_df(self, conn, df, table):
        conn.execute(f"CREATE TABLE IF NOT EXISTS {table}(date,url,topic,tags,title,text,text_str,title_lemmas,year,month,day,date_enc,day_of_week,season,dummy_weekday,topic_le)")
        df.to_sql(table, self.DB, if_exists='replace', index=False)
        # res = conn.execute(f"SELECT * FROM {table}")
        # print(res.fetchone())
        return table
    
    @__db_action('get')
    def get_df(self, conn, table):
        df = pd.read_sql_query(f"SELECT * FROM {table}", self.DB)
        return df