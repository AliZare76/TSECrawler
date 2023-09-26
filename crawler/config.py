# constants
base_url='http://cdn.tsetmc.com/api/Shareholder'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json; charset=utf-8'
}

start_date = '2023-09-01'

end_date = '2023-09-20'

columns = ['cIsin VARCHAR(80)', 'change VARCHAR(80)', 'changeAmount VARCHAR(80)', 'dEven VARCHAR(80)', 'numberOfShares VARCHAR(80)',
            'perOfShares VARCHAR(80)', 'shareHolderID VARCHAR(80)', 'shareHolderName VARCHAR(80)', 'shareHolderShareID VARCHAR(80)', 'symbol_id VARCHAR(80)']

db_server = 'localhost'
db_name = 'postgres'
db_user = 'postgres'
db_password = '123456'