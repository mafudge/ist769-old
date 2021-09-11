from urllib.error import HTTPError
import requests
import pandas as pd
import os 

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def lat_lng(location):
    try:
        tokens = location.split()
        lat = 1 if tokens[1] == 'N' else -1
        lng = 1 if tokens[3] == 'E' else -1

        return ( lat*float(tokens[0]), lng*float(tokens[2]) )
    except:
        return None

def save_file(source_url, target_file_path):
    response = requests.get(source_url)
    with open (target_file_path, "w") as f:
        f.write(response.text)

print("Making sure folders exist...")
folders = ['raw', 'one_file_csv', 'one_file_json', 'multi_file_csv', 'multi_file_json', 'raw/ref_data', 'multi_file_csv/ref_data', 'multi_file_json/ref_data']
for folder in folders:
    create_directory(folder)

print("Fetching Station Table from noaa.gov...")
stations_file = 'https://www.ndbc.noaa.gov/data/stations/station_table.txt'
stations_file_out = "raw/ref_data/station_table.txt"
save_file(stations_file, stations_file_out)

stations = pd.read_csv(stations_file,sep="|")
stations.columns = [ c.replace("#","").strip() for c in stations.columns]
stations['LATLNG'] = stations.apply(lambda r: lat_lng(r['LOCATION']), axis=1)
mb_stations = stations[ stations['TTYPE'].str.find('Moored') > -1 ]
print("Writing Out station Table...")
mb_stations.to_csv('multi_file_csv/ref_data/station_table.csv', index=False)
mb_stations.to_json('multi_file_json/ref_data/station_table.json', orient='records')

print("Gathering Realtime Weather Data for Moored Bouys from noaa.gov...")
readings = pd.DataFrame()
for row in mb_stations.to_records():
    try:
        file = f'https://www.ndbc.noaa.gov/data/realtime2/{row["STATION_ID"]}.txt'
        file_out = f'raw/{row["STATION_ID"]}.txt'
        df=pd.read_csv(file, delim_whitespace=True)
        df['READING_STATION_ID'] = row["STATION_ID"]
        save_file(file, file_out)
        df.to_csv(f'multi_file_csv/{row["STATION_ID"]}.csv', index=False)
        df.to_json(f'multi_file_json/{row["STATION_ID"]}.json', orient='records')
        print(f"[  OK   ] {file}")    
        readings = readings.append( df.loc[1:])
    except HTTPError:
        print(f"[MISSING] {file}")        
        pass
    
print("Writing out combined files...")
combined = mb_stations.merge(readings, how='inner', left_on='STATION_ID',right_on='READING_STATION_ID' )
combined_sorted = combined.sort_values(by = ['#YY','MM','DD','hh','mm', 'STATION_ID'],  ascending=True)
combined_sorted.to_csv('one_file_csv/noaa_bouy_meterological_data.csv', index=False)
combined_sorted.to_json('one_file_json/noaa_bouy_meterological_data.json', orient='records')