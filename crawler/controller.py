from crawler import Crawler
from service import DatabaseManager
import pandas as pd
from config import *

class Interface:
    def __init__(self, base_url, start_date, end_date):
        self.collected_data = []
        symbol_ids_df = pd.read_csv('TSE Symbols.csv')
        self.pattern = symbol_ids_df['id'].tolist()
        self.columns = columns
        self.base_url = base_url
        self.start = start_date
        self.end = end_date
        print(f'controller set for crawling from {base_url} from {start_date} to {end_date}')
    
    def crawl(self):
        crawler = Crawler(base_url= self.base_url)
        crawler.crawl_data(self.pattern, self.start, self.end)
        self.collected_data = crawler.get_collected_data()

    def to_csv(self):
        self.collected_data.to_csv(f'./collection_{self.end}.csv')


    def sync_data(self):
        postgres = DatabaseManager(db_server, db_name, user = db_user, password = db_password)
        postgres.connect()
        postgres.create_table('share_holders',', '.join(self.columns))
        postgres.insert_data('share_holders', self.collected_data)
        postgres.commit()
        postgres.disconnect()