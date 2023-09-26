from crawler import Crawler
from service import DatabaseManager
import pandas as pd
from controller import Interface

# initialize interface for crawl
controller = Interface()
controller.assign(base_url='http://cdn.tsetmc.com/api/Shareholder',
                  start_date = '2023-09-01', end_date = '2023-09-20')

# Read the symbol IDs from the CSV file
symbol_ids_df = pd.read_csv('TSE Symbols.csv')
symbol_ids = symbol_ids_df['id'].tolist()
controller.url_patterns(symbol_ids)

# creat a new instance of Scraper and pass the arguments
controller.crawl()

# final data 
controller.to_csv()

# data schema
columns = ['cIsin VARCHAR(80)', 'change VARCHAR(80)', 'changeAmount VARCHAR(80)', 'dEven VARCHAR(80)', 'numberOfShares VARCHAR(80)',
            'perOfShares VARCHAR(80)', 'shareHolderID VARCHAR(80)', 'shareHolderName VARCHAR(80)', 'shareHolderShareID VARCHAR(80)', 'symbol_id VARCHAR(80)']
controller.schema(columns)

# setting up the database and inserting the data
postgres = DatabaseManager('localhost', 'postgres', user='postgres', password='123456')
postgres.connect()
postgres.create_table('share_holders',', '.join(columns))
postgres.insert_data('share_holders', scraped_data)
postgres.commit()
postgres.disconnect()
