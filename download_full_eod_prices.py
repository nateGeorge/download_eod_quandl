import os
import urllib.request

key = os.environ.get('QUANDL_KEY')

save_folder = 'data/'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

url = 'https://www.quandl.com/api/v3/databases/EOD/data?api_key=' + key
urllib.request.urlretrieve(url, save_folder + 'full_EOD_data.csv')
