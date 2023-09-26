from crawler import Crawler
from service import DatabaseManager
import pandas as pd

class Interface:
    def __init__(self):
        self.collected_data = []

    def assign(self, base_url, start_date, end_date):
        self.base_url = base_url
        self.start = start_date
        self.end = end_date
        print(f'controller set for crawling from {base_url} from {start_date} to {end_date}')

    def url_patterns(self, pattern):
        self.pattern = pattern
    
    def schema(self, columns):
        self.columns = columns
    
    def crawl(self):
        crawler = Crawler(base_url= self.base_url)
        crawler.crawl_data(self.pattern, self.start, self.end)
        self.collected_data = crawler.get_collected_data()

    def to_csv(self):
        self.collected_data.to_csv(f'./collection_{self.end}.csv')