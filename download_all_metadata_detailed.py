import os
import urllib.request

key = os.environ.get('QUANDL_KEY')

save_folder = 'data/'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

for i in range(112):  # currently 111 pages to download
    page = str(i)
    url = 'https://www.quandl.com/api/v3/datasets.csv' \
          '?database_code=EOD&per_page=100&sort_by=id&page=' \
          + page + '&api_key=' + key
    urllib.request.urlretrieve (url, save_folder + \
                                'metadata_details_page' + \
                                page + '.csv')
