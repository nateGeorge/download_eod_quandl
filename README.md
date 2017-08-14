# download_eod_quandl
This downloads the data from the EOD database for stocks on Quandl.

# Usage
I've only tested and run this on Ubuntu 16.04.2 with Python3, so if you're going to use Mac or Windows, don't unless you can figure out how to set the environment variable for your Quandl api key, or set the variable `key` in the scripts to your Quandl api key.

## Set environment variable in Linux
Open `~/.bashrc` and add the line:

`export QUANDL_KEY=[your api key here, no brackets]`

Then, if you're in the same terminal do

`source ~/.bashrc`

Then change the `download_all.sh` to be executable:

`sudo chmod a+x download_all.sh`

and run the bash script `download_all.sh`.  This will execute the python scripts to download all the EOD data and the metadata.  The files will be in the folder `data` in the main repo folder.
