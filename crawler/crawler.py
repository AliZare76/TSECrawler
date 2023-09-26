import pandas as pd
import requests
import json
from config import *

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.collected_data = []  # List to store the scraped data

    def get_url(self, symbol_id, date):
        url = f"{self.base_url}/{symbol_id}/{date}"
        return str(url)
    
    def get_request(self, url):
        response = requests.get(url=url, headers=headers)
        return response.text
    
    def crawl_data(self, symbol_ids, start_date, end_date):
            dates = pd.date_range(start=start_date, end=end_date).strftime("%Y%m%d")
            
            for symbol_id in symbol_ids:
                print(f"Scraping data for Symbol ID: {symbol_id}")
                
                for date in dates:
                    try:
                        url = self.get_url(symbol_id=symbol_id, date=date)
                        response = self.get_request(url)
                        self.process_data(response, symbol_id)
                        print(f"Data for {date} processed successfully")
                    except Exception as e:
                        print(f"Error occurred for {date}: {str(e)}")

    def process_data(self, response, symbol_id):
        # Process the response and extract the required data
        res_json = json.loads(response)
        df = pd.DataFrame(res_json['shareShareholder'])
        df['symbol_id'] = symbol_id
        print(df)
        # Store the scraped data
        self.collected_data.append(df)

    def get_collected_data(self):
        return pd.concat(self.collected_data)