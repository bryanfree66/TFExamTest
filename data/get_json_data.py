import json
import os
import urllib.request


def retrieve_url(url, filename):
    if not (os.path.exists(filename) and not os.path.isfile(filename)):
        print(f'Downloading {filename}')
        urllib.request.urlretrieve(url,filename)
    else:
        print(f'{filename} already exists.')


def get_json_from_file(filename):
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


def print_dict(json_dict,items=5):
    print({x: json_dict[x] for (i,x) in enumerate(json_dict) if i < items})


def main():

    # Download the data
    url = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series/110/pcp/12/12/1895-2016.json?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    data_path = 'C:\\Users\\bryan\\local_code\\TFExamTest\\data'
    filename = f'{data_path}\\climate.json'
    retrieve_url(url,filename)

    # Load JSON
    json_data = get_json_from_file(filename)
    print(f'JSON keys: {json_data.keys()}')
    print_dict(json_data['data'])

    # Load JSON from string data
    with open(filename,'r') as json_file:
        raw_json = json_file.read()

    json_from_string = json.loads(raw_json)
    print(f'JSON keys: {json_from_string.keys()}')
    print_dict(json_from_string['data'])


if __name__ == "__main__":
    main()
