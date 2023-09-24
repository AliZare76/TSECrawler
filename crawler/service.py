import psycopg2
import pandas as pd

class DatabaseManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"cannot connect to database: {str(e)}")
    
    def disconnect(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            self.cursor = None
            self.conn = None
    
    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
    
    def commit(self):
        self.conn.commit()
    
    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        self.execute_query(query)
        self.commit()
    
    def insert_data(self, table_name, collected_data):
        try:
            columns = ', '.join(collected_data.columns)
            values_template = ', '.join(['%s'] * len(collected_data.columns))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_template});"
            values = [tuple(row) for row in collected_data.values]
            self.cursor.executemany(query, values)
            self.commit()
            print('inserting complete')
        except:
            print('error in inserting data to database')
    
    def execute_select_query(self, query, values=None):
        self.execute_query(query, values)
        return self.cursor.fetchall()
