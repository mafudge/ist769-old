from urllib.error import HTTPError
import requests
import pandas as pd
import os 
import datetime

DATE_START = '2021-07-01'
DATE_END = '2021-08-31'

def create_directory(path):
    os.makedirs(path, exist_ok=True)


print("Making sure folders exist...")
folders = ['daily_requests_csv', 'daily_requests_json']
for folder in folders:
    create_directory(folder)

end_date = datetime.datetime.strptime(DATE_END,'%Y-%m-%d') #datetime.datetime.today()
start_date = datetime.datetime.strptime(DATE_START,'%Y-%m-%d')
time_diff = end_date - start_date

df = pd.read_csv('nyc311-2021.csv')

for i in range(time_diff.days):
    begin_date_range = start_date + datetime.timedelta(days=i)
    end_date_range = start_date + datetime.timedelta(days=i+1)
    next_date = begin_date_range 

    next_date_str = next_date.strftime('%Y-%m-%d')
    csv_file = f"daily_requests_csv/nyc311-{next_date_str}.csv"
    json_file = f"daily_requests_json/nyc311-{next_date_str}.json"
    print(f"Processing {csv_file}...")
    print(f"Processing {json_file}...")
    dataset = df[ (df['Created Date'] >= begin_date_range.strftime('%m/%d/%Y')) & (df['Created Date'] < end_date_range.strftime('%m/%d/%Y')) ]
    dataset.to_csv(csv_file, index=False)
    dataset.to_json(json_file, orient='records')
