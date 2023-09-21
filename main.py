import pandas as pd
import requests
import json
import psycopg2


def get_url(symbol_id, date):
    url = f"http://cdn.tsetmc.com/api/Shareholder/{symbol_id}/{date}"
    return url

def get_request(url):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json; charset=utf-8'
    }
    response = requests.get(url=url, headers=headers)
    return response.text

def json_to_dataframe(response):
    res_json = json.loads(response)
    return pd.DataFrame(res_json['shareShareholder'])

# Read the symbol IDs from the CSV file
symbol_ids_df = pd.read_csv('./TSE Symbols.csv')
symbol_ids = symbol_ids_df['id'].tolist()
print(symbol_ids)

# Scraping date range 1 year
start_date = '2022-09-20'
end_date = '2023-09-20'
dates = pd.date_range(start=start_date, end=end_date).strftime("%Y%m%d")

# Connect to PostgreSQL database
# conn = psycopg2.connect(
#     host="your_host",
#     database="your_database",
#     user="your_user",
#     password="your_password"
# )

# # Create a cursor object
# cursor = conn.cursor()

# Iterate over symbol IDs
for symbol_id in symbol_ids:
    print(f"Scraping data for Symbol ID: {symbol_id}")
    
    # Start Crawling:
    df_list = []  # List to store dataframes for each date
    for date in dates:
        try:
            response = get_request(get_url(symbol_id=symbol_id, date=date))
            df = json_to_dataframe(response)
            df_list.append(df)
            print(f"Data for {date}:")
            print(df.head())
        except Exception as e:
            print(f"Error occurred for {date}: {str(e)}")
    
    # Combine all dataframes into a single dataframe
    combined_df = pd.concat(df_list, ignore_index=True)
    print(combined_df)
    # Create the shareHolders table in the database if it doesn't exist
#     create_table_query = '''
#         CREATE TABLE IF NOT EXISTS shareHolders (
#             id SERIAL PRIMARY KEY,
#             shareholderName TEXT,
#             numShares INT,
#             percentShares FLOAT,
#             date DATE,
#             symbolId TEXT
#         )
#     '''
#     cursor.execute(create_table_query)
#     conn.commit()
    
#     # Insert the data into the shareHolders table
#     for index, row in combined_df.iterrows():
#         insert_query = '''
#             INSERT INTO shareHolders (shareholderName, numShares, percentShares, date, symbolId)
#             VALUES (%s, %s, %s, %s, %s)
#         '''
#         values = (row['shareholderName'], row['numShares'], row['percentShares'], pd.to_datetime(row['date']).date(), symbol_id)
#         cursor.execute(insert_query, values)
    
#     # Commit the changes for the current symbol ID
#     conn.commit()

# # Close the cursor and the connection
# cursor.close()
# conn.close()