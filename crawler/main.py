from crawler import Crawler
from service import DatabaseManager
import pandas as pd
from controller import Interface
from config import *

# initialize interface for crawl
controller = Interface()
controller.assign(base_url=base_url, start_date = start_date, end_date = end_date)

# creat a new instance of Scraper and pass the arguments
controller.crawl()

# final data 
controller.to_csv()

# data schema
columns = columns
controller.schema(columns)

# setting up the database and inserting the data
controller.sync_data()
