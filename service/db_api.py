import pandas as pd
from fastapi import File, UploadFile
import io
from service.config import settings
from sqlalchemy import create_engine, text

class db_api(object):
    DB = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(db_api, cls).__new__(cls)
            cls.instance.DB = create_engine(settings.db_url)
        return cls.instance


    def __db_action(type):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                conn = self.DB.connect()
                res = func(self, conn=conn, **kwargs)
                if type == 'put':
                    conn.commit()
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
        df.to_sql(table, self.DB, if_exists='append', index=False)
        return table
    
    @__db_action('put')
    def push_df(self, conn, df, table, csv_name):
        conn.execute(text(f"""DELETE FROM {table} WHERE csv_name = '{csv_name}';"""))
        df.to_sql(table, self.DB, if_exists='append', index=False)
        return table
    
    @__db_action('get')
    def get_df(self, conn, table, csv_name):
        df = pd.read_sql_query(f"""SELECT * FROM {table} WHERE csv_name = '{csv_name}';""", self.DB)
        return df